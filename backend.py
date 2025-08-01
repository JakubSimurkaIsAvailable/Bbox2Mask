import numpy as np
import cv2
import torch
import matplotlib.pyplot as plt
from segment_anything import sam_model_registry, SamPredictor
from segment_anything.utils.transforms import ResizeLongestSide



def load_image(imageurl):
    global image_original
    image_original = cv2.imread(imageurl)
    
def load_sam():
    global predictorSam, sam
    
    sam_checkpoint = "sam_vit_h_4b8939.pth"
    model_type = "vit_h"
    device = "cuda"
    
    sam = sam_model_registry[model_type](checkpoint = sam_checkpoint)
    sam.to(device = device)
    predictorSam = SamPredictor(sam)

def process_image(bboxes):
    image_boxes = torch.tensor(bboxes, device=sam.device)
    resize_transform = ResizeLongestSide(sam.image_encoder.img_size)
    batched_input = {
        'image': prepare_image(image_original, resize_transform, sam),
        'boxes': resize_transform.apply_boxes_torch(image_boxes, image_original.shape[:2]),
        'original_size': image_original.shape[:2]
    }
    batched_output = sam(batched_input, multimask_output = False)
    return batched_output[0]['masks']
    
def prepare_image(image, transform, device):
    image = transform.apply_image(image)
    image = torch.as_tensor(image, device=device.device)
    return image.permute(2, 0, 1).contiguous()