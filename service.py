import psutil
import time
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit
from PySide6 import QtCore


class Monitor(QtCore.QThread):
    service_name = QtCore.Signal(list)

    def run(self):
        while True:
            time.sleep(0.5)
            self.service_name.emit(psutil.win_service_iter())


class ServiceMonitor(QMainWindow, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()
        self.initThreads()

    def initUI(self) -> None:
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout(self.main_widget)
        self.text = QTextEdit()

    def initThreads(self) -> None:
        self.serviceMonitor = Monitor()
        self.serviceMonitor.start()
        self.serviceMonitor.service_name.connect(self.updateSystemWidget)

    def updateSystemWidget(self) -> None:
        service_name = [(item.name(), item.status()) for item in psutil.win_service_iter()]
        self.text.setText(str(service_name))
        self.layout.addWidget(self.text)


if __name__ == "__main__":
    app = QApplication()
    window = ServiceMonitor()
    window.show()
    app.exec()
