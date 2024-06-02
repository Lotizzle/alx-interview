#!/usr/bin/python3
"""
Module contains script that reads stdin
line by line and computes metrics.
"""
import sys
import signal

total_size = 0
status_counts = {}
valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
line_count = 0


def print_stats():
    """Print the accumulated metrics."""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts):
        if status_code in valid_status_codes:
            print(f"{status_code}: {status_counts[status_code]}")


def signal_handler(sig, frame):
    """Handle the keyboard interruption."""
    print_stats()
    sys.exit(0)


# Set the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) == 9:
            file_size = parts[-1]
            status_code = parts[-2]
            try:
                total_size += int(file_size)
                if (status_code.isdigit() and
                        int(status_code) in valid_status_codes):
                    if int(status_code) not in status_counts:
                        status_counts[int(status_code)] = 1
                    else:
                        status_counts[int(status_code)] += 1
            except ValueError:
                continue

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
