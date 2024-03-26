#!/usr/bin/python3
"""
Lock Boxes
"""


from collections import deque


def canUnlockAll(boxes):
    """
        Return True if all boxes can be opened, else return False
    """
    num_boxes = len(boxes)
    seen_boxes = set()
    keys_queue = deque([0])  # Start with the key to the first box (index 0)

    while keys_queue:
        current_box = keys_queue.popleft()
        seen_boxes.add(current_box)

        # Add keys from the current box to the queue
        for key in boxes[current_box]:
            if key < num_boxes and key not in seen_boxes:
                keys_queue.append(key)

    # Check if all boxes have been seen
    return len(seen_boxes) == num_boxes

# # Example usage:
# boxes = [[1], [2], [3], []]  # Each box contains the key to the next box
# print(canUnlockAll(boxes))  # Output: True

# boxes = [[1, 3], [2], [3], []]  # Box 0 has keys to boxes 1 and 3
# print(canUnlockAll(boxes))  # Output: False
