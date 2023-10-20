#!/bin/usr/python3
"""stats"""
import sys
import signal

# Define a dictionary to store status code counts
status_code_counts = {}

# Initialize variables to store total file size and line count
total_file_size = 0
line_count = 0

def print_metrics(signum, frame):
    """
    Print metrics when a signal (CTRL + C) is received.
    """
    print(f"Total file size: {total_file_size}")
    
    # Print status code counts in ascending order
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        print(f"{status_code}: {count}")

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, print_metrics)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Check if the line has enough parts to extract status code and file size
        if len(parts) >= 9:
            status_code = parts[8]
            file_size = int(parts[-1])

            # Update total file size
            total_file_size += file_size

            # Update status code counts
            if status_code in ['200', '301', '400', '401', '403', '404', '405', '500']:
                status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics(None, None)

except KeyboardInterrupt:
    pass
