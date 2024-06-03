import psutil
import time
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit
from PySide6.QtGui import QIcon



class SystemMonitor(QtCore.QThread):
    system_info = QtCore.Signal(list)

    def run(self):
        while True:
            time.sleep(0.5)
            self.system_info.emit(psutil.cpu_percent(percpu=True))


# class SystemWidget(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.initUi()
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

    # def setValue(self, value: int) -> None:
    #     """
    #     Установка значения system_value в CPUWidget
    #     :param value: новое значение
    #     :return: None
    #     """
    #     self.system_value.setValue(value)
    #
    # def setText(self, text: str) -> None:
    #     """
    #     Установка значения system_label в CPUWidget
    #     :param text: новый текст в виджете
    #     :return: None
    #     """
    #     self.system_label.setText(text)


class CPUMonitor(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()
        self.initThreads()
        self.process_data = []

    def initUI(self) -> None:

        self.setWindowTitle("мониторинг системы")
        self.setWindowIcon(QIcon('icon.png'))

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout(self.main_widget)

        self.text = QTextEdit()
        self.text.setText(str(self.process_data))
        self.layout.addWidget(self.text)

        layout = QtWidgets.QHBoxLayout()

        # for _ in range(psutil.cpu_count()):
        #     layout.addWidget(SystemWidget(self))

        self.setLayout(layout)

    def initThreads(self) -> None:
        """
        Инициализация потоков
        :return: None
        """
        self.systemMonitor = SystemMonitor()
        self.systemMonitor.start()
        self.systemMonitor.system_info.connect(self.updateSystemWidget)

    def updateSystemWidget(self, cpu_percent_list: list) -> None:
        """
        Обновление параметров системных виджетов
        :param cpu_percent_list: список со значениями загрузки CPU
        :return: None
        """
        layout = self.layout()

        for cpu_count in range(layout.count()):
            widget_link = layout.itemAt(cpu_count).widget()

            widget_link.setValue(cpu_percent_list[cpu_count])
            widget_link.setText(f"CPU №{cpu_count + 1} - {cpu_percent_list[cpu_count]}%")


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = CPUMonitor()
    win.show()

    app.exec()
