def check_disk(diskusage):
    if diskusage < 0 or diskusage > 100:
        return "INVALID  DISK USAGE"
    if diskusage > 75:
        return "CRITICAL ALERT"
    elif diskusage >= 70:
        return "WARNING!"
    else:
        return "DISK NORMAL"


try:
    diskusage = int(input("Enter disk usage%:"))
    print(check_disk(diskusage))

except ValueError:
    print("Please enter a valid number")