import os
print("Number of CPUs:", os.cpu_count())
import platform
print("ЦП", platform.processor())
import psutil

for p in psutil.process_iter():
  print(p.name(), p.status())
import time

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



