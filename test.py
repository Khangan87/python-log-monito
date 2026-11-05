
import json
with open("server.json", "r") as file:
    servers = json.load(file)

for server in servers:
    if server["CPU"] > 80:
        print("CRITICAL:", server["name"])
    elif server["CPU"] > 65:
        print("WARNING:", server["name"])
    else:
        print("NORMAL:", server["name"])