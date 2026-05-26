import sys

def count_lines(filename):
    with open(filename, "r") as file:
        return len(file.readlines())

def count_words(filename):
    with open(filename, "r") as file:
        return len(file.read().split())

if len(sys.argv) < 2:
    print("Usage: python file_stats.py <filename>")
    sys.exit(1)

target_file = sys.argv[1]   # <-- now at the top level, after the guard

try:
    lines_total = count_lines(target_file)
    words_total = count_words(target_file)
    print(f"{target_file} has {lines_total} lines and {words_total} words.")
except FileNotFoundError:
    print(f"Error: The file '{target_file}' was not found.")
except PermissionError:
    print(f"Error: You do not have permission to read the file '{target_file}'.")
except Exception as e:
    print(f"An error occurred: {e}")