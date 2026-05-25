filename = input("Enter the filename (e.g., sample.log): ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

        line_count = len(lines)
    print(f"The file {filename} has {line_count} lines.")
except FileNotFoundError:
    print(f"Error: The file {filename} was not found. Please check the path and try again")