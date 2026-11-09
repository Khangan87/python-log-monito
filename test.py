
import json

with open("server.json", "r") as file:
    servers = json.load(file)


def check_cpu(cpu):
    if cpu > 80:
        return "Critical"
    elif cpu > 65:
        return "Warning"
    else:
        return "Normal"

status = check_cpu(90)
print(f"CPU: {status}")
status = check_cpu(70)
print(f"CPU: {status}")
status = check_cpu(50)
print(f"CPU: {status}")
