import sys
import webbrowser
from datetime import time

from PyQt5.QtGui import QIcon, QPixmap, QFont, QIntValidator
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QStackedLayout, QSplitter, \
    QWidget, QPushButton, QLabel, QDesktopWidget, QSizePolicy, QLineEdit, QTextEdit, QListWidget, QRadioButton, \
    QStackedWidget, QToolButton, QCheckBox, QCommandLinkButton, QDialogButtonBox, QMenu, QAction, QButtonGroup, \
    QComboBox, QFontComboBox, QPlainTextEdit, QSpinBox, QDoubleSpinBox, QGroupBox, QTimeEdit, QDateEdit
from PyQt5.QtCore import Qt, QTime, QDate
from PyQt5 import uic


# from PyQt5 import *

# https://blog.csdn.net/weixin_50296259/article/details/130539311?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168515292116800180683050%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=168515292116800180683050&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-4-130539311-null-null.142^v88^control_2,239^v2^insert_chatgpt&utm_term=pyqt5%20qpushbutton%E6%A0%B7%E5%BC%8F&spm=1018.2226.3001.4187

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
        ltwdg.insertItems(0, ["ComboBox",
                              "FontComboBox",
                              "LineEdit",
                              "TextEdit",
                              "PlainTextEdit",
                              "SpinBox",
                              "DoubleSpinBox",
                              "TimeEdit",
                              "DateEdit",
                              "Date/TimeEidt",
                              "Dial",
                              "Horizontal/Vertical Scroll Bar",
                              "Slider",
                              "Splitter",
                              "StackedWidget",
                              "KeySequenceEdit"
                              ])

        # ------------------------------------------
        #wdiget prepared for stacked widget
        self.cbbwdg = QWidget()  #combo box
        self.fcbwdg = QWidget()  #font combo box
        self.ldtwdg = QWidget()  #Line Edit
        self.tdtwdg = QWidget()  #TextEdit
        self.ptdwdg = QWidget()  #PlainTextEdit
        self.spbwdg = QWidget()  #Spin Box
        self.dspwdg = QWidget()  #Double Spin Box
        self.tmewdg = QWidget()  #Time Edit
        self.dedwdg = QWidget()  #date Edit
        self.dtewdg = QWidget()  #Date Time Edit
        self.dalwdg = QWidget()  #Dial
        self.hvbwdg = QWidget()  #Horizontal/Vertical Scroll Bar
        self.splwdg = QWidget()  #Splitter
        self.stkwdg = QWidget()  #StackedWidget
        self.ksewdg = QWidget()  #Key Sequence Edit

        # ------------------------------------------
        self.cbb()
        self.fcb()
        self.ldt()
        self.tdt()
        self.ptd()
        self.spb()
        self.dsp()
        self.tme()
        self.ded()
        self.dte()
        self.dal()
        self.hvb()
        self.spl()
        self.stk()
        self.kse()

        # ---------------------------------------------
        # self.stkwdg = QStackedLayout()   #注意不是 stackedLayout
        stkwdg = QStackedWidget()
        stkwdg.addWidget(self.cbbwdg)
        stkwdg.addWidget(self.fcbwdg)
        stkwdg.addWidget(self.ldtwdg)
        stkwdg.addWidget(self.tdtwdg)
        stkwdg.addWidget(self.ptdwdg)
        stkwdg.addWidget(self.spbwdg)
        stkwdg.addWidget(self.dspwdg)
        stkwdg.addWidget(self.tmewdg)
        stkwdg.addWidget(self.dedwdg)
        stkwdg.addWidget(self.dtewdg)
        stkwdg.addWidget(self.dalwdg)
        stkwdg.addWidget(self.hvbwdg)
        stkwdg.addWidget(self.splwdg)
        stkwdg.addWidget(self.stkwdg)

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
    #Combo Box
    def cbb(self):
        mlayout = QVBoxLayout()
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        # ----------------------------------------------------------------------
        lab = QLabel('Language:')  # 创建个标签默认空白
        lab.setFixedSize(200, 120)
        lab.setStyleSheet("QLabel{background:white;}"
                          r"QLabel{color:rgb(100,100,100,250);font-size:25px;font-weight:bold;font-family:Arial;}"
                          "QLabel:hover{color:rgb(100,100,100,120);}")
        self.cb = QComboBox()

        # 单个添加条目
        self.cb.addItem('c')
        self.cb.addItem('C++')
        self.cb.addItem('Python')

        # 多个添加条目
        self.cb.addItems(['Java', 'c#', 'PHP'])

        self.cb.setFixedSize(300, 120)
        self.cb.setStyleSheet(
            "QComboBox{color:rgb(100,100,100,250);font-size:25px;font-weight:bold;font-family:Arial;}")

        # 当下拉索引发生改变时发出信号触发绑定的事件
        self.cb.currentIndexChanged.connect(self.selectionchange)

        h_layout.addWidget(lab)
        h_layout.addWidget(self.cb)
        # ----------------------------------------------------------------------
        self.labshow = QLabel('Test')
        v_layout.addWidget(self.labshow)

        # ----------------------------------------------------------------------
        mlayout.addLayout(h_layout)
        mlayout.addLayout(v_layout)

        mlayout.addStretch()
        self.cbbwdg.setLayout(mlayout)

    #FontComboBox
    def fcb(self):
        mlayout = QVBoxLayout(self)
        # ----------------------------------------------------------------------
        self.label_text = QLabel("PyQt5: QFontComboBox text", self)
        # self.label_text.setFont(QFont(self.font().family(), 16))
        # ----------------------------------------------------------------------

        self.filterCmb = QComboBox(self)
        self.filterCmb.addItems(['All', 'Scalable', 'Non-Scalable', 'Equal-Width', 'Equal-Ratio'])
        self.filterCmb.currentIndexChanged.connect(self.onFontFilterChanged)

        # ----------------------------------------------------------------------
        self.fontCmb = QFontComboBox(self)  ##自动包含系统安装的所有字体
        self.fontCmb.currentFontChanged.connect(self.onFontChanged)
        self.fontCmb.setCurrentFont(self.font())

        # ------------------------------------------------------------------------
        mlayout.addSpacing(10)
        mlayout.addWidget(self.label_text)
        mlayout.addSpacing(20)
        mlayout.addWidget(QLabel("Filter"))
        mlayout.addWidget(self.filterCmb)
        mlayout.addSpacing(20)
        mlayout.addWidget(QLabel('Selection'))
        mlayout.addWidget(self.fontCmb)
        mlayout.addStretch()
        self.fcbwdg.setLayout(mlayout)

    #Line Edit
    def ldt(self):
        mlayout = QVBoxLayout()
        hlayout1 = QHBoxLayout()
        hlayout2 = QVBoxLayout()
        # ----------------------------------------------------------------------
        lb = QLabel("LineEdit:")
        lb.setStyleSheet("QLabel{background:white;}"
                         r"QLabel{color:rgb(100,100,100,250);font-size:25px;font-weight:bold;font-family:Arial;}"
                         "QLabel:hover{color:rgb(100,100,100,120);}")
        lb.setFixedSize(200, 80)

        # ----------------------------------------------------------------------
        lineedit = QLineEdit()
        lineedit.setFixedSize(300, 80)

        # 密码输入
        # lineedit.setEchoMode(QLineEdit.Password)        #在输入时隐藏内容
        lineedit.setEchoMode(QLineEdit.PasswordEchoOnEdit)  # 失去焦点时隐藏

        # 背景文字
        lineedit.setPlaceholderText("Input the password please!")  # 背景文字

        # ----------------------------------------------------------------------
        self.lineedit2 = QLineEdit()

        # regExp = QRegExp('^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])$')   #利用正则表达式限制输入数据的范围
        # uCharValidator = QRegExpValidator(regExp)
        # lineedit2.setValidator(uCharValidator)

        self.lineedit2.setValidator(QIntValidator(0, 10))  # 使用QIntValidator 限制输入数据的范围

        # ------------------------------------------------------------------------
        btn = QPushButton("Confrim")
        btn.clicked.connect(self.gettext)
        # ------------------------------------------------------------------------
        hlayout1.addWidget(lb)
        hlayout1.addSpacing(10)
        hlayout1.addWidget(lineedit)
        hlayout1.addSpacing(10)

        hlayout2.addWidget(self.lineedit2)
        hlayout2.addWidget(btn)

        mlayout.addLayout(hlayout1)
        mlayout.addLayout(hlayout2)
        self.ldtwdg.setLayout(mlayout)

    #Text Edit
    def tdt(self):
        mlayout = QVBoxLayout(self)
        hlayout1 = QHBoxLayout(self)
        hlayout2 = QHBoxLayout(self)
        hlayout3 = QHBoxLayout(self)
        hlayout4 = QHBoxLayout(self)
        # ----------------------------------------------------------------------
        lb = QLabel("TextEdit:")
        lb.setStyleSheet("QLabel{background:white;}"
                         r"QLabel{color:rgb(100,100,100,250);font-size:25px;font-weight:bold;font-family:Arial;}"
                         "QLabel:hover{color:rgb(100,100,100,120);}")
        lb.setFixedSize(200, 30)

        # ----------------------------------------------------------------------
        self.txtedit = QTextEdit()

        # ----------------------------------------------------------------------

        # ------------------------------------------------------------------------
        btn1 = QPushButton("ShowText")  # 显示文本
        btn1.clicked.connect(self.showText)

        btn2 = QPushButton("ShowHTML")  # 显示HTML文本
        btn2.clicked.connect(self.showHTML)

        btn3 = QPushButton("Add Text")
        btn3.clicked.connect(self.appendText)
        # ------------------------------------------------------------------------
        self.selectedshow = QLabel("Initial")
        self.selectedshowHTML = QLabel("Initial")

        # ------------------------------------------------------------------------
        hlayout1.addWidget(lb)
        hlayout1.addSpacing(10)
        hlayout1.addWidget(self.txtedit)

        hlayout2.addWidget(btn1)
        hlayout2.addSpacing(10)
        hlayout2.addWidget(btn2)
        hlayout2.addSpacing(10)
        hlayout2.addWidget(btn3)

        hlayout3.addWidget(QLabel("SelectedToText"))
        hlayout3.addWidget(self.selectedshow)

        hlayout4.addWidget(QLabel("SelectedToHTML"))
        hlayout4.addWidget(self.selectedshowHTML)

        mlayout.addLayout(hlayout1)
        mlayout.addLayout(hlayout2)
        mlayout.addSpacing(20)
        mlayout.addLayout(hlayout3)
        mlayout.addSpacing(20)
        mlayout.addLayout(hlayout4)

        mlayout.addStretch()
        self.tdtwdg.setLayout(mlayout)

    # Plain Text Edit
    def ptd(self):
        mlayout = QVBoxLayout(self)
        gridlayout = QGridLayout(self)
        # ----------------------------------------------------------------------
        self.plaintextedit = QPlainTextEdit(self)
        self.plaintextedit.setPlainText("Waiting for optimization")
        self.plaintextedit.setStyleSheet("QPlainTextEdit{font-size:24px}")
        self.plaintextedit.resize(300, 300)
        # ----------------------------------------------------------------------
        # 设置占位符
        btn1 = QPushButton("设置占位符")
        gridlayout.addWidget(btn1, 0, 0, 1, 1)
        btn1.clicked.connect(self.setholder)
        # ----------------------------------------------------------------------
        btn2 = QPushButton("只读")
        gridlayout.addWidget(btn2, 0, 1, 1, 1)
        btn2.clicked.connect(self.readonly)
        # ------------------------------------------------------------------------
        btn3 = QPushButton("格式设置")
        gridlayout.addWidget(btn3, 0, 2, 1, 1)
        btn3.clicked.connect(self.setformat)
        # ------------------------------------------------------------------------
        btn4 = QPushButton("换行模式")
        gridlayout.addWidget(btn4, 0, 3, 1, 1)
        btn4.clicked.connect(self.wrapmode)
        # ------------------------------------------------------------------------
        btn5 = QPushButton('覆盖模式')  # 类似键盘上的insert键按下了
        gridlayout.addWidget(btn5, 1, 0, 1, 1)
        btn5.clicked.connect(self.overwrite)
        # ------------------------------------------------------------------------
        btn6 = QPushButton("Tab控制")
        gridlayout.addWidget(btn6, 1, 1, 1, 1)
        btn6.clicked.connect(self.tabcontrol)
        # ------------------------------------------------------------------------
        btn7 = QPushButton("TextHandle")
        gridlayout.addWidget(btn7, 1, 2, 1, 1)
        btn7.clicked.connect(self.texthandle)
        # ------------------------------------------------------------------------
        btn8 = QPushButton("blockoperate")
        gridlayout.addWidget(btn8, 1, 3, 1, 1)
        btn8.clicked.connect(self.blockoperate)
        # ------------------------------------------------------------------------
        btn9 = QPushButton("zoom")
        gridlayout.addWidget(btn9, 2, 0, 1, 1)
        btn9.clicked.connect(self.zoom)
        # ------------------------------------------------------------------------
        btn10 = QPushButton("scroll")
        gridlayout.addWidget(btn10, 2, 1, 1, 1)
        btn10.clicked.connect(self.scroll)
        # ------------------------------------------------------------------------
        mlayout.addWidget(self.plaintextedit)
        mlayout.addLayout(gridlayout)
        mlayout.addStretch()
        self.ptdwdg.setLayout(mlayout)

    def spb(self):
        mlayout = QVBoxLayout()
        spinBoxesGroup = QGroupBox("Spinboxes")

        # ----------------------------------------------------------------------
        integerLabel = QLabel("Input a value between {} and {}:".format(-20, 20))
        integerSpinBox = QSpinBox()
        integerSpinBox.setRange(-20, 20)
        integerSpinBox.setSingleStep(1)
        integerSpinBox.setValue(0)
        # ----------------------------------------------------------------------
        zoomLabel = QLabel("Input a zoom value between {} and {}:".format(0, 1000))
        zoomSpinBox = QSpinBox()
        zoomSpinBox.setRange(0, 1000)
        zoomSpinBox.setSingleStep(10)
        zoomSpinBox.setSuffix('%')  # 后缀
        zoomSpinBox.setSpecialValueText("Automatic")
        zoomSpinBox.setValue(100)  # 默认值

        # ----------------------------------------------------------------------
        priceLabel = QLabel("Input a price between {} ~ {}:".format(0, 999))
        priceSpinBox = QSpinBox()
        priceSpinBox.setRange(0, 999)
        priceSpinBox.setSingleStep(1)
        priceSpinBox.setPrefix("￥")
        priceSpinBox.setValue(99)

        # ------------------------------------------------------------------------
        mlayout.addWidget(integerLabel)
        mlayout.addWidget(integerSpinBox)
        mlayout.addWidget(zoomLabel)
        mlayout.addWidget(zoomSpinBox)
        mlayout.addWidget(priceLabel)
        mlayout.addWidget(priceSpinBox)
        mlayout.addStretch()
        self.spbwdg.setLayout(mlayout)

    # Spin Box
    def dsp(self):
        mlayout = QVBoxLayout()

        # ----------------------------------------------------------------------
        precisionLabel = QLabel("Number of dcimal places to show:")
        precisionSpinBox = QSpinBox()
        precisionSpinBox.setRange(0, 100)
        precisionSpinBox.setValue(2)
        # ----------------------------------------------------------------------
        doubleLabel = QLabel("Enter a value between -20 and 20:")
        self.doubleSpinBox = QDoubleSpinBox()
        self.doubleSpinBox.setRange(-20.0, 20.0)
        self.doubleSpinBox.setSingleStep(1.0)
        self.doubleSpinBox.setValue(0.0)

        # ----------------------------------------------------------------------
        scaleLabel = QLabel("Enter a scale factor between 0 and 1000:")
        self.scaleSpinBox = QDoubleSpinBox()
        self.scaleSpinBox.setRange(0.0, 1000.0)
        self.scaleSpinBox.setSingleStep(10.0)
        self.scaleSpinBox.setSuffix('%')
        self.scaleSpinBox.setSpecialValueText("No scaling")
        self.scaleSpinBox.setValue(100.0)
        # ------------------------------------------------------------------------
        priceLabel = QLabel("Enter a price between 0 and 100:")
        self.priceSpinBox = QDoubleSpinBox()
        self.priceSpinBox.setRange(0.0, 1000.0)
        self.priceSpinBox.setSingleStep(1.0)
        self.priceSpinBox.setPrefix("￥")
        self.priceSpinBox.setValue(99.99)
        # ------------------------------------------------------------------------
        precisionSpinBox.valueChanged.connect(self.changePrecision)
        # ------------------------------------------------------------------------
        mlayout.addWidget(precisionLabel)
        mlayout.addWidget(precisionSpinBox)
        mlayout.addWidget(doubleLabel)
        mlayout.addWidget(self.doubleSpinBox)
        mlayout.addWidget(scaleLabel)
        mlayout.addWidget(self.scaleSpinBox)
        mlayout.addWidget(priceLabel)
        mlayout.addWidget(self.priceSpinBox)
        mlayout.addStretch()
        self.dspwdg.setLayout(mlayout)

    # Double Spin Box

    def tme(self):
        mlayout = QVBoxLayout()
        # ----------------------------------------------------------------------
        timeEdit = QTimeEdit(self)
        timeEdit.setDisplayFormat('HH:mm:ss')
        timeEdit.setTime(QTime.currentTime())
        # ----------------------------------------------------------------------
        self.plainTextEdit = QPlainTextEdit(self)
        self.plainTextEdit.setReadOnly(True)
        timeEdit.timeChanged.connect(lambda time: self.plainTextEdit.appendPlainText(time.toString('hh:mm:ss')))

        # ----------------------------------------------------------------------
        mlayout.addWidget(timeEdit)
        mlayout.addWidget(self.plainTextEdit)
        # ------------------------------------------------------------------------
        # mainFrame = QWidget()
        # mainFrame.setLayout(mlayout)
        # self.setCentralWidget(mainFrame)
        self.tmewdg.setLayout(mlayout)

    # date time edit
    def ded(self):
        mlayout = QVBoxLayout()
        # ----------------------------------------------------------------------
        dateEdit = QDateEdit()
        dateEdit.setStyleSheet("QDateEdit{font-size:24px}")
        dateEdit.setDisplayFormat('yyyy-MM-dd')
        dateEdit.setDate(QDate.currentDate())
        # ----------------------------------------------------------------------
        plainTextEdit = QPlainTextEdit()
        plainTextEdit.setStyleSheet("QPlainTextEdit{font-size:24px}")
        plainTextEdit.setReadOnly(True)
        dateEdit.dateChanged.connect(lambda date: plainTextEdit.appendPlainText(date.toString('yyyy-MM-dd')))

        # ----------------------------------------------------------------------
        mlayout.addWidget(dateEdit)
        mlayout.addWidget(plainTextEdit)
        self.dedwdg.setLayout(mlayout)

    def dte(self):
        mlayout = QVBoxLayout()
        noteedit = QTextEdit()
        noteedit.setStyleSheet("QTextEdit{font-size:24px}")
        noteedit.setText("To Do")

        mlayout.addWidget(noteedit)
        self.dtewdg.setLayout(mlayout)

    def dal(self):
        pass
    def hvb(self):
        pass
    def spl(self):
        pass
    def stk(self):
        pass
    def kse(self):
        pass

    # Combo Box
    def selectionchange(self):
        #标签用来显示选中的文本
        #currentText(): 返回选中选项的文本
        self.labshow.setText(self.cb.currentText())
        print("Items in the list are:")

        #输出选项集合中每个选项的索引与对应的内容
        #count(): 返回选项集合中的数目
        for count in range(self.cb.count()):
            print('Item '+str(count) + '=' + self.cb.itemText(count))
            print('current index', count, 'selection changed', self.cb.currentText())

    # FontComb Box
    def onFontFilterChanged(self, index):
        switcher = {
            0: QFontComboBox.AllFonts,
            1: QFontComboBox.ScalableFonts,
            2: QFontComboBox.NonScalableFonts,
            3: QFontComboBox.MonospacedFonts,
            4: QFontComboBox.ProportionalFonts
        }
        self.fontCmb.setFontFilters(switcher.get(index))

    # FontComb Box
    def onFontChanged(self, font):
        self.label_text.setFont(QFont(font.family(), 16))

    # for line Edit
    def gettext(self):
        with open(r'..\testdata\lineedit.txt','w') as fp:
            fp.write(self.lineedit2.text())
            print(self.lineedit2.text())

    #Text Edit
    def showText(self):
        self.txtedit.setPlainText(r"Hellow World again,Hellow World again,Hellow World again,Hellow World again,Hellow World again")
        self.selectedText()

    #Text Edit
    def showHTML(self):
        self.txtedit.setHtml('<font color="blue" size="5">Hello World</font>')
        self.selectedText()

    # Text QTextEdit
    def appendText(self):
        self.txtedit.append('<font color="red" size="10">Hello World</font>')
        self.txtedit.append(str(12345))            #数字必须转换成字符串
        self.selectedText()

    # Text Edit
    def selectedText(self):
        txt = self.txtedit.toPlainText()
        self.selectedshow.setText(txt)
        print("txt:",txt)

        html = self.txtedit.toHtml()
        self.selectedshowHTML.setText(html)
        print("html:", html)

    # Plain Text Edit
    def setholder(self):
        self.plaintextedit.setPlaceholderText("Input what you want here!")  # 设置占位符

    # Plain Text Edit
    def readonly(self):
        if self.plaintextedit.isReadOnly():
            self.plaintextedit.setReadOnly(False)
        else:
            self.plaintextedit.setReadOnly(True)

    # Plain Text Edit
    def setformat(self):
        textCharFormat = QTextCharFormat()   #格式设置

        #textCharFormat格式设置
        textCharFormat.setFontUnderline(True)
        textCharFormat.setUnderlineColor(QColor(20, 200, 200))

        self.plaintextedit.setCurrentCharFormat(textCharFormat)

    # Plain Text Edit
    def wrapmode(self):
        print(self.plaintextedit.lineWrapMode())   #默认是软换行, 返回 1
        self.plaintextedit.setLineWrapMode(0)      #设置成硬换行, 即敲Enter

    # Plain Text Edit
    def overwrite(self):
        print(self.plaintextedit.overwriteMode())       #默认False
        self.plaintextedit.setOverwriteMode(True)

    # Plain Text Edit
    def tabcontrol(self):
        # self.plaintextedit.setTabChangesFocus(True)       #True:焦点跳到下一个对象上
        self.plaintextedit.setTabStopDistance(10)           #设置tab的距离

    # Plain Text Edit
    def texthandle(self):
        self.plaintextedit.setPlainText("Hello World!")
        self.plaintextedit.setPlainText("Python!")
        self.plaintextedit.insertPlainText("Life is short!")   #默认在哪里插入???
        self.plaintextedit.insertPlainText("我去")
        self.plaintextedit.appendHtml("<a href = 'http:www.python.io'>I learn Python</a>")
        # 但是并不是所有的html  ，它都可以接收，它主要还是针对的是plainText
        # 例如表格它就不能接受
        # tab_str = ''' <table>\
        #         <tr><td>1</td><td>2</td><td>3</td></tr>\
        #         <tr><td>4</td><td>5</td><td>6</td></tr>\
        #         </table>'''
        # self.plainTextEdit.appendHtml(tab_str)  # 这时不支持的
        print(self.plaintextedit.toPlainText())   #获取纯文本框中所有纯文本

    # Plain Text Edit
    def blockoperate(self):
        print(self.plaintextedit.blockCount())  #当前的块个数为1, 是默认空白的

        #块是按换行符来粉的
        self.plaintextedit.setMaximumBlockCount(3)     #也就是说最多输入3行,多了上面的会被覆盖掉

    # Plain Text Edit
    def zoom(self):
        self.plaintextedit.zoomIn(20)

    # Plain Text Edit
    def scroll(self):
        # self.plaintextedit.centerCursor()      # 尽可能  保证光标所在行   在中间位置
        # self.setFocus()
        # self.plaintextedit.setCenterOnScroll(True)

        self.plaintextedit.ensureCursorVisible()        # 保证光标可见  而且是光标移动最小的距离
        self.setFocus()

    # Spin Box
    def changePrecision(self,decimals):
        self.doubleSpinBox.setDecimals(decimals)
        self.scaleSpinBox.setDecimals(decimals)
        self.priceSpinBox.setDecimals(decimals)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindown()
    w.show()

    app.exec()
