log_file = "app.log"
report_file = "log_report.txt"

error_messages = []
warning_count = 0
info_count = 0
error_count = 0
error_frequency = {}

try:
    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
                message = line.strip()
                error_messages.append(message)

                # Count frequency of each error
                error_frequency[message] = error_frequency.get(message, 0) + 1

            elif "WARNING" in line:
                warning_count += 1

            elif "INFO" in line:
                info_count += 1

    # Print summary to terminal
    print("------ LOG ANALYSIS SUMMARY ------")
    print("INFO messages   :", info_count)
    print("WARNING messages:", warning_count)
    print("ERROR messages  :", error_count)

    print("\nERROR DETAILS:")
    for error, count in error_frequency.items():
        print(f"{count} times → {error}")

    # Write summary report to file
    with open(report_file, "w", encoding="utf-8") as report:
        report.write("LOG FILE ANALYSIS REPORT\n")
        report.write("------------------------\n")
        report.write(f"INFO messages    : {info_count}\n")
        report.write(f"WARNING messages : {warning_count}\n")
        report.write(f"ERROR messages   : {error_count}\n\n")

        report.write("ERROR DETAILS:\n")
    for error, count in error_frequency.items():
         print("\nReport saved successfully to", report_file)

except FileNotFoundError:
    print("Log file not found. Please check file name and path.")
