# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(474, 378)
        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(50, 30, 371, 51))
        self.n1 = QPushButton(Form)
        self.n1.setObjectName(u"n1")
        self.n1.setGeometry(QRect(30, 90, 41, 41))
        self.n1.setCheckable(False)
        self.n2 = QPushButton(Form)
        self.n2.setObjectName(u"n2")
        self.n2.setGeometry(QRect(90, 90, 41, 41))
        self.n3 = QPushButton(Form)
        self.n3.setObjectName(u"n3")
        self.n3.setGeometry(QRect(150, 90, 41, 41))
        self.n4 = QPushButton(Form)
        self.n4.setObjectName(u"n4")
        self.n4.setGeometry(QRect(30, 140, 41, 41))
        self.n5 = QPushButton(Form)
        self.n5.setObjectName(u"n5")
        self.n5.setGeometry(QRect(90, 140, 41, 41))
        self.n6 = QPushButton(Form)
        self.n6.setObjectName(u"n6")
        self.n6.setGeometry(QRect(150, 140, 41, 41))
        self.plus = QPushButton(Form)
        self.plus.setObjectName(u"plus")
        self.plus.setGeometry(QRect(210, 90, 41, 41))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 330, 371, 22))
        self.n7 = QPushButton(Form)
        self.n7.setObjectName(u"n7")
        self.n7.setGeometry(QRect(30, 200, 41, 41))
        self.n8 = QPushButton(Form)
        self.n8.setObjectName(u"n8")
        self.n8.setGeometry(QRect(90, 200, 41, 41))
        self.n9 = QPushButton(Form)
        self.n9.setObjectName(u"n9")
        self.n9.setGeometry(QRect(150, 200, 41, 41))
        self.n0 = QPushButton(Form)
        self.n0.setObjectName(u"n0")
        self.n0.setGeometry(QRect(30, 250, 41, 41))
        self.minus = QPushButton(Form)
        self.minus.setObjectName(u"minus")
        self.minus.setGeometry(QRect(270, 90, 41, 41))
        self.multiply = QPushButton(Form)
        self.multiply.setObjectName(u"multiply")
        self.multiply.setGeometry(QRect(210, 140, 41, 41))
        self.divide = QPushButton(Form)
        self.divide.setObjectName(u"divide")
        self.divide.setGeometry(QRect(270, 140, 41, 41))
        self.equal = QPushButton(Form)
        self.equal.setObjectName(u"equal")
        self.equal.setGeometry(QRect(210, 200, 41, 41))
        self.C = QPushButton(Form)
        self.C.setObjectName(u"C")
        self.C.setGeometry(QRect(270, 200, 41, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.n1.setText(QCoreApplication.translate("Form", u"1", None))
        self.n2.setText(QCoreApplication.translate("Form", u"2", None))
        self.n3.setText(QCoreApplication.translate("Form", u"3", None))
        self.n4.setText(QCoreApplication.translate("Form", u"4", None))
        self.n5.setText(QCoreApplication.translate("Form", u"5", None))
        self.n6.setText(QCoreApplication.translate("Form", u"6", None))
        self.plus.setText(QCoreApplication.translate("Form", u"+", None))
        self.n7.setText(QCoreApplication.translate("Form", u"7", None))
        self.n8.setText(QCoreApplication.translate("Form", u"8", None))
        self.n9.setText(QCoreApplication.translate("Form", u"9", None))
        self.n0.setText(QCoreApplication.translate("Form", u"0", None))
        self.minus.setText(QCoreApplication.translate("Form", u"-", None))
        self.multiply.setText(QCoreApplication.translate("Form", u"*", None))
        self.divide.setText(QCoreApplication.translate("Form", u"/", None))
        self.equal.setText(QCoreApplication.translate("Form", u"=", None))
        self.C.setText(QCoreApplication.translate("Form", u"C", None))
    # retranslateUi

