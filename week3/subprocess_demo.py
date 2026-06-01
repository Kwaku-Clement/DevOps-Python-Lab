import subprocess
import os

log_file_target = "sample.log"

try:
    #Run the shell script and check its outcome
    result = subprocess.run(
        ["./analyze_log.sh", log_file_target],
        capture_output=True,
        text=True,
        check=True
    )
    print("--- Output from bash script (via python) ---")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error: The script failed with exit code {e.returncode}")
    print(f"Standard Output: {e.stdout}")
    print(f"Error details: {e.stderr.strip()}")

except FileNotFoundError:
    print(f"Friendly Message: Could not find the executable script './analyze_logs.sh'. Please make sure it exists and is in the correct location.")