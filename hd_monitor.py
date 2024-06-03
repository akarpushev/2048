from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit
import psutil

import os
import sys
from psutil._common import bytes2human


class HdMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        self.layout = QTextEdit(self.main_widget)
        self.layout.setGeometry(100, 100, 800, 600)

        self.layout.setText(f"количество HD: {len(psutil.disk_partitions())}\n\n"
                            f"{psutil.disk_partitions()}\n\n")

        #self.layout.

        #self.main()

    # def main(self):
    #     templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
    #     print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
    #                    "Mount"))
    #     for part in psutil.disk_partitions(all=False):
    #         if os.name == 'nt':
    #             if 'cdrom' in part.opts or part.fstype == '':
    #                 continue
    #         usage = psutil.disk_usage(part.mountpoint)
    #         print(templ % (
    #             part.device,
    #             bytes2human(usage.total),
    #             bytes2human(usage.used),
    #             bytes2human(usage.free),
    #             int(usage.percent),
    #             part.fstype,
    #             part.mountpoint))
    #         self.layout.setText(str(templ % ("Device", "Total", "Used", "Free", "Use ", "Type\n")))
    #
    #             (templ % ( part.device,
    #             bytes2human(usage.total),
    #             bytes2human(usage.used),
    #             bytes2human(usage.free),
    #             int(usage.percent)))



                # str(templ % (
                # part.device,
                # bytes2human(usage.total),
                # bytes2human(usage.used),
                # bytes2human(usage.free),
                # int(usage.percent),
                # part.fstype,
                # part.mountpoint)))


if __name__ == "__main__":
    app = QApplication()
    window = HdMonitor()
    window.show()
    app.exec()