import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindown(QMainWindow):
    count = 0
    def __init__(self, parent=None):
        super(MyWindown, self).__init__(parent)

        self.mdi = QMdiArea()       #实例化QMidArea
        # self.setCentralWidget(self.mdi)     #设置为中间控件

        # 实例化菜单栏
        bar = self.menuBar()
        file = bar.addMenu('File')
        # 添加子菜单
        file.addAction('New')
        file.addAction('Cascade')
        file.addAction('Quit')

        # 点击QAction绑定自定义的槽函数
        file.triggered[QAction].connect(self.windowaction)

    def windowaction(self, q):
        print('Triggered')
        if q.text() == 'New':
            #子窗口增加一个
            MyWindown.count = MyWindown.count + 1

            #实例化多文档界面对象
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("subwindow"+str(MyWindown.count))

            #将子窗口添加到Mdi区域
            self.mdi.addSubWindow(sub)

            sub.show()

        elif q.text() == 'Cascade':
            #cascadesubwindows(): 安排子窗口在Mdi区域级联显示
            self.mdi.cascadeSubWindows()
        elif q.text() == 'Tile':
            self.mdi.tileSubWindows()  #安排子窗口在Mdi区域平铺显示
        else:
            pass




if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindown()
    w.show()

    app.exec()