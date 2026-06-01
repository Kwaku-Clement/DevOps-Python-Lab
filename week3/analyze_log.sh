#!/bin/bash

# 1. Check if the user provided a filename as an argument
if [ -z "$1" ]; then
  echo "Usage: ./analyze_log.sh <log_file>"
  exit 1
fi

LOGFILE=$1

# Check if the file actually exists before running analysis
if [ ! -f "$LOGFILE" ]; then
  echo "Error: File '$LOGFILE' not found!"
  exit 1
fi

# 2. Count the total number of lines
TOTAL_LINES=$(wc -l < "$LOGFILE")
echo "Total lines in log file: $TOTAL_LINES"

# 3. Count lines containing "ERROR"
ERROR_COUNT=$(grep -c "ERROR" "$LOGFILE")
echo "ERROR count: $ERROR_COUNT"

# 4. Count lines containing "WARNING"
WARNING_COUNT=$(grep -c "WARNING" "$LOGFILE")
echo "WARNING count: $WARNING_COUNT"

# 5. Print the last 3 lines (bottom of the file)
echo "last 3 lines of the log file:"
tail -n 3 "$LOGFILE"