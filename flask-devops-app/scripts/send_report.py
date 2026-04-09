import datetime
import os

log_dir = "./logs"

# Create folder if not exists
os.makedirs(log_dir, exist_ok=True)

report_file = os.path.join(log_dir, "daily_report.txt")

with open(report_file, "a") as f:
    f.write(f"Report generated at {datetime.datetime.now()}\n")

print(f"Report saved to {report_file}")