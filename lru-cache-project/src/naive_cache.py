"""
Naive O(n) cache implementation, used only as a benchmark baseline
to prove the real LRUCache is faster.

DAY 5 TASKS: implement using a plain list of (key, value, timestamp) tuples.
"""

import time


class NaiveCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.entries = []  # list of [key, value, timestamp]

    def get(self, key):
        """Linear scan to find the key; update its timestamp if found."""
        # TODO (Day 5): implement
        raise NotImplementedError

    def put(self, key, value):
        """
        Linear scan to check if key exists (update if so).
        If inserting a new key over capacity, find and remove the
        entry with the oldest (minimum) timestamp — also linear.
        """
        # TODO (Day 5): implement
        raise NotImplementedError
