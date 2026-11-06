
import json

with open("server.json", "r") as file:
    servers = json.load(file)


def check_cpu():
    cpu = 90
    if cpu > 80:
        print("CPU: Critical")
    else:
        print("CPU: Normal")


for server in servers:
    print("\n server:", server["name"])

    if server["CPU"] > 80:
        print("CPU: Critical")
    elif server["CPU"] > 65:
        print("CPU: Warning")
    else:
        print("CPU: Normal")

    if server["Memory"] > 80:
        print("Memory: Critical")
    elif server["Memory"] > 65:
        print("Memory: Warning")
    else:
        print("Memory: Normal")

    if server["Disk"] > 80:
        print("Disk: Critical")
    elif server["Disk"] > 65:
        print("Disk: Warning")
    else:
        print("Disk: Normal")


check_cpu() 