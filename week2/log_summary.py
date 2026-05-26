import sys

def count_log_levels(filename):
    """
    Reads a log file and counts how many lines contain 'ERROR' or 'WARNING'.
    Returns a dictionary like {"ERROR": 12, "WARNING": 34}.
    """
    counts = {"ERROR": 0, "WARNING": 0}

    try:
        with open(filename, "r") as file:
            for line in file:
                if "ERROR" in line:
                    counts["ERROR"] += 1
                if "WARNING" in line:
                    counts["WARNING"] += 1
    except FileNotFoundError:
        prinnnt(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    return counts


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python log_summary.py <filename>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    stats = count_log_levels(log_file)

    print(f"Log Summary for '{log_file}':")
    print(f"ERROR: {stats['ERROR']} lines")
    print(f"WARNING: {stats['WARNING']} lines")
