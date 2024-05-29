from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication, QMainWindow
from system_monitoring import Ui_MainWindow
import os
import platform
import psutil
import time


class Window(QMainWindow, QtCore.QSettings, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class SystemMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Системный монитор")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        self.main_widget = QWidget(self)


if __name__ == "__main__":
    app = QApplication()
    window = SystemMonitor()
    window.show()
    app.exec()