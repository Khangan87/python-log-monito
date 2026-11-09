
import json
with open("server.json", "r") as f:
    servers = json.load(f)
def check_memory_usage(memory):
        if memory > 80:
            return "High Memory Usage"
        else:
            return "Memory Usage is Normal"
        
def check_cpu_usage(cpu):
        if cpu > 80:
            return "High CPU Usage"
        else:
            return "CPU Usage is Normal"

def check_disk_usage(disk):
        if disk > 80:
            return "High Disk Usage"
        else:
            return "Disk Usage is Normal"

for server in servers:
    print(f"\nServer Name: {server['name']}")
    cpu_status = check_cpu_usage(server['CPU'])
    memory_status = check_memory_usage(server['Memory'])
    disk_status = check_disk_usage(server['Disk'])
    print(f"Disk Status: {disk_status}")
    print(f"CPU Status: {cpu_status}")
    print(f"Memory Status: {memory_status}")       

