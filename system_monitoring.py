# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'system_monitoring.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QStatusBar, QTabWidget, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(885, 654)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1150, 550))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.textEdit_1 = QTextEdit(self.tab_1)
        self.textEdit_1.setObjectName(u"textEdit_1")
        self.textEdit_1.setGeometry(QRect(0, 0, 480, 200))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_1.sizePolicy().hasHeightForWidth())
        self.textEdit_1.setSizePolicy(sizePolicy)
        self.textEdit_1.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"border.transparent\n"
"")
        self.scrollArea = QScrollArea(self.tab_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 200, 500, 256))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 498, 254))
        self.textEdit_cpu = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_cpu.setObjectName(u"textEdit_cpu")
        self.textEdit_cpu.setGeometry(QRect(100, 0, 400, 40))
        self.textEdit_ram = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_ram.setObjectName(u"textEdit_ram")
        self.textEdit_ram.setGeometry(QRect(100, 40, 400, 40))
        self.textEdit_hd = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_hd.setObjectName(u"textEdit_hd")
        self.textEdit_hd.setGeometry(QRect(100, 80, 400, 40))
        self.pushButton_cpu = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_cpu.setObjectName(u"pushButton_cpu")
        self.pushButton_cpu.setGeometry(QRect(0, 0, 100, 40))
        self.pushButton_ram = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_ram.setObjectName(u"pushButton_ram")
        self.pushButton_ram.setGeometry(QRect(0, 40, 100, 40))
        self.pushButton_hd = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_hd.setObjectName(u"pushButton_hd")
        self.pushButton_hd.setGeometry(QRect(0, 80, 100, 40))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox = QGroupBox(self.tab_1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(510, 10, 120, 80))
        self.groupBox.setAutoFillBackground(False)
        self.frame = QFrame(self.tab_1)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(670, 30, 120, 80))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget = QStackedWidget(self.tab_1)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(500, 200, 300, 250))
        self.page_cpu = QWidget()
        self.page_cpu.setObjectName(u"page_cpu")
        self.stackedWidget.addWidget(self.page_cpu)
        self.page_ram = QWidget()
        self.page_ram.setObjectName(u"page_ram")
        self.stackedWidget.addWidget(self.page_ram)
        self.page_hd = QWidget()
        self.page_hd.setObjectName(u"page_hd")
        self.stackedWidget.addWidget(self.page_hd)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.textEdit_2 = QTextEdit(self.tab_3)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(0, 0, 480, 120))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 885, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u044b\u0439 \u043c\u043e\u043d\u0438\u0442\u043e\u0440", None))
        self.pushButton_cpu.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440", None))
        self.pushButton_ram.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043c\u044f\u0442\u044c", None))
        self.pushButton_hd.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u043a", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043e \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0443\u0436\u0431\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a \u0437\u0430\u0434\u0430\u0447", None))
    # retranslateUi

