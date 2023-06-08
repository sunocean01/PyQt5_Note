import sys
import webbrowser

from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QStackedLayout, QSplitter, \
    QWidget, QPushButton, QLabel, QDesktopWidget, QSizePolicy, QLineEdit, QTextEdit, QListWidget, QRadioButton, \
    QStackedWidget, QToolButton, QCheckBox, QCommandLinkButton, QDialogButtonBox, QMenu, QAction, QButtonGroup, \
    QTreeWidgetItem, QTreeWidget, QTableWidgetItem, QComboBox, QAbstractItemView, QHeaderView, QTableWidget, QGroupBox, \
    QTextBrowser, QScrollArea, QToolBox, QFrame, QMdiArea, QMainWindow, QDial, QSlider
from PyQt5.QtCore import Qt
from PyQt5 import uic

# from PyQt5 import *

class MyWindown(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(800, 800)
        self.setWindowTitle("Button")
        mlayout = QHBoxLayout()
        op_area = QVBoxLayout()
        show_area = QVBoxLayout()

        # ---------------------------------------
        ltwdg = QListWidget()
        # ltwdg.setFixedSize(150, 380)
        ltwdg.insertItems(0, ["ListWidget",
                              "TreeWidget",
                              "TableWidget",
                              "QAxWidget",
                              "Spliter",
                              "Stacked",
                              "GroupBox",
                              "Frame",
                              "MDI",
                              "Dial",
                              "Dock",
                              "KeySequence",
                              "ScrollBar",
                              "Slider",
                              "ToolBox"
                              ])

        # ------------------------------------------
        #wdiget prepared for stacked widget
        self.lstwdg = QWidget()  #ListWidget
        self.trewdg = QWidget()  #ListWidget
        self.tblwdg = QWidget()  #ListWidget
        self.qaxwdg = QWidget()  #QAxWidget
        self.sptwdg = QWidget()  #spliter
        self.stkwdg = QWidget()  #Stacked
        self.grbwdg = QWidget()  #GroupBox
        self.frmwdg = QWidget()  #Frame
        self.mdiwdg = QWidget()  #MDI
        self.dilwdg = QWidget()  #Dial
        self.dckwdg = QWidget()  #Dock
        self.ksqwdg = QWidget()  #KeySequence
        self.slbwdg = QWidget()  #ScrollBar
        self.sldwdg = QWidget()  #slider
        self.tlbwdg = QWidget()  #Tool Box
        # ------------------------------------------
        self.lst()
        self.tre()
        self.tbl()
        self.qax()
        self.spt()
        self.stk()
        self.grb()
        self.frm()
        self.mdi()
        self.dil()
        self.dck()
        self.ksq()
        self.slb()
        self.sld()
        self.tlb()

        # ---------------------------------------------
        # self.stkwdg = QStackedLayout()   #注意不是 stackedLayout
        stkwdg = QStackedWidget()
        stkwdg.addWidget(self.lstwdg)
        stkwdg.addWidget(self.trewdg)
        stkwdg.addWidget(self.tblwdg)
        stkwdg.addWidget(self.qaxwdg)
        stkwdg.addWidget(self.sptwdg)
        stkwdg.addWidget(self.stkwdg)
        stkwdg.addWidget(self.grbwdg)
        stkwdg.addWidget(self.frmwdg)
        stkwdg.addWidget(self.mdiwdg)
        stkwdg.addWidget(self.dilwdg)
        stkwdg.addWidget(self.dckwdg)
        stkwdg.addWidget(self.ksqwdg)
        stkwdg.addWidget(self.slbwdg)
        stkwdg.addWidget(self.sldwdg)
        stkwdg.addWidget(self.tlbwdg)


        stkwdg.setCurrentIndex(1)
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
    # List widget
    def lst(self):
        hb = QHBoxLayout()
        Dm_lwdgt = QListWidget()
        Dm_lwdgt.insertItem(0,'Item1 in ListWidget')
        Dm_lwdgt.insertItem(1,'Item2 in ListWidget')

        hb.addWidget(Dm_lwdgt)
        self.lstwdg.setLayout(hb)
        Dm_lwdgt.currentRowChanged.connect(lambda i: print("Item {}".format(i)))

    # Tree widget
    def tre(self):
        hb = QHBoxLayout()
        Dm_trwdgt = QTreeWidget()
        Dm_trwdgt.setColumnCount(2)     #设置树结构中的列数
        Dm_trwdgt.setHeaderLabels(["Member", "Resposibility"])
        Dm_trwdgt.setColumnWidth(0, 150)  #设置列的宽度, 一列一列设置
        Dm_trwdgt.setColumnWidth(1, 280)

        root = QTreeWidgetItem()   #创建节点, 或者直接将parent传进来, QTreeWidgetItem(Dm_trwdgt)
        Dm_trwdgt.insertTopLevelItem(0, root)
        root.setText(0, "Classmembers(toop node)")
        dict = {'Leader': 'Coordinator',
                'Vice Leader': 'Support Leader',
                'Study Module': 'Study related',
                'Displine Module': 'Displine related',
                'Labor Module': 'Labor related'}
        for key, value in dict.items():
            child = QTreeWidgetItem(root)   #创建子节点
            child.setText(0, key)       #设置第一列的值
            child.setText(1, value)     #设置第二列的值
            Dm_trwdgt.setAlternatingRowColors(True)
            Dm_trwdgt.addTopLevelItem(root)         #将创建的树节点添加到树控件中

        root2 = QTreeWidgetItem()  #一行就是一个Item
        root2.setText(0, "Name")
        root2.setText(1, "Sex")

        Dm_trwdgt.insertTopLevelItem(1, root2)
        hb.addWidget(Dm_trwdgt)
        self.trewdg.setLayout(hb)

    # Table widget
    def tbl(self):
        hb = QVBoxLayout()

        #创建表格
        tablewidget = QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)
        # tablewidget = QTableWidget(4,   3)  #同上, 设置4行3列

        #设置水平方向的表头标签与垂直方向上的表头标签, 注意必须在初始化行列之后进行, 否则无效
        tablewidget.setHorizontalHeaderLabels(['Name','Sex','Weight'])  #设置column
        tablewidget.setVerticalHeaderLabels(['1','2','3','4'])      #设置index, 只能是字符串

        tablewidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #设置水平方向表格为自适应的伸缩模式
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)       #设置表格为禁止编辑
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)      #设置表格整行选中

        QTableWidget.resizeColumnsToContents(tablewidget)        #设置列宽与内容匹配
        QTableWidget.resizeRowsToContents(tablewidget)           #设置行高与内容匹配

        # tablewidget.verticalHeader().setVisible(False)      #显示/隐藏表头
        # tablewidget.horizontalHeader().setVisible(False)     #显示/隐藏索引

        # 可以在单元格内放置控件
        self.cmBox = QComboBox()
        self.cmBox.addItems(['M','F'])
        self.cmBox.addItem('NA')
        self.cmBox.setStyleSheet('QComboBox{margin:3px}')
        tablewidget.setCellWidget(0, 1, self.cmBox)
        self.cmBox.currentTextChanged.connect(lambda x: print(self.cmBox.currentText()))

        tablewidget.setItem(0, 0, QTableWidgetItem('Tom'))  #填充数据

        searchBtn = QPushButton()
        searchBtn.setText("Modify")
        searchBtn.setDown(True)
        searchBtn.setStyleSheet("QPushButton{margin:3px}")
        tablewidget.setCellWidget(0, 2, searchBtn)
        searchBtn.clicked.connect(lambda x: print("Search Button is pressed"))

        #添加数据
        newItem = QTableWidgetItem('Lily')
        tablewidget.setItem(1, 0, newItem)

        newItem = QTableWidgetItem('M')
        tablewidget.setItem(1, 1, newItem)

        newItem = QTableWidgetItem('160')
        tablewidget.setItem(1, 2, newItem)

        hb.addWidget(tablewidget)
        self.tblwdg.setLayout(hb)

    # QAxWidget
    def qax(self):
        # vb = QVBoxLayout()
        # QAx = QAxWidget()
        # QAx.setControl("{8856F961-340A-11D0-A96B-00C04FD705A2}")
        # QAx.dynamicCall("Navigate(const QString&)", "https://map.baidu.com/@13523265.31,3641114.64,12z")
        # vb.addWidget(QAx)
        #
        # noteedit = QTextEdit()
        # noteedit.setStyleSheet("QTextEdit{font-size:24px}")
        # noteedit.setText("https://blog.csdn.net/u012839256/article/details/107857631?ops_request_misc=&request_id=&biz_id=102&utm_term=pyqt5%20qaxwidget&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-4-107857631.142^v88^koosearch_v1,239^v2^insert_chatgpt&spm=1018.2226.3001.4187")
        # vb.addWidget(noteedit)
        # self.qaxwdg.setLayout(vb)

        pass

    def spt(self):
        layout = QVBoxLayout()
        mainSplitter = QSplitter()
        layout.addWidget(mainSplitter)

        mainSplitter.setOrientation(Qt.Horizontal)

        rightSplitter = QSplitter()

        #垂直分割
        rightSplitter.setOrientation(Qt.Vertical)
        textEdit = QTextEdit()
        textEdit.setText("Window2")
        rightSplitter.addWidget(textEdit)
        textEdit = QTextEdit()
        textEdit.setText("Window3")
        rightSplitter.addWidget(textEdit)

        textEdit = QTextEdit()
        textEdit.setText("Window1")

        #分割的结构和添加的顺序有关
        mainSplitter.addWidget(textEdit)
        mainSplitter.addWidget(rightSplitter)

        #分割比例
        mainSplitter.setStretchFactor(0, 1)
        mainSplitter.setStretchFactor(1, 2)
        self.sptwdg.setLayout(layout)

    def stk(self):
        pass

    def grb(self):
        groupbox1 = QGroupBox("Sex")
        grouplayout1 = QHBoxLayout()
        radio1 = QRadioButton('Female')
        radio2 = QRadioButton('Male')
        radio1.setChecked(True)
        grouplayout1.addWidget(radio1)
        grouplayout1.addWidget(radio2)
        groupbox1.setLayout(grouplayout1)

        groupbox2 = QGroupBox("NameCard")
        grouplayout2 = QFormLayout()
        nameEdit = QLineEdit()
        address = QLineEdit()
        grouplayout2.addRow("Name:", nameEdit)
        grouplayout2.addRow("Address:", address)
        groupbox2.setLayout(grouplayout2)

        mlayout = QVBoxLayout()
        mlayout.addWidget(groupbox1)
        mlayout.addWidget(groupbox2)
        mlayout.addStretch()
        self.grbwdg.setLayout(mlayout)

    def frm(self):
        pass
    def mdi(self):
        pass
    def dil(self):
        pass
    def dck(self):
        pass
    def ksq(self):
        pass
    def slb(self):
        scrolla = QScrollArea(self)
        disp_img = QLabel()
        pixmap = QPixmap(r"..\testdata\PmSetUp.jpg")
        disp_img.setPixmap(pixmap)
        scrolla.setWidget(disp_img)

        textbrowser = QTextBrowser()
        textbrowser.setFixedSize(800, 1000)
        textbrowser.setStyleSheet("QLabel{background:white;}")
        textbrowser.setText("<h1>Hello World!</h1>")     # 设置编辑框初始化时显示的文本
        textbrowser.setReadOnly(True)                    # 设置编辑框是否为只读
        sla = QScrollArea(self)
        sla.setWidget(textbrowser)

        mlayout = QVBoxLayout()
        mlayout.addWidget(scrolla)
        mlayout.addWidget(sla)
        self.slbwdg.setLayout(mlayout)

    def sld(self):
        pass

    def tlb(self):
        # self.names = ['长跑', '斯诺克', '棒球']
        gamers = {'长跑':['赵四', '钱二'],
                  '斯诺克':['张三', '李四'],
                  '棒球':['王五', '郑六']
                  }

        toolBox = QToolBox()
        for categ in gamers:
            toolBox.addItem(self.tboxset(categ, gamers), categ)

        toolBox.currentChanged.connect(lambda : toolBox.currentIndex())

        mlayout = QVBoxLayout()
        mlayout.addWidget(toolBox)
        self.tlbwdg.setLayout(mlayout)

    def frm(self):
        mlayout = QVBoxLayout()

        sbly = QHBoxLayout()
        sbly.addWidget(QPushButton("name:"))
        sbly.addWidget(QLineEdit())
        sbly.addStretch()

        frm1 = QFrame()
        frm1.setFrameShape(QFrame.Box)      #设置Frame形状
        frm1.setLineWidth(5)
        frm1.setLayout(sbly)

        frm2 = QFrame()
        frm2.setFrameShape(QFrame.HLine)
        frm2.setLineWidth(3)

        frm3 = QFrame()
        frm3.setFrameShape(QFrame.Panel)
        frm3.setFrameShadow(QFrame.Raised)
        frm3.setLineWidth(3)

        mlayout.addWidget(frm1)
        mlayout.addWidget(frm2)
        mlayout.addWidget(frm3)

        self.frmwdg.setLayout(mlayout)

    def mdi(self):
        # mlayout = QVBoxLayout()
        # mywdge = QWidget()
        # self.mdi = QMdiArea()       #实例化QMidArea
        #
        # # 实例化菜单栏
        # bar = QMainWindow.menuBar()
        # file = bar.addMenu('File')
        # # 添加子菜单
        # file.addAction('New')
        # file.addAction('Cascade')
        # file.addAction('Quit')
        #
        # # 点击QAction绑定自定义的槽函数
        # file.triggered[QAction].connect(self.windowaction)
        #
        # mlayout.addWidget(self.mdi)
        # self.mdiwdg.setLayout(mlayout)
        pass

    def dil(self):
        mlayout = QVBoxLayout()
        dial = QDial()
        dial.setRange(0, 100)
        dial.setNotchesVisible(True)           #设置刻度
        # self.dial.setWrapping(True)                 # 刻度不留缺口
        dial.setNotchTarget(20)                #设置刻度密度
        dial.setFixedSize(200, 200)

        labvalue = QLabel('0', self)
        labvalue.setFont(QFont('Arial Black', 24))
        dial.valueChanged.connect(lambda i: labvalue.setText(str(dial.value())))

        mlayout.addWidget(dial)
        mlayout.addWidget(labvalue)

        self.dilwdg.setLayout(mlayout)

    def sld(self):
        mlayout = QVBoxLayout()
        # ------------------------------------------------------------------------
        lab = QLabel("我爱你,中国!")
        lab.setAlignment(Qt.AlignCenter)

        # ------------------------------------------------------------------------
        # 水平方向:
        s1 = QSlider(Qt.Horizontal)
        print(s1.orientation())
        s1.setOrientation(1)  # 设置方向, 是水平还是竖直

        # 设置最小最大值及step,当前值
        s1.setMinimum(10)
        s1.setMaximum(50)
        s1.setInvertedAppearance(True)
        s1.setPageStep(15)
        s1.setSingleStep(3)
        s1.setValue(20)

        # 刻度位置,刻度在下方
        s1.setTickPosition(QSlider.TicksBelow)

        # 设置刻度的间隔
        s1.setTickInterval(5)

        # ------------------------------------------------------------------------
        mlayout.addWidget(lab)
        mlayout.addWidget(s1)

        def slot_value_change():
            print('Current slider value = {}'.format(s1.value()))
            size = s1.value()
            lab.setFont(QFont('Arial', size))
            print(s1.sliderPosition())
            print(s1.value())
            if size == 50:
                s1.setMaximum(100)

        s1.valueChanged.connect(slot_value_change)
        # s1.sliderMoved.connect(slot_slider_move)
        s1.rangeChanged.connect(slot_value_change)
        # self.s1.sliderMoved.connect(s1.slot_silder_move)

        # ------------------------------------------------------------------------
        self.sldwdg.setLayout(mlayout)

    # for mdi:
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

    #for toolbox
    def tboxset(self, categ, gamers):
        grpBox = QGroupBox()
        layout = QHBoxLayout()
        for nm in gamers[categ]:
            gamer = QToolButton()
            gamer.setText(nm)
            # gamer.setIcon(QIcon(category['pic']))
            # gamer.setIconSize(QSize(128, 128))
            gamer.setAutoRaise(True)
            # gamer.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            layout.addWidget(gamer)

        grpBox.setLayout(layout)
        return grpBox

    #for toolbox
    def tboxchanged(self):
        info = '您正在查看{}项目.'.format(self.toolBox.currentIndex())
        print(info)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindown()
    w.show()

    app.exec()
