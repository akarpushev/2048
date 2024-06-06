import sys

from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QMainWindow, QStackedWidget, QComboBox, QVBoxLayout


from cpu_monitor import CPUMonitor
from ram_monitor import RAMMonitor
from hd_monitor import HdMonitor

from system_monitoring import Ui_MainWindow

class Window(QMainWindow, QStackedWidget, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)





        self.cpu_monitor_ = CPUMonitor()
        self.ram_monitor_ = RAMMonitor()
        self.hd_monitor_ = HdMonitor()
        #self.ui.stackedWidget
        #self.stacked_widget = QStackedWidget(self)
        # self.stacked_widget.addWidget(self.cpu_monitor_)
        # self.stacked_widget.addWidget(self.ram_monitor_)
        # self.stacked_widget.addWidget(self.hd_monitor_)
        # self.combobox = QComboBox(self)
        # self.combobox.addItems(['cpu_monitor_', 'ram_monitor_', 'hd_monitor_'])
        #self.layout = QVBoxLayout(self)
        # self.layout.addWidget(self.combobox)
        # self.layout.addWidget(self.stacked_widget)
        # self.setLayout(self.layout)


        #self.combobox.activated.connect(self.stacked_widget.setCurrentIndex)

        self.ui.pushButton_cpu.clicked.connect(self.cpu_monitor)
        self.ui.pushButton_ram.clicked.connect(self.ram_monitor)
        #self.ui.pushButton_hd.clicked.connect(self.hd_monitor)
        #self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget.addWidget(self.ram_monitor_)
        self.ui.stackedWidget.addWidget(self.cpu_monitor_)
        #self.ui.stackedWidget.setCurrentIndex(1)


    def cpu_monitor(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.stackedWidget.setCurrentWidget(self.cpu_monitor_)
        #self.stacked_widget.setCurrentIndex(0)
        #self.ui.stackedWidget.show()

    def ram_monitor(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.stackedWidget.addWidget(self.cpu_monitor_)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()