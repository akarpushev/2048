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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 550)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1200, 550))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.widget = QWidget(self.tab_1)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 471, 491))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_cpu = QPushButton(self.widget)
        self.pushButton_cpu.setObjectName(u"pushButton_cpu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cpu.sizePolicy().hasHeightForWidth())
        self.pushButton_cpu.setSizePolicy(sizePolicy)
        self.pushButton_cpu.setMinimumSize(QSize(100, 40))
        self.pushButton_cpu.setMaximumSize(QSize(100, 40))

        self.gridLayout.addWidget(self.pushButton_cpu, 0, 0, 1, 1)

        self.textEdit_cpu = QTextEdit(self.widget)
        self.textEdit_cpu.setObjectName(u"textEdit_cpu")
        sizePolicy.setHeightForWidth(self.textEdit_cpu.sizePolicy().hasHeightForWidth())
        self.textEdit_cpu.setSizePolicy(sizePolicy)
        self.textEdit_cpu.setMinimumSize(QSize(350, 45))
        self.textEdit_cpu.setMaximumSize(QSize(350, 45))

        self.gridLayout.addWidget(self.textEdit_cpu, 0, 1, 1, 1)

        self.pushButton_ram = QPushButton(self.widget)
        self.pushButton_ram.setObjectName(u"pushButton_ram")
        sizePolicy.setHeightForWidth(self.pushButton_ram.sizePolicy().hasHeightForWidth())
        self.pushButton_ram.setSizePolicy(sizePolicy)
        self.pushButton_ram.setMinimumSize(QSize(100, 40))
        self.pushButton_ram.setMaximumSize(QSize(100, 40))

        self.gridLayout.addWidget(self.pushButton_ram, 1, 0, 1, 1)

        self.textEdit_ram = QTextEdit(self.widget)
        self.textEdit_ram.setObjectName(u"textEdit_ram")
        sizePolicy.setHeightForWidth(self.textEdit_ram.sizePolicy().hasHeightForWidth())
        self.textEdit_ram.setSizePolicy(sizePolicy)
        self.textEdit_ram.setMinimumSize(QSize(350, 40))
        self.textEdit_ram.setMaximumSize(QSize(350, 40))

        self.gridLayout.addWidget(self.textEdit_ram, 1, 1, 1, 1)

        self.pushButton_hd = QPushButton(self.widget)
        self.pushButton_hd.setObjectName(u"pushButton_hd")
        self.pushButton_hd.setEnabled(True)
        self.pushButton_hd.setMinimumSize(QSize(100, 40))
        self.pushButton_hd.setMaximumSize(QSize(100, 40))

        self.gridLayout.addWidget(self.pushButton_hd, 2, 0, 1, 1)

        self.textEdit_hd = QTextEdit(self.widget)
        self.textEdit_hd.setObjectName(u"textEdit_hd")
        sizePolicy.setHeightForWidth(self.textEdit_hd.sizePolicy().hasHeightForWidth())
        self.textEdit_hd.setSizePolicy(sizePolicy)
        self.textEdit_hd.setMinimumSize(QSize(350, 40))
        self.textEdit_hd.setMaximumSize(QSize(350, 40))

        self.gridLayout.addWidget(self.textEdit_hd, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
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
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u044b\u0439 \u043c\u043e\u043d\u0438\u0442\u043e\u0440", None))
        self.pushButton_cpu.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440", None))
        self.pushButton_ram.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043c\u044f\u0442\u044c", None))
        self.pushButton_hd.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043e \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0443\u0436\u0431\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a \u0437\u0430\u0434\u0430\u0447", None))
    # retranslateUi

