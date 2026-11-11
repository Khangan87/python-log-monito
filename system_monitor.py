import platform
print("system:", platform.system()) 
print("release:", platform.release())
print("Machine:", platform.machine())
print("python version:", platform.python_version())


import os
print("Current Working Directory:", os.getcwd())
print("os system:", os.name)
print("user:", os.getlogin())


import psutil
print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
memory = psutil.virtual_memory()
print("Total RAM:" , memory.total / (1024 ** 3), "GB")
print("Available RAM:" , memory.available / (1024 ** 3), "GB")
print("Used RAM:" , memory.used / (1024 ** 3), "GB")
print("RAM Usage Percentage:", memory.percent, "%")   
disk = psutil.disk_usage('/')
print("Total Disk Space:", disk.total / (1024 ** 3), "GB")
print("Used Disk Space:", disk.used / (1024 ** 3), "GB")
print("Free Disk Space:", disk.free / (1024 ** 3), "GB") 
print("Disk Usage Percentage:", disk.percent, "%")

 