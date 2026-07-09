"""
LRU Cache — combines a hash table (dict) with the DoublyLinkedList
from linked_list.py to achieve O(1) get and put.

DAY 2 TASKS: implement get() and put() (no eviction yet)
DAY 3 TASKS: add eviction logic to put()
"""

from src.linked_list import DoublyLinkedList, Node


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}  # key -> Node
        self.list = DoublyLinkedList()

    def get(self, key):
        """
        Return the value for `key` if present, else -1.
        Accessing a key marks it as most recently used.
        """
        # TODO (Day 2): implement
        raise NotImplementedError

    def put(self, key, value):
        """
        Insert or update `key` with `value`.
        If the cache is over capacity after inserting, evict the
        least recently used item.
        """
        # TODO (Day 2): handle insert/update
        # TODO (Day 3): handle eviction when over capacity
        raise NotImplementedError

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map
