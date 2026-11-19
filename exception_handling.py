try:
	with open("system_monitor.log", "r") as file:
		data = file.read()
	print(data)
except FileNotFoundError:
	print("Error: Log file not found.")
else:
	print("Log file read successfully.")
finally:
	print("Log monitoring completed.")
 
cpu_usage =95
try:
     if cpu_usage > 90:
         raise Exception("High CPU Usage Detected!")
     print("CPU Usage is Normal.")
except Exception as error:
     print("Error:", error)
finally:
     print("CPU monitoring completed.")    