#import os
#print("Number of CPUs:", os.cpu_count())
#import platform
#print("ЦП", platform.processor())
#import psutil
#from PySide6.QtCore import QTimer

# def init_timer(self):
#   self.timer = QTimer()
#   self.timer.timeout.connect(self.print)
#import time

# while True:
#     time.sleep(5.5)
#     i = 0
#     for p in psutil.process_iter():
#         if p.status() == 'stopped':
#             i += 1
#             process = i, p.name(), p.status()
#             print(process)
        #print(i, p.name(), p.status())

# process_name = [item.name() for item in psutil.process_iter()]
# process_status = [item.status() for item in psutil.process_iter()]
# print(process_name, process_status)





#import time

# for proc in psutil.process_iter():
#     print(proc)
# for i in psutil.win_service_iter():
#     print(i)

# while True:
#     cpu_percent = psutil.cpu_percent(interval=1)
#     print(f"Использование процессора: {cpu_percent}%")
#     time.sleep(1)

# import schedule
# import time
#
# def job():
#   print("I'm working...")
#
# schedule.every().hour.do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().day.at("10:30").do(job)
#
# while True:
#   schedule.run_pending()
#   time.sleep(1)

# import psutil
# # for proc in psutil.process_iter(['name', 'status']):
# #     print(proc.info)
#
# for p in psutil.win_service_iter():
#     print(p.name(), p.status())

import os
import sys
import psutil
from psutil._common import bytes2human

def main():
    templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
    print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
                   "Mount"))
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':

                continue
        usage = psutil.disk_usage(part.mountpoint)
        print(templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))
        return templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint)

if __name__ == '__main__':
    sys.exit(main())



