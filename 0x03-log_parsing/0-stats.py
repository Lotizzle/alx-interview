#!/usr/bin/env python3
"""
This module contains the print_statistics, parse_line, and main functions.
"""

import sys
from collections import defaultdict


def print_statistics(total_size, status_counts):
    """
    This Function prints statistics after
    every 10 lines and/or a keyboard interruption
    """
    print("File size:", total_size)
    for status_code, count in sorted(status_counts.items()):
        print(f"{status_code}: {count}")

def parse_line(line):
    """
    This functioon parses the stdin line to draw metrics
    """
    parts = line.strip().split()
    if len(parts) < 9:
        return None, None
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = parts[-1]
    if not status_code.isdigit():
        return None, None
    return status_code, int(file_size)

def main():
    """
    The main function
    """
    total_size = 0
    status_counts = defaultdict(int)
    try:
        for i, line in enumerate(sys.stdin, 1):
            status_code, file_size = parse_line(line)
            if status_code is None or file_size is None:
                continue
            total_size += file_size
            status_counts[status_code] += 1
            if i % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        raise

if __name__ == "__main__":
    main()
