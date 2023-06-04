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
        ltwdg.insertItems(0, ["ButtonOverview", "PushButton", "ToolButton", "RadioButton", "CheckBox", "CommandLinkButton", "DialogButtonBox"])
        ltwdg.currentRowChanged.connect(self.rowchanged)

        # ------------------------------------------
        #wdiget prepared for stacked widget
        self.bovwdg = QWidget()  #button overview
        self.phbwdg = QWidget()  #push button
        self.tlbwdg = QWidget()  #tool button
        self.rdbwdg = QWidget()  #radio button
        self.chbwdg = QWidget()  #check box
        self.clbwdg = QWidget()  #command link button
        self.dlbwdg = QWidget()  #dialog button
        # ------------------------------------------
        self.bov()
        self.phb()
        self.tlb()
        self.rdb()
        self.chb()
        self.clb()
        self.dlb()

        # ---------------------------------------------
        # self.stkwdg = QStackedLayout()   #注意不是 stackedLayout
        self.stkwdg = QStackedWidget()
        self.stkwdg.addWidget(self.bovwdg)
        self.stkwdg.addWidget(self.phbwdg)
        self.stkwdg.addWidget(self.tlbwdg)
        self.stkwdg.addWidget(self.rdbwdg)
        self.stkwdg.addWidget(self.chbwdg)
        self.stkwdg.addWidget(self.clbwdg)
        self.stkwdg.addWidget(self.dlbwdg)

        self.stkwdg.setCurrentIndex(1)

        # ---------------------------------------------
        op_area.addWidget(ltwdg)   #put the list in the left op_area
        op_area.addStretch()
        show_area.addWidget(self.stkwdg)   #put the stacked in the right show_area
        show_area.addStretch()

        mlayout.addLayout(op_area)
        mlayout.addLayout(show_area)
        mlayout.addStretch()
        self.setLayout(mlayout)

        # ---------------------------------------------

    def rowchanged(self, i):
        self.stkwdg.setCurrentIndex(i)

    def bov(self):    #button overview
        grdlyt = QGridLayout()
        grdlyt.addWidget(QPushButton("PushButton"), 0, 0, 1, 1)
        grdlyt.addWidget(QToolButton(), 0, 1, 1, 1)
        grdlyt.addWidget(QRadioButton("Radio"), 0, 2, 1, 1)
        grdlyt.addWidget(QCheckBox("CheckBox"), 1, 0, 1, 1)
        grdlyt.addWidget(QCommandLinkButton("cmdLkButton"), 1, 1, 1, 1)
        # grdlyt.addWidget(QDialogButtonBox("DialogBox"), 1, 2, 1, 1)

        # grdlyt.setSpacing(50)
        grdlyt.setHorizontalSpacing(100)  #设置列间距
        grdlyt.setVerticalSpacing(50)     #设置行间距
        grdlyt.setRowStretch(grdlyt.rowCount(), 5)
        grdlyt.setColumnStretch(grdlyt.columnCount(), 10)
        self.bovwdg.setLayout(grdlyt)

    def phb(self):
        mlyt = QVBoxLayout()
        hb = QGridLayout()
        showlyt = QVBoxLayout()

        self.lnedit = QTextEdit()
        self.lnedit.setStyleSheet("font-size:40px;color:green;border: 1px solid gray;")
        # self.lnedit.setFixedSize(650, 500)
        showlyt.addWidget(self.lnedit)

        baidu = QPushButton()
        baidu.setText("ButtonToBaidu")
        baidu.setIcon(QIcon(r"C:\Sensirion\icons\NO2.svg"))
        baidu.setFixedSize(180, 30)
        baidu.setShortcut("Alt+Q")   #设置快捷键
        # baidu.move(200, 100)
        baidu.clicked.connect(lambda: webbrowser.open_new_tab("https://www.baidu.com/"))
        # -------------------------------------------------------------------

        MenuBtn = QPushButton("MenuButton")
        self.menuset(MenuBtn)
        MenuBtn.setFixedSize(180, 30)
        MenuBtn.pressed.connect(self.MenuBtninfo)
        # -------------------------------------------------------------------

        shortcutBtn = QPushButton('Short&Cut')  #方法一, 初始化时不显示, 按一下 'Alt+C'后, C下面就显示下划线
        # shortcutBtn.setText("Short&Cut")     #方法二
        # shortcutBtn.setShortcut("Alt+C")     #方法三
        shortcutBtn.setFixedSize(180, 30)
        shortcutBtn.clicked.connect(self.shortcutBtninfo)
        # -------------------------------------------------------------------

        iconbtn = QPushButton("Icon")
        iconbtn.setIcon(QIcon(r"C:\Sensirion\icons\NO2.svg"))   #方法一
        # iconbtn = QPushButton(QIcon(r"C:\Sensirion\icons\NO2.svg"), "Icon")  #方法二: 创建按钮的同时添加icon
        iconbtn.setFixedSize(180, 30)
        iconbtn.clicked.connect(self.iconbtninfo)
        # -------------------------------------------------------------------
        defaultbtn = QPushButton("Default")
        defaultbtn.setFixedSize(180, 30)
        defaultbtn.setDefault(True)
        defaultbtn.clicked.connect(self.defaultbtninfo)
        # -------------------------------------------------------------------
        autodefaultbtn = QPushButton("AutoDefault")
        autodefaultbtn.setFixedSize(180, 30)
        autodefaultbtn.setAutoDefault(True)
        autodefaultbtn.clicked.connect(self.autodefaultbtninfo)
        # -------------------------------------------------------------------
        sgnlbtn = QPushButton("Signal")
        sgnlbtn.setFixedSize(180, 30)
        sgnlbtn.pressed.connect(self.sgnlbtninfo)
        # -------------------------------------------------------------------
        stysetbtn = QPushButton("StyleSet")
        stysetbtn.setFixedSize(180, 30)
        # 方法一:使用CSS方式
        # stysetbtn.setStyleSheet("QPushButton{color:black}"        #字体颜色
        #                         "QPushButton:hover{color:red}"    #鼠标在上面划过时字体颜色
        #                         "QPushButton{background-color:rgb(78,255,255)}"    #背景色
        #                         "QPushButton{border:10px}"            #边框宽度
        #                         "QPushButton{border-radius:10px}"     #边框圆角
        #                         "QPushButton{padding:2px 4px}"        #边距
        #                         "QPushButton{font-size:16px}"         #字体大小
        #                         )
        # 方法二: PyQt5 自带的函数进行设置
        # 字体配置:
        font = QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(12)
        font.setWeight(20)

        stysetbtn.setFont(font)
        stysetbtn.setFlat(True)   #设置透明背景
        stysetbtn.clicked.connect(self.stysetbtninfo)

        # -------------------------------------------------------------------

        hb.addWidget(baidu, 0, 0, 1, 1)
        hb.addWidget(MenuBtn, 0, 1, 1, 1)
        hb.addWidget(shortcutBtn, 0, 2, 1, 1)
        hb.addWidget(iconbtn, 1, 0, 1, 1)
        hb.addWidget(defaultbtn, 1, 1, 1, 1)
        hb.addWidget(autodefaultbtn, 1, 2, 1, 1)
        hb.addWidget(sgnlbtn, 2, 0, 1, 1)
        hb.addWidget(stysetbtn, 2, 1, 1, 1)

        hb.setHorizontalSpacing(20)
        hb.setVerticalSpacing(20)
        hb.setRowStretch(hb.rowCount(), 10)
        hb.setColumnStretch(hb.columnCount(), 10)

        mlyt.addLayout(hb)
        mlyt.addLayout(showlyt)
        mlyt.addStretch()
        self.phbwdg.setLayout(mlyt)

    def tlb(self):
        mlyt = QVBoxLayout()
        hb = QGridLayout()
        showlyt = QVBoxLayout()
        self.tlbedit = QTextEdit()
        self.tlbedit.setStyleSheet("font-size:16px;color:green;border: 1px solid gray;")
        showlyt.addWidget(self.tlbedit)

        # ---------------------------------------------
        tlb_icon = QToolButton()
        tlb_icon.setFixedSize(180, 30)
        tlb_icon.setIcon(QIcon(r"C:\Sensirion\icons\Water Quality Sensors.svg"))
        tlb_icon.setText("IconToolButton")
        tlb_icon.setToolTip("This is a tool button.")
        # tlb_icon.setToolButtonStyle(Qt.ToolButtonTextOnly)
        tlb_icon.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        tlb_icon.clicked.connect(self.tlb_iconinfo)

        # ---------------------------------------------
        tlb_arrow = QToolButton()
        tlb_arrow.setFixedSize(180, 30)
        tlb_arrow.setArrowType(Qt.UpArrow)
        tlb_arrow.setAutoRaise(True)
        tlb_arrow.clicked.connect(self.tlb_arrowinfo)
        # ---------------------------------------------
        tlb_menu = QToolButton(self)
        self.tlbmenuset(tlb_menu)
        tlb_menu.clicked.connect(self.tlb_menuinfo)

        # ---------------------------------------------
        hb.addWidget(tlb_icon, 0, 0, 1, 1,)
        hb.addWidget(tlb_arrow, 0, 1, 1, 1,)
        hb.addWidget(tlb_menu, 0, 2, 1, 1,)


        mlyt.addLayout(hb)
        mlyt.addLayout(showlyt)
        mlyt.addStretch()
        self.tlbwdg.setLayout(mlyt)

    def rdb(self):
        mlyt = QVBoxLayout()
        gridlyt = QGridLayout()
        lnedit = QTextEdit()
        lnedit.setStyleSheet("QTextEdit{font-size:24px}")
        lnedit.setText("QButtonGroup 待研究")

        rdbtn1 = QRadioButton()
        rdbtn1.setText("East")
        rdbtn2 = QRadioButton("West")
        rdbtn2.setStyleSheet("QRadioButton{color:black}"        #字体颜色
                                "QRadioButton:hover{color:red}"    #鼠标在上面划过时字体颜色
                                "QRadioButton{background-color:rgb(78,255,255)}"    #背景色
                                "QRadioButton{border:10px}"            #边框宽度
                                "QRadioButton{border-radius:10px}"     #边框圆角
                                "QRadioButton{padding:2px 4px}"        #边距
                                "QRadioButton{font-size:24px}"         #字体大小
                                )
        rdbtn3 = QRadioButton("South")
        rdbtn4 = QRadioButton("North")
        rdbtn4.setChecked(True)                  #设置成默认被选中

        rdbtn1.setAutoExclusive(False)   #取消按钮的排他性

        rdbtn1.toggled.connect(lambda x: lnedit.setText("setAutoExclusive(False) 取消排他性") if x else print(''))    #返回bool值, True, False
        rdbtn2.toggled.connect(lambda x: lnedit.setText("2 is Checked") if x else print(''))    #返回bool值, True, False
        rdbtn3.toggled.connect(lambda x: lnedit.setText("3 is Checked") if x else print(''))    #返回bool值, True, False
        rdbtn4.toggled.connect(lambda x: lnedit.setText("4 is Checked") if x else print(''))    #返回bool值, True, False

        gridlyt.addWidget(rdbtn1, 0, 0, 1, 1)
        gridlyt.addWidget(rdbtn2, 0, 1, 1, 1)
        gridlyt.addWidget(rdbtn3, 0, 2, 1, 1)
        gridlyt.addWidget(rdbtn4, 0, 3, 1, 1)
        # ---------------------------------------------------------------------------
        hbox = QHBoxLayout()
        rdwdg = QWidget()
        sex_gp = QButtonGroup(rdwdg)
        result_gp = QButtonGroup(rdwdg)

        btn1 = QRadioButton("Male", rdwdg)
        btn1.move(100, 100)
        btn2 = QRadioButton("Female", rdwdg)
        btn2.move(100, 200)
        btn3 = QRadioButton("Yes", rdwdg)
        btn2.move(200, 100)
        btn4 = QRadioButton("No", rdwdg)
        btn4.move(200, 200)

        sex_gp.addButton(btn1)
        sex_gp.addButton(btn2)
        result_gp.addButton(btn3)
        result_gp.addButton(btn4)

        hbox.addWidget(rdwdg)

        mlyt.addLayout(gridlyt)
        mlyt.addLayout(hbox)
        # mlyt.addWidget(btn1)
        # mlyt.addWidget(btn2)
        # mlyt.addWidget(btn3)
        # mlyt.addWidget(btn4)
        mlyt.addStretch()

        mlyt.addWidget(lnedit)
        self.rdbwdg.setLayout(mlyt)

    def chb(self):
        mylyt = QVBoxLayout()
        # gridlyt = QGridLayout()
        chlyt = QHBoxLayout()
        lnedit = QTextEdit()
        lnedit.setStyleSheet("QTextEdit{font-size:24px}")

        ch1 = QCheckBox("Coffee")
        ch2 = QCheckBox("Tea")
        ch3 = QCheckBox("MilkTea")
        ch4 = QCheckBox("BeanSource")

        ch1.clicked.connect(lambda x: lnedit.setText("Ch1 is selected") if x else lnedit.setText("ch1 is cancelled!"))

        chlyt.addWidget(ch1)
        chlyt.addWidget(ch2)
        chlyt.addWidget(ch3)
        chlyt.addWidget(ch4)

        mylyt.addLayout(chlyt)
        mylyt.addWidget(lnedit)

        self.chbwdg.setLayout(mylyt)

    def clb(self):
        mlyt = QVBoxLayout()
        lnedit = QTextEdit()

        commandlinkbtn = QCommandLinkButton()
        commandlinkbtn.setText("Quit")
        commandlinkbtn.setDescription("Inlet for quit!")

        mlyt.addWidget(commandlinkbtn)
        mlyt.addWidget(lnedit)
        self.clbwdg.setLayout(mlyt)

    def dlb(self):
        pass

    def menuset(self, MenuBtn):
        menu = QMenu("Menu", MenuBtn)

        #主菜单清单
        act1 = QAction("New", menu)
        act2 = QAction("Open", menu)
        act3 = QAction("Save", menu)
        act4 = QAction("Quit", menu)

        #添加快捷键
        act1.setShortcut("Alt+Insert")
        act3.setShortcut("Ctrl+S")

        #信号与槽
        act1.triggered.connect(lambda : print("New file"))
        act2.triggered.connect(lambda : MenuBtn.setText("Open"))
        act3.triggered.connect(lambda : print("Save file"))
        act4.triggered.connect(lambda : print("Quit"))

        #添加图标
        act1.setIcon(QIcon(r"C:\Sensirion\icons\Liquid Flow.svg"))
        act2.setIcon(QIcon(r"C:\Sensirion\icons\Liquid Flow.svg"))
        act3.setIcon(QIcon(r"C:\Sensirion\icons\Liquid Flow.svg"))
        act4.setIcon(QIcon(r"C:\Sensirion\icons\Liquid Flow.svg"))

        #创建子菜单
        me = QMenu("Recent ...", menu)
        me.setIcon(QIcon(r"C:\Sensirion\icons\Liquid Flow.svg"))

        #创建子菜单清单
        ac1 = QAction("01_QPushbutton.py", me)
        ac2 = QAction("02_QRaidobutton.py", me)
        ac3 = QAction("03_QCheckboxbutton.py", me)

        #信号与槽
        ac1.triggered.connect(lambda : print("open:"+ac1.text()))
        ac2.triggered.connect(lambda : print("open:"+ac2.text()))
        ac3.triggered.connect(lambda : print("open:"+ac3.text()))

        #子菜单添加项目
        me.addAction(ac1)
        me.addAction(ac2)
        me.addAction(ac3)

        #菜单添加项目
        menu.addAction(act1)
        menu.addAction(act2)
        menu.addAction(act3)

        #给菜单添加分割线
        menu.addSeparator()

        #把子菜单添加到主菜单
        menu.addMenu(me)
        menu.addSeparator()
        menu.addAction(act4)

        MenuBtn.setMenu(menu)

    def MenuBtninfo(self):
        self.lnedit.setText("Menu Button was pressed")

    def shortcutBtninfo(self):
        self.lnedit.setText("ShortCut: Alt+C")

    def iconbtninfo(self):
        self.lnedit.setText("This button is with Icon.")

    def defaultbtninfo(self):
        self.lnedit.setText("setDefault as True, always show 'blue frame")

    def autodefaultbtninfo(self):
        # self.lnedit.setText()
        self.lnedit.setPlainText("setAutoDefault as True, only with 'blue frame' when selected")

    def sgnlbtninfo(self):
        self.lnedit.setText("pressed: 鼠标按下信息\nreleased: 鼠标释放信号\nclicked:单击信号,传递信号按钮释放被选中\ntoffled:选中状态切换信号（一般在单选框或者复选框中使用）")

    def stysetbtninfo(self):
        self.lnedit.setText("Demo to show style setting.")

    def tlb_iconinfo(self):   #tool button
        self.tlbedit.setText(
            '''1. In default, Text not show when icon is set.
2. Hint will show when mouse hover on the button.
3. etToolButtonStyle(): 设置tool button风格
    3.1 Qt.ToolButtonIconOnly;
    3.2 Qt.ToolButtonTextOnly;
    3.3 Qt.ToolButtonTextBesideIcon;
    3.4 Qt.ToolButtonTextUnderIcon;
    3.5 Qt. ToolButtonFollowStyle;
                                ''')

    def tlb_arrowinfo(self):
        self.tlbedit.setText("setAutoRaise(True),没发现有什么区别")

    def tlbmenuset(self, tlb_menu) -> None:
        tlb_menu.setFixedSize(180, 30)
        tlb_menu.setText("Menu")

        menu = QMenu(tlb_menu)
        act1 = QAction("New")
        act2 = QAction("Open")
        menu.addAction(act1)
        menu.addAction(act2)
        menu.addSeparator()
        tlb_menu.setMenu(menu)
        tlb_menu.setAutoRaise(True)
        tlb_menu.setPopupMode(QToolButton.MenuButtonPopup)
        # sub_menu = QMenu(menu)  #创建子菜单
        # sub_menu.setTitle("sub_menu")
        # sub_menu.setIcon(QIcon(r"C:\Sensirion\icons\Water Quality Sensors.svg"))
        # menu.addMenu(sub_menu)  #再菜单中添加子菜单
        #
        # action = QAction(QIcon(r"C:\Sensirion\icons\Water Quality Sensors.svg"), "open", menu)
        # action.triggered.connect(lambda : print("open"))
        # menu.addAction(action)
        #
        # tlb_menu.setMenu(menu)

    def tlb_menuinfo(self):
        self.tlbedit.setText("不显示下拉菜单??  ToDo")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindown()
    w.show()

    app.exec()
