try:
    error_count = 0
    warning_count = 0
    critical_count = 0
    info_count = 0
    total_logs = 0
    with open("logs.txt", "r") as file:
        for line in file:
            total_logs += 1
            if "CRITICAL" in line:
                critical_count += 1
                print(line.strip())
            elif "ERROR" in line:
                error_count += 1
                print(line.strip())
            elif "WARNING" in line:
                warning_count += 1
                print(line.strip())
            elif "INFO" in line:
                info_count += 1
                print(line.strip())
                    
    print(f"Errors: {error_count}")
    print(f"Warnings: {warning_count}")
    print(f"Critical: {critical_count}")
    print(f"Info: {info_count}")
    print(f"Total Logs: {total_logs}")
    if critical_count > 0:
        print("ALERT: Critical issues found!")
    else:
        print("system running normally.")
except FileNotFoundError:
    print("Log file not found.")