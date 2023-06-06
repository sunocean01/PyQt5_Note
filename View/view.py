import sys
import time

from PyQt5.QtGui import QIcon, QPixmap, QFont, QRegExpValidator, QIntValidator, QTextCharFormat, QColor, \
    QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QStackedLayout, QSplitter, \
    QWidget, QPushButton, QLabel, QDesktopWidget, QSizePolicy, QLineEdit, QTextEdit, QTextBrowser, QMessageBox, \
    QComboBox, QFontComboBox, QPlainTextEdit, QDial, QScrollBar, QSlider, QMainWindow, QListWidget, QDockWidget, \
    QStackedWidget, QTreeWidget, QTreeWidgetItem, QTableWidget, QHeaderView, QAbstractItemView, QTableWidgetItem, \
    QListView, QColumnView, QDirModel, QTreeView, QFileSystemModel, QTableView
from PyQt5.QtCore import Qt, QRegExp, QTime
from PyQt5 import  uic
# from PyQt5 import *

class MyWindown(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.resize(800, 800)
        self.setWindowTitle("Widget_Widget")

        mlayout = QHBoxLayout()
        listlayout = QVBoxLayout()
        self.displaylayout = QVBoxLayout()

        widgetlist = QListWidget()
        widgetlist.setFixedSize(150, 800)
        widgetlist.insertItem(0, 'List View')
        widgetlist.insertItem(1, 'Tree View')
        widgetlist.insertItem(2, 'Table View')
        widgetlist.insertItem(3, 'Column View')
        widgetlist.insertItem(4, 'Undo View')

        # listwidget.selectionMode()      #确定可以同时选择列表中的多少个项目

        listlayout.addWidget(widgetlist)
        # listlayout.addStretch()
        widgetlist.currentRowChanged.connect(self.rowchang)

        self.frltview = QWidget()
        self.frtrview = QWidget()
        self.frtbview = QWidget()
        self.frclview = QWidget()
        self.frudview = QWidget()

        self.listviewDemo()
        self.treeviewDemo()
        self.tabviewDemo()
        self.clnviewDemo()
        self.udoviewDemo()

        self.stackedwidget = QStackedWidget(self)
        # self.stackedwidget.setFixedSize(600, 720)
        self.stackedwidget.addWidget(self.frltview)
        self.stackedwidget.addWidget(self.frtrview)
        self.stackedwidget.addWidget(self.frtbview)
        self.stackedwidget.addWidget(self.frclview)
        self.stackedwidget.addWidget(self.frudview)


        self.displaylayout.addWidget(self.stackedwidget)
        # self.displaylayout.addStretch()
        mlayout.addLayout(listlayout)
        mlayout.addSpacing(2)
        mlayout.addLayout(self.displaylayout)
        mlayout.addStretch()
        self.setLayout(mlayout)

    def listviewDemo(self):
        lview = QListView()
        smodel = QStandardItemModel()
        self.sports = [
            {'img': r'C:\Python\PyQt5_Note\testdata\basketball.PNG', 'title':'basketball'},
            {'img': r'C:\Python\PyQt5_Note\testdata\football.jpg', 'title':'football'}
        ]
        for sport in self.sports:
            item = QStandardItem(QIcon(sport['img']), sport['title'])
            smodel.appendRow(item)

        lview.setModel(smodel)
        hb = QHBoxLayout()
        hb.addWidget(lview)
        self.frltview.setLayout(hb)

    def treeviewDemo(self):
        mlyt = QVBoxLayout()
        treesyslyt = QVBoxLayout()
        treecusPathlyt = QVBoxLayout()
        treecuslyt = QVBoxLayout()

        # mode = QDirModel()
        # treeview1 = QTreeView()
        # treeview1.setModel(mode)
        # treesyslyt.addWidget(treeview1)
        noteedit = QTextEdit()
        noteedit.setStyleSheet("QTextEdit{font-size:24px}")
        noteedit.setText("为了提高速度, 系统的树形结构就不显示, 如需要而已手动改.")
        treesyslyt.addWidget(noteedit)
        # -----------------------------------

        path = r"C:\Python\PyQt5_Note"
        path_mode = QFileSystemModel()
        path_mode.setRootPath(path)

        #为控件添加模式
        treeview2 = QTreeView()
        treeview2.setModel(path_mode)
        treeview2.setRootIndex(path_mode.index(path))  #只显示设置的那个文件路径
        treeview2.doubleClicked.connect(lambda Qmodelidx: print(path_mode.filePath(Qmodelidx)))  #双击文件打开
        treecusPathlyt.addWidget(treeview2)
        # --------------------------------------
        txedit = QTextEdit()
        txedit.setStyleSheet("QTextEdit{font-size:24px}")
        txedit.setText("自定义方式见QTreeWidget介绍.")
        treecuslyt.addWidget(txedit)


        mlyt.addLayout(treesyslyt)
        mlyt.addLayout(treecusPathlyt)
        mlyt.addLayout(treecuslyt)
        self.frtrview.setLayout(mlyt)

    def tabviewDemo(self):
        vb = QVBoxLayout()

        model = QStandardItemModel(0, 3)        #创建一个0行,3列的标准模型
        model.setHorizontalHeaderLabels(['Name', 'Age', 'AnnualInCome'])        #设置表头标签

        # 创建tableview组件
        tableview = QTableView()
        vb.addWidget(tableview)

        tableview.setModel(model)       #设置模型

        tableview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  #所有列自动拉伸, 充满边界
        tableview.setSelectionMode(QAbstractItemView.SingleSelection)       #设置只能选中整行
        tableview.setEditTriggers(QTableView.NoEditTriggers)  #不可编辑
        tableview.setSelectionBehavior(QAbstractItemView.SelectRows)  #设置只能选中一行
        # tableview.setSelectionMode(QAbstractItemView.ExtendedSelection)  #设置只能选中多行

        print('a')
        # 写全
        item1 = QStandardItem('小朱')
        item2 = QStandardItem('21')
        item3 = QStandardItem('14w')
        print('b')
        model.appendRow([item1, item2, item3])
        print('c')
        # 简写
        model.appendRow([
            QStandardItem('小明'),
            QStandardItem('20'),
            QStandardItem('15w'),
        ])
        print('d')

        index = tableview.currentIndex()
        model.removeRow(index.row())   #根据索引删除行
        tableview.clicked.connect(lambda x: print(x))
        self.frtbview.setLayout(vb)

    def clnviewDemo(self):
        countries = ['中国', '美国', '日本', '...']
        provinces = [['安徽', '黑龙江', '江苏', '...'],
                     ['加利福尼亚', '德克萨斯', '...'],
                     ['东京都', '北海道', '九州', '...'],
                     ['...']
                     ]
        cities = [[['合肥', '黄山', '安庆', '...'], ['哈尔滨', '大庆', '...'], ['南京', '苏州', '...'], ['...']],
                  [['洛杉矶', '...'], ['休斯顿', '...'], ['...']],
                  [['...'], ['...'], ['...'], ['...']],
                  [['...'], ['...'], ['...'], ['...']]
                  ]

        columnview = QColumnView(self)
        model = QStandardItemModel()
        countryIndex = 0
        for country in countries:
            countryItem = QStandardItem(country)
            provinceIndex = 0
            for province in provinces[countryIndex]:
                provinceItem = QStandardItem(province)
                countryItem.appendRow(provinceItem)
                for city in cities[countryIndex][provinceIndex]:
                    cityItem = QStandardItem(city)
                    provinceItem.appendRow(cityItem)
                provinceIndex += 1
            model.appendRow(countryItem)
            countryIndex += 1
        columnview.setModel(model)
        vb = QVBoxLayout()
        vb.addWidget(columnview)
        self.frclview.setLayout(vb)

    def udoviewDemo(self):
        mlyt = QVBoxLayout()
        noteedit = QTextEdit()
        noteedit.setText("To Do")
        noteedit.setStyleSheet("QTextEdit{font-size:24px}")
        mlyt.addWidget(noteedit)
        self.frudview.setLayout(mlyt)

    def rowchang(self,i):
        self.stackedwidget.setCurrentIndex(i)
        # QMessageBox.information(self, "QListView", "你选择了: " +str(i))

    def showDm_lwdgetchanged(self, j):
        print("Listwidget index changed to {}".format(j))

    def searchBtnPressed(self):
        print("Search Button was pressed!")

    def cmBoxchenged(self):
        print("cmBoxchenged:", self.cmBox.currentText())

    def cleaner(self, layout):  #清理布局  clean layout
        # 清空子布局
        item_list = list(range(layout.count()))
        item_list.reverse()  # 倒序删除，避免影响布局顺序
        for i in item_list:
            item = layout.itemAt(i)
            layout.removeItem(item)    #删除
            if item.widget():
                item.widget().deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindown()
    w.show()

    app.exec()