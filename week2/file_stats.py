import sys

def count_lines(filename):
    """Counts the number of lines in a file."""
    with open(filename, "r") as file:
        lines = file.readlines()
        return len(lines)

def count_words(filename):
    """opens a file and returns the total number of words"""
    with open(filename, "r") as file:
        content = file.read()
        words = content.split()
        return len(words)
        
if len(sys.argv) < 2:
    print("Usage: python file_stats.py <filename>")
    sys.exit(1)
    
    target_file = sys.argv[1]

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