from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenuBar
from PyQt6.QtGui import QAction, QIcon
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

        

        


app = QApplication([])

window = MainWindow()
window.show()

app.exec()