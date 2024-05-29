import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

class SystemMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Системный монитор")
        self.setGeometry(100, 100, 800, 600)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemMonitor()
    window.show()
    app.exec()