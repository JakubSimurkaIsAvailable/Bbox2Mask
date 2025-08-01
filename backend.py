import numpy as np
import cv2
import torch
import matplotlib.pyplot as plt
from segment_anything import sam_model_registry, SamPredictor
from segment_anything.utils.transforms import ResizeLongestSide

loaded_images = []
loaded_images_boxes = []
loaded_images_masks = []

def load_image(imageurl):
    global image_original
    image_original = cv2.imread(imageurl)
    loaded_images.append(image_original)
    
def load_boxes(boxes):
    loaded_images_boxes.append(boxes)
    
    #sets up segment anything model
def load_sam():
    global predictorSam, sam
    
    sam_checkpoint = "sam_vit_h_4b8939.pth"
    model_type = "vit_h"
    device = "cuda"
    
    sam = sam_model_registry[model_type](checkpoint = sam_checkpoint)
    sam.to(device = device)
    predictorSam = SamPredictor(sam)

    #gets the image and bboxes adds masks to the list
def process_image(bboxes, image_p):
    image_boxes = torch.tensor(bboxes, device=sam.device)
    resize_transform = ResizeLongestSide(sam.image_encoder.img_size)
    batched_input = {
        'image': prepare_image(image_p, resize_transform, sam),
        'boxes': resize_transform.apply_boxes_torch(image_boxes, image_p.shape[:2]),
        'original_size': image_p.shape[:2]
    }
    batched_output = sam(batched_input, multimask_output = False)
    loaded_images_masks.append(batched_output[0]['masks'])
    
    #helper function to transform image
def prepare_image(image, transform, device):
    image = transform.apply_image(image)
    image = torch.as_tensor(image, device=device.device)
    return image.permute(2, 0, 1).contiguous()

#TODO add method to create an annotation for the image in a specific format
#TODO convert images to their correct format