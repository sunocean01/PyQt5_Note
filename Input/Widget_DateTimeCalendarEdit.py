import sys
from PyQt5.QtGui import QIcon, QPixmap, QFont, QRegExpValidator, QIntValidator
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QStackedLayout, QSplitter, \
    QWidget, QPushButton, QLabel, QDesktopWidget, QSizePolicy, QLineEdit, QTextEdit, QTextBrowser, QMessageBox, \
    QComboBox, QFontComboBox, QGroupBox, QSpinBox, QTimeEdit, QPlainTextEdit, QMainWindow, QDateEdit, QDateTimeEdit, \
    QCalendarWidget
from PyQt5.QtCore import Qt, QRegExp, QTime, QDate, QDateTime
from PyQt5 import  uic
# from PyQt5 import *

# QStackedLayout栈式布局管理器不能直接嵌套其它布局管理器，但可以通过QWidget容器组件间接嵌套使用其它布局管理器。

class MyWindown(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.resize(1000, 400)
        self.setWindowTitle("Widget_DateTimeCalendarEdit")

        self.mlayout = QHBoxLayout(self)
        self.group01 = QGroupBox("DateTime")
        self.group02 = QGroupBox("Calendar")
        self.mlayout.addWidget(self.group01)
        self.mlayout.addWidget(self.group02)

        self._uiinit_01()
        self._uiinit_02()

        #信号与槽
        self.timeupdate.clicked.connect(self.on_timeupdate_clicked)
        self.dateupdate.clicked.connect(self.on_dateupdate_clicked)
        self.datetimeupdate.clicked.connect(self.on_datetimeupdate_clicked)
        self.time_btn.clicked.connect(self.on_time_btn_clicked)
# ------------------------------------------------------------------------
    def _uiinit_01(self):
        childlayout01 = QGridLayout(self.group01)
        self.time_btn = QPushButton("CurrentDateTime")
        self.timelabel = QLabel('StringDisplay')
        childlayout01.addWidget(self.time_btn, 0, 0, 1, 2)   #0, 0, 1, 2: 第一行第一列, 跨越1行2列
        childlayout01.addWidget(self.timelabel, 0, 2, 1, 2)
        childlayout01.addWidget(QLabel('Time:'), 1, 0, 1, 1)
        self.timeEdit = QTimeEdit(self.group01)
        self.timeEdit.setDisplayFormat("HH:mm:ss")
        self.timeEdit.setTime(QTime.currentTime())
        self.timeEdit_text = QLineEdit(QTime.currentTime().toString('HH:mm:ss'))
        self.timeupdate = QPushButton("TimeSetting")
        childlayout01.addWidget(self.timeEdit, 1, 1, 1, 1)
        childlayout01.addWidget(self.timeEdit_text, 1, 2, 1, 1)
        childlayout01.addWidget(self.timeupdate, 1, 3, 1, 1)

        #日期
        childlayout01.addWidget(QLabel('Date:'), 2, 0, 1, 1)
        self.dateedit = QDateEdit(QDate.currentDate())
        self.dateedit.setDisplayFormat("yyyy-MM-dd")
        self.dateedit.setMinimumDate(QDate.currentDate().addDays(-3652))
        self.dateedit.setMaximumDate(QDate.currentDate().addDays(3652))
        self.dateedit_text = QLineEdit(QDate.currentDate().toString('yyyy-MM-dd'))
        self.dateupdate = QPushButton("DateSetting")
        childlayout01.addWidget(self.dateedit, 2, 1, 1, 1)
        childlayout01.addWidget(self.dateedit_text, 2, 2, 1, 1)
        childlayout01.addWidget(self.dateupdate, 2, 3, 1, 1)

        #时间日期
        childlayout01.addWidget(QLabel('DateTime'), 3, 0, 1, 1)
        self.datetimeedit = QDateTimeEdit()
        self.datetimeedit.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        self.datetimeedit.setDateTime(QDateTime.currentDateTime())
        self.datetimeedit_text = QLineEdit(QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss"))
        self.datetimeupdate = QPushButton("DateTimeSetting")
        childlayout01.addWidget(self.datetimeedit, 3, 1, 1, 1)
        childlayout01.addWidget(self.datetimeedit_text, 3, 2, 1, 1)
        childlayout01.addWidget(self.datetimeupdate, 3, 3, 1, 1)
        childlayout01.setRowStretch(4, 4)

    def _uiinit_02(self):
        childlayout02 = QGridLayout(self.group02)
        childlayout02.addWidget(QLabel("DateSelection:"), 0, 0, 1, 1)
        self.lineedit = QLineEdit()
        childlayout02.addWidget(self.lineedit, 0, 1, 1, 1)
        self.calendar = QCalendarWidget(self.group02)
        self.calendar.setDateRange(QDate(2020, 1, 1), QDate(2099, 1, 1))

        childlayout02.addWidget(self.calendar, 1, 0, 1, 2)
        self.btn_quit = QPushButton("Quit")
        childlayout02.addWidget(self.btn_quit, 2, 0, 1, 2)

        #信号与槽
        '''
        void activated(const QDate & date)
        void clicked(const QDate & date)
        void currentPageChanged(int year, int month)
        void selectionChanged()
        '''
        self.calendar.clicked.connect(self.calendar_clicked)
        self.calendar.selectionChanged.connect(lambda: print("Selected"))
        self.btn_quit.clicked.connect(lambda:self.close())

    def on_timeupdate_clicked(self):
        self.timeEdit.setTime(QTime.fromString(self.timeEdit_text.text()))

    def on_dateupdate_clicked(self):
        date = QDate.fromString(self.dateedit_text.text(), "yyyy-MM-dd")
        self.dateedit.setDate(date)

    def on_datetimeupdate_clicked(self):
        datetime = QDateTime.fromString(self.datetimeedit_text.text(), "yyyy-MM-dd HH:mm:ss")
        self.datetimeedit.setDateTime(datetime)

    def on_time_btn_clicked(self):
        self.timeEdit.setTime(QTime.currentTime())
        self.dateedit.setDate(QDate.currentDate())
        self.datetimeedit.setDateTime(QDateTime.currentDateTime())

        self.timeEdit_text.setText(QTime.currentTime().toString("HH:mm:ss"))
        self.dateedit_text.setText(QDate.currentDate().toString("yyyy-MM-dd"))
        self.datetimeedit_text.setText(QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss"))

    def calendar_clicked(self, date):
        self.lineedit.setText(date.toString("yyyy-MM-dd"))

        self.dateedit.setDate(date)
        self.dateedit_text.setText(date.toString("yyyy-MM-dd"))



# ------------------------------------------------------------------------


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindown()
    w.show()

    app.exec()