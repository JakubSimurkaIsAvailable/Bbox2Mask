from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenuBar, QLabel, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QAction, QIcon, QPixmap
from PyQt6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bbox2Mask")

        menu = self.menuBar()

        button_add_dataset = QAction("Add &Dataset", self)
        button_add_image = QAction("Add &Image", self)
        button_add_annotation = QAction("Add &Annotation", self)

        buton_draw = QAction("&Draw", self)
        button_remove_image = QAction("&Remove Image", self)

        file_menu = menu.addMenu("&File")

        file_menu.addAction(button_add_dataset)
        file_menu.addAction(button_add_image)
        file_menu.addAction(button_add_annotation)
 
        edit_menu = menu.addMenu("&Edit")

        edit_menu.addAction(buton_draw)
        edit_menu.addAction(button_remove_image)

        image_canvas = QLabel(self)
        pixmap = QPixmap("testimage.jpg")
        scaled_pixmap = pixmap.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        image_canvas.setPixmap(scaled_pixmap)
        self.setCentralWidget(image_canvas)
        

        layout = QVBoxLayout()
        navigation = BottomNavigation()
        layout.addWidget(image_canvas)
        layout.addWidget(navigation)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        

class BottomNavigation(QWidget):
    def __init__(self):
        super().__init__()
        back_button = QPushButton(self)
        next_button = QPushButton(self)

        back_button.setText("<-")
        next_button.setText("->")

        layout = QHBoxLayout()

        layout.addWidget(back_button)
        layout.addWidget(next_button)

        self.setLayout(layout)
        
        

        


app = QApplication([])

window = MainWindow()
window.show()

app.exec()