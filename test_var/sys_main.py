from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication, QMainWindow
from system_monitoring import Ui_MainWindow
from cpu_monutor import CPUMonitor
import os
import platform
import psutil
import time


# class SystemMonitor(QtCore.QThread):
#     system_info = QtCore.Signal(list)
#
#     def run(self):
#         while True:
#             time.sleep(0.5)
#             self.system_info.emit(psutil.cpu_percent(percpu=True))
#
#
# class SystemWidget(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.initUi()
#
#     def initUi(self) -> None:
#         """
#         Инициализация Ui
#         :return: None
#         """
#         self.system_value = QtWidgets.QProgressBar()
#         self.system_value.setRange(0, 100)
#         self.system_value.setOrientation(QtCore.Qt.Orientation.Vertical)
#         self.system_value.setSizePolicy(
#             QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
#
#         self.system_label = QtWidgets.QLabel()
#
#         layout = QtWidgets.QVBoxLayout()
#         layout.addWidget(self.system_value)
#         layout.addWidget(self.system_label)
#
#         self.setLayout(layout)
#
#     def setValue(self, value: int) -> None:
#         """
#         Установка значения system_value в CPUWidget
#         :param value: новое значение
#         :return: None
#         """
#         self.system_value.setValue(value)
#
#     def setText(self, text: str) -> None:
#         """
#         Установка значения system_label в CPUWidget
#         :param text: новый текст в виджете
#         :return: None
#         """
#         self.system_label.setText(text)


class Window(QMainWindow, QtCore.QSettings, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit_cpu.setText(str(f"{platform.processor()}"))

        self.ui.textEdit_1.setText(str(f"{platform.processor()} \n\n"
                                       f"количество ядер: {os.cpu_count()} \n\n"
                                       f"объём оперативной памяти: {psutil.virtual_memory().total}\n\n"
                                       f"используемая оперативная память: {psutil.virtual_memory().used}"))
        # layout = QtWidgets.QHBoxLayout()
        # for _ in range(psutil.cpu_count()):
        #     layout.addWidget(SystemWidget(self))
        #self.setLayout(layout)
        # self.ui.tab_2.setLayout(layout)
        # self.process_iter()

        # layout = CPUMonitor()
        # self.ui.tab_2.setLayout(layout)
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(CPUMonitor(self))
        self.ui.tab_2.setLayout(layout)




    # def CPUMonitor(self):
    #     self.CPUMonitor = CPUMonitor()
    #     layout = QtWidgets.QHBoxLayout()

        # self.systemMonitor.start()
        # self.systemMonitor.system_info.connect(self.updateSystemWidget)
        #self.systemMonitor.system_info

    def process_iter(self):
        for p in psutil.process_iter():
            self.ui.textEdit_2.setText(p.name())


    def updateSystemWidget(self, cpu_percent_list: list) -> None:
        """
        Обновление параметров системных виджетов
        :param cpu_percent_list: список со значениями загрузки CPU
        :return: None
        """
        # layout = self.layout()
        #
        # for cpu_count in range(layout.count()):
        #     widget_link = layout.itemAt(cpu_count).widget()
        #
        #     widget_link.setValue(cpu_percent_list[cpu_count])
        #     widget_link.setText(f"CPU №{cpu_count + 1} - {cpu_percent_list[cpu_count]}%")




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()