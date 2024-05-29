from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication, QMainWindow
from system_monitoring import Ui_MainWindow

from cpu_monutor import CPUMonitor
from ram_monitor import RAMMonitor
from monitor import SystemMonitor

import os
import platform
import psutil
import time


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit_cpu.setText(str(f"{platform.processor()}"))
        self.ui.textEdit_ram.setText(str(f"{psutil.virtual_memory().total}"))
        self.ui.textEdit_hd.setText(str(f"{len(psutil.disk_partitions())}"))

        self.ui.textEdit_2.setText(f"{psutil.process_iter()}")

        # self.ui.textEdit_1.setText(str(f"{platform.processor()} \n\n"
        #                         f"количество ядер: {os.cpu_count()} \n\n"
        #                         f"объём RAM: {psutil.virtual_memory().total}\n\n"
        #                         f"используемая RAM:"
        #                         f" {round(psutil.virtual_memory().used / psutil.virtual_memory().total * 100)}%\n\n"
        #                         f"количество HD: {len(psutil.disk_partitions())}"))

        self.stacked_Widget = self.ui.stackedWidget
        self.stacked_Widget.addWidget(SystemMonitor())

        self.ui.pushButton_cpu.clicked.connect(self.cpu_monitor())
        self.ui.pushButton_ram.clicked.connect(self.ram_monitor())
        self.ui.pushButton_hd.clicked.connect(self.hd_monitor())

        # self.ui.stackedWidget.setCurrentIndex(0)
        # self.ui.stackedWidget.addWidget(SystemMonitor())
        # self.ui.stackedWidget.setCurrentIndex(1)
        # self.ui.stackedWidget.addWidget(RAMMonitor())


    def cpu_monitor(self):
        self.stacked_Widget.setCurrentIndex(0)
        #self.ui.stackedWidget.setCurrentIndex(0)
        # self.ui.stackedWidget.addWidget(SystemMonitor())


        # layout_cpu = QtWidgets.QHBoxLayout()
        # layout_cpu.addWidget(SystemMonitor())
        # self.ui.stackedWidget.setLayout(layout_cpu)

    def ram_monitor(self):
        pass

    def hd_monitor(self):
        pass








        # layout_1 = QtWidgets.QHBoxLayout()
        # layout_1.addWidget(SystemMonitor())
        # self.ui.tab_1.setLayout(layout_1)
        # layout_1.setContentsMargins(350, 0, 0, 0)

        layout_2 = QtWidgets.QHBoxLayout()
        layout_2.addWidget(CPUMonitor())
        self.ui.tab_2.setLayout(layout_2)
        #self.setLayout(layout_2)



    def process_iter(self):
        for p in psutil.process_iter():
            self.ui.textEdit_2.setText(p.name())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()