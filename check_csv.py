#!/usr/bin/python3

import csv
import sys

def is_csv_file(file_path):
    try:
        with open(file_path, 'r', newline='') as file:
            dialect = csv.Sniffer().sniff(file.read(1024))
            return dialect.delimiter == ',' or dialect.delimiter == ';'
    except csv.Error:
        return False
    except FileNotFoundError:
        return False

if len(sys.argv) != 2:
    print("Usage: python check_csv.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

if is_csv_file(file_path):
    print(f"'{file_path}' is a CSV file.")
else:
    print(f"'{file_path}' is not a CSV file.")
