import psutil
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit


class ProcessMonitor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout(self.main_widget)
        self.text = QTextEdit()

        service_name = [(item.name(), item.status()) for item in psutil.process_iter()]
        self.text.setText(str(service_name))

        self.layout.addWidget(self.text)


if __name__ == "__main__":
    app = QApplication()
    window = ProcessMonitor()
    window.show()
    app.exec()
