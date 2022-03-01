import json

x = {"name":"jeyawin",
    "age":"23",
    "ip":"192.168.23.103"
}
y = json.dumps(x)
print(type(y))