#!/usr/bin/python3
"""
Calculating the island perimeter
"""

def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four sides
                if i == 0 or grid[i-1][j] == 0:  # top
                    perimeter += 1
                if i == rows - 1 or grid[i+1][j] == 0:  # bottom
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # left
                    perimeter += 1
                if j == cols - 1 or grid[i][j+1] == 0:  # right
                    perimeter += 1

    return perimeter
