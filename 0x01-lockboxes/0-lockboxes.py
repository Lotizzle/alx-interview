#!/usr/bin/python3

"""This file contains a method that determines if all the boxes can
   be opened.
"""


def canUnlockAll(boxes):
    """Unlock boxes method
       Parameter: boxes
    """
    n = len(boxes)
    keys = set([0])
    openable_boxes = [0]

    while openable_boxes:
        box = openable_boxes.pop()
        for key in boxes[box]:
            if key not in keys and key < n:
                keys.add(key)
                openable_boxes.append(key)

    return len(keys) == n
