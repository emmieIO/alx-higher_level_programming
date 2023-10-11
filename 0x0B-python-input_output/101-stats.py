#!/usr/bin/python3
"""Reads from standard input and computes metrics."""
import sys


def main():
    """
    Main function to read input from stdin, compute metrics, and print them.
    """
    # Define a dictionary to store status code counts
    status_code_counts = {}

    # Initialize variables to keep track of total file size and line count
    total_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()

            # Split the line into its components
            parts = line.split()
            if len(parts) != 7:
                continue  # Skip invalid lines

            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update the status code counts
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1

            # Update total file size and line count
            total_size += file_size
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print(f"File size: {total_size}")
                for code in sorted(status_code_counts):
                    print(f"{code}: {status_code_counts[code]}")

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print(f"File size: {total_size}")
        for code in sorted(status_code_counts):
            print(f"{code}: {status_code_counts[code]}")

if __name__ == "__main__":
    main()
