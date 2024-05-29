from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication, QMainWindow
from system_monitoring import Ui_MainWindow

from cpu_monutor import CPUMonitor
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

        self.ui.textEdit_1.setText(str(f"{platform.processor()} \n\n"
                                f"количество ядер: {os.cpu_count()} \n\n"
                                f"объём RAM: {psutil.virtual_memory().total}\n\n"
                                f"используемая RAM:"
                                f" {round(psutil.virtual_memory().used / psutil.virtual_memory().total * 100)}%\n\n"
                                f"количество HD: {len(psutil.disk_partitions())}"))
        # for i in range(len(psutil.disk_partitions())):
        #     total = psutil.disk_usage().total
        #     used = psutil.disk_usage().used



        #self.layout = FlexLayout()



        layout_1 = QtWidgets.QHBoxLayout()
        layout_1.addWidget(SystemMonitor())
        self.ui.tab_1.setLayout(layout_1)
        layout_1.setContentsMargins(350, 0, 0, 0)

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