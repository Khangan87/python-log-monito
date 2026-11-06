
import json

with open("server.json", "r") as file:
    servers = json.load(file)


def check_cpu(cpu):
    
    if cpu > 80:
        print("CPU: Critical")
    else:
        print("CPU: Normal")


def check_memory(memory):
    
    if memory > 80:
        print("Memory: Critical")
    else:
        print("Memory: Normal")


def check_disk(disk):
    
    if disk > 80:
        print("Disk: Critical")
    else:
        print("Disk: Normal")


for server in servers:
    print("\n server:", server["name"])

    check_cpu(server["CPU"])
    check_memory(server["Memory"])
    check_disk(server["Disk"]) 