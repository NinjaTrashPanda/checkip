#!/usr/bin/python3

# Sample data
data = [
    ("Name", "Age", "Location"),
    ("Alice", 30, "New York"),
    ("Bob", 25, "Los Angeles"),
    ("Charlie", 22, "San Francisco"),
]

print(data)
print()

# Find the maximum width for each column
max_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

# Create a format string based on column widths
format_string = " | ".join(f"{{:<{width}}}" for width in max_widths)

# Print the table header
print(format_string.format(*data[0]))

# Print the data rows
for row in data[1:]:
    print(format_string.format(*row))
