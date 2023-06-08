import sys
import time

from PyQt5.QtGui import QIcon, QPixmap, QFont, QRegExpValidator, QIntValidator, QTextCharFormat, QColor, QKeySequence
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QStackedLayout, QSplitter, \
    QWidget, QPushButton, QLabel, QDesktopWidget, QSizePolicy, QLineEdit, QTextEdit, QTextBrowser, QMessageBox, \
    QComboBox, QFontComboBox, QPlainTextEdit, QDial, QScrollBar, QSlider, QKeySequenceEdit
from PyQt5.QtCore import Qt, QRegExp, QTime
from PyQt5 import  uic
# from PyQt5 import *

# 在一个窗口中设计了一个按钮，点击该按钮就会弹出一个设置按钮快捷键的QKeySequenceEdit弹窗以供输入快捷键，输入完成后即将按钮快捷键设置为输入值。
from PyQt5.uic.properties import QtGui


class MyWindow01(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.resize(400, 600)
        self.setWindowTitle("Widget_KeySequence")

        mlayout = QVBoxLayout()
# ------------------------------------------------------------------------
        btn = QPushButton("点我设置快捷键")
        btn.clicked.connect(self.setBtnShortCut)



# ------------------------------------------------------------------------
        mlayout.addWidget(btn)

# ------------------------------------------------------------------------
        self.setLayout(mlayout)
# ------------------------------------------------------------------------
    def setBtnShortCut(self):
        self.keySeqEdit = QKeySequenceEdit()
        self.keySeqEdit.show()
        self.keySeqEdit.keySequenceChanged.connect(self.BtnShortCutChanged)

    def BtnShortCutChanged(self, ks):
        self.btn.setShortcut(ks)
        print(ks.toString())

class MyWindow02(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QKeySequenceEdit_快捷键')
        self.resize(500, 500)
        self.iniUI()

    ##############################################键序列编辑器 基本操作
    #
    # kse = QKeySequenceEdit()              创建一个键序列编辑器对象
    # ks  = QKeySequence(Qt.CTRL+Qt.Key_A)  创建一个键序列对象
    # kse.setKetSequence(ks)                将键序列对象设置到键序列编辑器上
    #
    #
    # kse.keySequence()  返回键序列对象ks
    # ks.toString()      返回键序列对象的字符串
    # ks.count()         返回键序列对象的个数
    #
    def iniUI(self):
        kse = QKeySequenceEdit(self)
        # ks = QKeySequence('ctrl+a')
        ks = QKeySequence(Qt.CTRL + Qt.Key_A)
        kse.setKeySequence(ks)

        # print(ks.toString())
        sds = kse.keySequence()  # 上面在编辑器kse上面设置了ks对象， 现在kse.keySequence()返回ks对象
        print(sds.toString())
        #############################键序列编辑器 基本操作

        ##############################################键序列编辑器 信号相关
        #
        #
        # editingFinished       结束编辑时 发射的信号
        # keySequenceChanged    键序列改变 发射的信号
        btn = QPushButton(self)
        self.btn = btn
        # self.btn_w = self.width() / 3
        # self.btn_h = self.height() * 3 / 32
        # self.btn.resize(self.btn_w, self.btn_h)
        # self.btn_x = (self.width() - self.btn_w) / 2
        # self.btn_y = self.height() * 7 / 8 + (self.height() / 8 - self.btn_h) / 2
        self.btn.setText('信号测试')
        self.btn.setStyleSheet('font-size:30px')
        # self.btn.move(self.btn_x, self.btn_y)

        self.btn.clicked.connect(lambda: print(kse.keySequence().toString(), kse.keySequence().count()))

        kse.editingFinished.connect(lambda: print('总是会在一秒钟之后编辑结束，发射信号'))
        kse.keySequenceChanged.connect(lambda ks_obj: print('键序列改变', ks_obj.toString()))
    #############################键序列编辑器 信号相关

        mlayout = QVBoxLayout()
        mlayout.addWidget(self.btn)
        self.setLayout(mlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow02()
    w.show()

    app.exec()