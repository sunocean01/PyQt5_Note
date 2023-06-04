import sys
import webbrowser
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QStackedLayout, QSplitter, \
    QWidget, QPushButton, QLabel, QDesktopWidget, QSizePolicy, QLineEdit, QTextEdit, QListWidget, QRadioButton, \
    QStackedWidget, QToolButton, QCheckBox, QCommandLinkButton, QDialogButtonBox, QMenu, QAction, QButtonGroup
from PyQt5.QtCore import Qt
from PyQt5 import uic


# from PyQt5 import *

# https://blog.csdn.net/weixin_50296259/article/details/130539311?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168515292116800180683050%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=168515292116800180683050&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-4-130539311-null-null.142^v88^control_2,239^v2^insert_chatgpt&utm_term=pyqt5%20qpushbutton%E6%A0%B7%E5%BC%8F&spm=1018.2226.3001.4187

class MyWindown(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(800, 500)
        self.setWindowTitle("Button")
        mlayout = QHBoxLayout()
        op_area = QVBoxLayout()
        show_area = QVBoxLayout()

        # ---------------------------------------
        ltwdg = QListWidget()
        # ltwdg.setFixedSize(150, 380)
        ltwdg.insertItems(0, ["QVBoxLayout", "QHBoxLayout", "QGridLayout", "QFormLayout", "StackedLayout"])

        # ------------------------------------------
        #wdiget prepared for stacked widget
        self.vbwdg = QWidget()  #button overview
        self.hbwdg = QWidget()  #push button
        self.gdwdg = QWidget()  #tool button
        self.fmwdg = QWidget()  #radio button

        # ------------------------------------------
        self.vb()
        self.hb()
        self.gd()
        self.fm()

        # ---------------------------------------------
        # self.stkwdg = QStackedLayout()   #注意不是 stackedLayout
        stkwdg = QStackedWidget()
        stkwdg.addWidget(self.vbwdg)
        stkwdg.addWidget(self.hbwdg)
        stkwdg.addWidget(self.gdwdg)
        stkwdg.addWidget(self.fmwdg)

        # self.stkwdg.setCurrentIndex(1)

        ltwdg.currentRowChanged.connect(lambda i: stkwdg.setCurrentIndex(i))
        # ---------------------------------------------
        op_area.addWidget(ltwdg)   #put the list in the left op_area
        op_area.addStretch()
        show_area.addWidget(stkwdg)   #put the stacked in the right show_area
        show_area.addStretch()

        mlayout.addLayout(op_area)
        mlayout.addLayout(show_area)
        mlayout.addStretch()
        self.setLayout(mlayout)

        # ---------------------------------------------
    def vb(self):
        mlyt = QVBoxLayout()
        mlyt.addWidget(QPushButton("语文"))
        mlyt.addWidget(QPushButton("数学"))
        mlyt.addWidget(QPushButton("英语"))
        self.vbwdg.setLayout(mlyt)
    def hb(self):
        mlyt = QHBoxLayout()
        mlyt.addWidget(QPushButton("语文"))
        mlyt.addWidget(QPushButton("数学"))
        mlyt.addWidget(QPushButton("英语"))
        self.hbwdg.setLayout(mlyt)
    def gd(self):
        mlyt = QGridLayout()
        mlyt.addWidget(QPushButton("咖啡"), 0, 0, 1, 1)
        mlyt.addWidget(QPushButton("豆浆"), 0, 1, 1, 1)
        mlyt.addWidget(QPushButton("油条"), 0, 2, 1, 1)
        mlyt.addWidget(QPushButton("烧卖"), 1, 0, 1, 1)
        mlyt.addWidget(QPushButton("可颂"), 1, 1, 1, 1)
        mlyt.addWidget(QPushButton("豆腐脑"), 1, 2, 1, 1)

        self.gdwdg.setLayout(mlyt)
    def fm(self):
        mlyt = QFormLayout()
        mlyt.setLabelAlignment(Qt.AlignRight)    #标签靠右对齐

        nameedit = QLineEdit()
        nameedit.setAlignment(Qt.AlignRight)
        sexedit = QLineEdit()
        phoneedit = QLineEdit()
        addressedit = QLineEdit()

        mlyt.addRow("Name:", nameedit)
        mlyt.addRow("Sex:", sexedit)
        mlyt.addRow("Phone:", phoneedit)
        mlyt.addRow("Address:", addressedit)

        self.fmwdg.setLayout(mlyt)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindown()
    w.show()

    app.exec()
