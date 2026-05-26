import os

all_files = os.listdir(".")

log_files = []

for file in all_files:
    if file.endswith(".log"):
        log_files.append(file)

if log_files:
    print(f"Found the following log files in the current directory:")
    for log in log_files:
        print(f"- {log}")
else:
    print(f"No .log file found")