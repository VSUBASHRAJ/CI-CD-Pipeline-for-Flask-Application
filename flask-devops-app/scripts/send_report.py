import datetime
report_file = "./logs/daily_report.txt"
with open(report_file, "a") as f:
    f.write(f"Report generated at {datetime.datetime.now()}\n")
print(f"Report saved to {report_file}")