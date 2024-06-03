from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QStackedWidget

from system_monitoring import Ui_MainWindow
from cpu_monitor import CPUMonitor
from ram_monitor import RAMMonitor
from hd_monitor import HdMonitor
from cpu_core_monutor import CPU_Core_Monitor
from process_2 import ProcessMonitor
from service_2 import ServiceMonitor

import platform
import psutil
import os


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit_cpu.setText(str(f"{platform.processor()}\n"
                                         f"количество ядер: {os.cpu_count()}"))
        self.ui.textEdit_ram.setText(str(f"{psutil.virtual_memory().total}"))
        self.ui.textEdit_hd.setText(str(f"{len(psutil.disk_partitions())}\n"
                                        ))

        #self.ui.textEdit_2.setText(f"{psutil.process_iter()}")
        #self.ui.textEdit_2.setText(f"{[item.name() for item in psutil.process_iter()]}")

        layout_2 = QtWidgets.QHBoxLayout()
        layout_2.addWidget(CPU_Core_Monitor())
        self.ui.tab_2.setLayout(layout_2)

        layout_3 = QtWidgets.QHBoxLayout()
        layout_3.addWidget(ProcessMonitor())
        self.ui.tab_3.setLayout(layout_3)

        layout_4 = QtWidgets.QHBoxLayout()
        layout_4.addWidget(ServiceMonitor())
        self.ui.tab_4.setLayout(layout_4)


        #                         f"количество ядер: {os.cpu_count()} \n\n"
        #                         f"объём RAM: {psutil.virtual_memory().total}\n\n"
        #                         f"используемая RAM:"
        #                         f" {round(psutil.virtual_memory().used / psutil.virtual_memory().total * 100)}%\n\n"
        #                         f"количество HD: {len(psutil.disk_partitions())}"))




        #self.ui.stackedWidget.addWidget(SystemMonitor())

        # self.cpu_monitor = SystemMonitor()
        # self.stacked_widget = QStackedWidget(self)
        # self.stacked_widget.addWidget(self.cpu_monitor)
        #
        # self.cpu_monitor = SystemMonitor()
        # self.stacked_widget = QStackedWidget(self)
        # self.stacked_widget.addWidget(self.cpu_monitor)
        # self.stacked_widget.setGeometry(500, 50,700, 500)

        # self.sW = QStackedWidget(self)
        # self.sW.setGeometry(200, 200, 200,200)
        # self.ui.tab_1.setLayout(self.sW)

        # self.layout = QVBoxLayout(self)
        # self.layout.addWidget(SystemMonitor)
        # self.ui.frame_cpu.

        self.ui.pushButton_cpu.clicked.connect(self.cpu_monitor)
        self.ui.pushButton_ram.clicked.connect(self.ram_monitor)
        self.ui.pushButton_hd.clicked.connect(self.hd_monitor)

        # self.ui.stackedWidget.setCurrentIndex(0)
        # self.ui.stackedWidget.addWidget(SystemMonitor())
        # self.ui.stackedWidget.setCurrentIndex(1)
        # self.ui.stackedWidget.addWidget(RAMMonitor())


    def cpu_monitor(self):
        self.cpu_monitor_ = CPUMonitor()
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.addWidget(self.cpu_monitor_)
        self.stacked_widget.setGeometry(500, 50, 700, 500)
        self.stacked_widget.show()


        #self.stacked_Widget.setCurrentIndex(0)
        #self.ui.stackedWidget.setCurrentIndex(0)
        # self.ui.stackedWidget.addWidget(SystemMonitor())


        # layout_cpu = QtWidgets.QHBoxLayout()
        # layout_cpu.addWidget(SystemMonitor())
        # self.ui.stackedWidget.setLayout(layout_cpu)

    def ram_monitor(self):
        self.ram_monitor_ = RAMMonitor()
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.addWidget(self.ram_monitor_)
        self.stacked_widget.setGeometry(500, 50, 700, 500)
        self.stacked_widget.show()

    def hd_monitor(self):
        self.hd_monitor_ = HdMonitor()
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.addWidget(self.hd_monitor_)
        self.stacked_widget.setGeometry(500, 50, 700, 500)
        self.stacked_widget.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
