import sys
import time

from PyQt5.QtGui import QIcon, QPixmap, QFont, QRegExpValidator, QIntValidator, QTextCharFormat, QColor
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QStackedLayout, QSplitter, \
    QWidget, QPushButton, QLabel, QDesktopWidget, QSizePolicy, QLineEdit, QTextEdit, QTextBrowser, QMessageBox, \
    QComboBox, QFontComboBox, QPlainTextEdit, QDial, QScrollBar, QSlider, QMainWindow, QListWidget, QDockWidget
from PyQt5.QtCore import Qt, QRegExp, QTime
from PyQt5 import  uic
# from PyQt5 import *

class MyWindown(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.resize(600, 400)
        self.setWindowTitle("Widget_Dock")
        text_edit = QTextEdit()
        self.setCentralWidget(text_edit)   #放在中心位置

        #创建DockWidget并将list_widget添加到其中
        list_widget = QListWidget()
        list_widget.addItem("DockHere")
        dock_widget1 = QDockWidget("DockWidget_1", self)
        dock_widget1.setWidget(list_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, dock_widget1)

        text_edit2 = QTextEdit()
        text_edit2.setText("Hello word!")
        dock_widget2 = QDockWidget("DockWidget_2", self)
        dock_widget2.setWidget(text_edit2)
        dock_widget2.setFloating(True)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget2)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindown()
    w.show()

    app.exec()