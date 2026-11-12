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
print("\nRunning Processes:")
for proc in psutil.process_iter(['pid', 'name']):
    print(proc.info)
print("\nPython Processes:")

for process in psutil.process_iter(["pid", "name"]):
    if "python" in process.info["name"].lower():
        print(process.info)
print("\nProcess CPU Usage:")

for process in psutil.process_iter(["pid", "name"]):
    try:
        cpu = process.cpu_percent(interval=0.1)

        print(
            "PID:", process.info["pid"],
            "Name:", process.info["name"],
            "CPU:", cpu, "%"
        )

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass            