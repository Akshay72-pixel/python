temperature = 33
device_status = "active".lower()

if device_status == "active":
    if temperature > 35:
        print("High Temperature !")
    else:
        print("Normal temperature")
else:
    print("Device is offline")