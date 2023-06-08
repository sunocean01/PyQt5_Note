import sys
import time

from PyQt5.QtGui import QIcon, QPixmap, QFont, QRegExpValidator, QIntValidator, QTextCharFormat, QColor, \
    QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QStackedLayout, QSplitter, \
    QWidget, QPushButton, QLabel, QDesktopWidget, QSizePolicy, QLineEdit, QTextEdit, QTextBrowser, QMessageBox, \
    QComboBox, QFontComboBox, QPlainTextEdit, QDial, QScrollBar, QSlider, QMainWindow, QListWidget, QDockWidget, \
    QStackedWidget, QTreeWidget, QTreeWidgetItem, QTableWidget, QHeaderView, QAbstractItemView, QTableWidgetItem, \
    QListView, QColumnView, QDirModel, QTreeView, QFileSystemModel, QTableView, QCalendarWidget, QFrame, QLCDNumber, \
    QProgressBar
from PyQt5.QtCore import Qt, QRegExp, QTime, QDate, QBasicTimer
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
        widgetlist.insertItems(0, ['Label', 'TextBrowser', 'Graphics', 'Calendar', 'LCD', 'ProgressBar', 'HorizontalLine'])

        widgetlist.selectionMode()      #确定可以同时选择列表中的多少个项目

        listlayout.addWidget(widgetlist)
        # listlayout.addStretch()

        self.lbwdge = QWidget()
        self.tbwdge = QWidget()
        self.ghwdge = QWidget()
        self.cdwdge = QWidget()
        self.ldwdge = QWidget()
        self.pgwdge = QWidget()
        self.hlwdge = QWidget()

        self.lb()
        self.tb()
        self.gh()
        self.cd()
        self.ld()
        self.pg()
        self.hl()

        stackedwidget = QStackedWidget(self)
        # self.stackedwidget.setFixedSize(600, 720)
        stackedwidget.addWidget(self.lbwdge)
        stackedwidget.addWidget(self.tbwdge)
        stackedwidget.addWidget(self.ghwdge)
        stackedwidget.addWidget(self.cdwdge)
        stackedwidget.addWidget(self.ldwdge)
        stackedwidget.addWidget(self.pgwdge)
        stackedwidget.addWidget(self.hlwdge)

        widgetlist.currentRowChanged.connect(lambda i:stackedwidget.setCurrentIndex(i))


        self.displaylayout.addWidget(stackedwidget)
        # self.displaylayout.addStretch()
        mlayout.addLayout(listlayout)
        mlayout.addSpacing(2)
        mlayout.addLayout(self.displaylayout)
        mlayout.addStretch()
        self.setLayout(mlayout)

    #label display
    def lb(self):   #label display
        mlayout = QVBoxLayout()

        label1 = QLabel("This sentence is too long, so need to set 'label.setWordWrap(True)'")
        label1.setFixedWidth(600)
        label1.setFixedHeight(100)
        label1.setWordWrap(True)  # 换行
        label1.setAlignment(Qt.AlignCenter)  # 对齐方式
        # label1.setText("Rest the Label")
        label1.setStyleSheet('''font-size: 24px;
                             color:red;
                             border: 2px solid gray;
                             border-radius: 8px''')
        # label1.setFixedSize(200, 100)
        # ----------------------------------------------------------------------
        label2 = QLabel()
        label2.setText("label2:Property setting")
        label2.setFixedSize(500, 100)
        # label2.setStyleSheet("QLabel{color:rgb(225,22,173,255);font-size:50px;font-weight:normal;font-family:Roman times;}")

        # color: rgb()
        # 中的四个参数, 前三个是控制颜色, 第四个控制透明度
        # font - size: 设置字体大小
        # font - weight: bold可设置字体加粗
        # font - family: 选择自己想要的颜色
        # setStyleSheet同时可以设置标签背景图片, 但无法使图片与标签大小匹配

        label2.setStyleSheet("QLabel{background:white;}"
                             r"QLabel{color:rgb(100,100,100,250);font-size:25px;font-weight:bold;font-family:Arial;}"
                             "QLabel:hover{color:rgb(100,100,100,120);}")

        # ----------------------------------------------------------------------
        label3 = QLabel()
        label3.setText("SetBackground")
        label3.setGeometry(50, 50, 200, 200)
        pixmap = QPixmap(r"C:\Sensirion\icons\Water Quality.svg").scaled(label3.width(), label3.height())
        label3.setPixmap(pixmap)

        # --------------------------------------
        # label3.setStyleSheet(r"QLabel{background-image: C:\Sensirion\icons\Water Quality.svg;}")
        label3.setStyleSheet(r"QLabel{background: white;}")

        # label3.setScaledContents(True)

        # ------------------------------------------------------------------------
        label4 = QLabel()
        label4.setFixedSize(300, 50)
        label4.setStyleSheet(r"QLabel{background: white;}"
                             r"QLabel{font-size:25px;font-weight:bold;font-family:Arial;}")
        label4.setText('<a href="https://www.baidu.com/">label4:百度一下</a>')
        label4.setOpenExternalLinks(True)

        # ------------------------------------------------------------------------

        mlayout.addWidget(label1)
        mlayout.addWidget(label2)
        mlayout.addWidget(label3)
        mlayout.addWidget(label4)

        # -----------------------------------------------------------------
        mlayout.addStretch()

        self.lbwdge.setLayout(mlayout)

    #TextBrowser display
    def tb(self):
        mlayout = QVBoxLayout()
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        # ----------------------------------------------------------------------
        self.textbrowser = QTextBrowser()
        self.textbrowser.setStyleSheet("QLabel{background:white;}")
        self.textbrowser.setText("<h1>Hello World!</h1>")  # 设置编辑框初始化时显示的文本
        self.textbrowser.setReadOnly(True)  # 设置编辑框是否为只读

        self.save_btn = QPushButton('Save')
        self.save_btn.clicked.connect(lambda: self.button_slot(self.save_btn))

        self.clear_btn = QPushButton('Clear')
        self.clear_btn.clicked.connect(lambda: self.button_slot(self.clear_btn))

        self.add_btn = QPushButton('Add')
        self.add_btn.clicked.connect(self.add_text)

        mlayout.addLayout(v_layout)
        mlayout.addLayout(h_layout)

        v_layout.addWidget(self.textbrowser)

        h_layout.addWidget(self.save_btn)
        h_layout.addWidget(self.clear_btn)
        h_layout.addWidget(self.add_btn)

        # mlayout.addStretch()

        self.tbwdge.setLayout(mlayout)

    #Graphic display
    def gh(self):
        mlyt = QVBoxLayout()
        noteedit = QTextEdit()
        noteedit.setText("To Do")
        noteedit.setStyleSheet("QTextEdit{font-size:24px}")

        mlyt.addWidget(noteedit)
        self.ghwdge.setLayout(mlyt)

    #Calendar display
    def cd(self):
        mlayout = QVBoxLayout()
        # ----------------------------------------------------------------------
        cal = QCalendarWidget(self)
        cal.setFixedSize(500, 300)

        cal.setDateRange(QDate(2020, 1, 1), QDate(2025, 12, 30))  # 设置日期范围
        # cal.setMinimumDate(QDate(2020,1,1))                 #设置日期最小值
        # cal.setMaximumDate(QDate(2025,12,30))               #设置日期最大值
        # cal.setFirstDayOfWeek(Qt.Monday)                    #设置星期的第一天
        # cal.minimumDate()                                   #获取控件的最小日期
        # cal.maximumDate()                                   #获取控件的最小日期
        # cal.setSelectedDate()                               #设置一个Qdate对象,作为日期控件所选定的日期

        cal.setGridVisible(True)  # 设置日历控件是否显示网格
        cal.clicked[QDate].connect(self.showDate)

        self.lb = QLabel(self)
        date = cal.selectedDate()  # 返回当前选定日期
        self.lb.setText(date.toString('yyyy-MM-dd dddd'))
        self.lb.move(20, 300)

        mlayout.addWidget(cal)
        mlayout.addWidget(self.lb)
        mlayout.addStretch()
        self.cdwdge.setLayout(mlayout)

    def ld(self):
        mlayout = QVBoxLayout()
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        # ----------------------------------------------------------------------
        lcd1 = QLCDNumber()
        lcd1.setDigitCount(10)  # 设置可以显示多少个数字
        lcd1.display(1234567)
        lcd1.setSegmentStyle(QLCDNumber.Filled)  # 数字样式, 可以是 QLCDNumber.Outline: 内容浮显  Filled: 浮显; Flat:扁平显

        lcd2 = QLCDNumber()
        lcd2.display(1.2364)
        lcd2.setSegmentStyle(QLCDNumber.Flat)
        lcd2.setSmallDecimalPoint(False)  # 设置小数点要不要占一个位置
        # lcd2.setMode(QLCDNumber.Hex)                  #进制: Hex, Dec, Oct, Bin

        # ----------------------------------------------------------------------
        mlayout.addWidget(lcd1)
        mlayout.addWidget(lcd2)
        self.ldwdge.setLayout(mlayout)
    def pg(self):
        mlyt = QVBoxLayout()
        self.pgb = QProgressBar(self)
        self.pgb.move(50, 50)
        self.pv = 0              #配置一个值表示当前进度
        self.timer1 = QBasicTimer()

        #设置当前进度的范围
        self.pgb.setMinimum(0)
        self.pgb.setMaximum(100)
        self.pgb.setValue(self.pv)

        self.btn = QPushButton("开始", self)
        self.btn.move(50, 100)
        self.btn.clicked.connect(self.myTimerState)

        mlyt.addWidget(self.pgb)
        mlyt.addWidget(self.btn)
        mlyt.addStretch()
        self.pgwdge.setLayout(mlyt)

    #HorizontalLine
    def hl(self):
        mlayout = QVBoxLayout()
        # ----------------------------------------------------------------------
        hl = QFrame()
        hl.setFrameShape(QFrame.HLine)
        # hl.setFrameStyle()
        hl.setFrameShadow(QFrame.Plain)

        vl = QFrame()
        vl.setFrameShape(QFrame.VLine)

        mlayout.addWidget(hl)
        mlayout.addWidget(vl)
        self.hlwdge.setLayout(mlayout)

    def cleaner(self, layout):  #清理布局  clean layout
        # 清空子布局
        item_list = list(range(layout.count()))
        item_list.reverse()  # 倒序删除，避免影响布局顺序
        for i in item_list:
            item = layout.itemAt(i)
            layout.removeItem(item)    #删除
            if item.widget():
                item.widget().deleteLater()

    # for text browser display
    def button_slot(self, button):
        if button == self.save_btn:
            choice = QMessageBox.question(self, "Question", "Do you want to save it?", QMessageBox.Yes | QMessageBox.No)
            if choice == QMessageBox.Yes:
                with open("TestBrowser.txt", 'w') as f:
                    f.write(self.textbrowser.toPlainText())
                self.close()
            elif choice == QMessageBox.No:
                self.close()
        elif button == self.clear_btn:
            self.textbrowser.clear()

    # for text browser display
    def add_text(self):
        self.textbrowser.append("<h1>Hello World!</h1>")   # 调用append方法可以向文本浏览框中添加文本
        print("Pressed!")

    # for Calender display
    def showDate(self,date):
        self.lb.setText(date.toString('yyyy-MM-dd dddd'))

    #Progress Bar
    def myTimerState(self):
        if self.timer1.isActive():
            self.timer1.stop()
            self.btn.setText("开始")
        else:
            self.timer1.start(100, self)
            self.btn.setText("停止")
    #Progress Bar
    def timerEvent(self, e):
        if self.pv == 100:
            self.timer1.stop()
            self.btn.setText("完成")
        else:
            self.pv += 1
            self.pgb.setValue(self.pv)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindown()
    w.show()

    app.exec()