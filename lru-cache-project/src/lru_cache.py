"""
LRU Cache — combines a hash table (dict) with the DoublyLinkedList
from linked_list.py to achieve O(1) get and put.

DAY 2 TASKS: implement get() and put() (no eviction yet)
DAY 3 TASKS: add eviction logic to put()
"""
from .linked_list import DoublyLinkedList, Node


class LRUCache:
    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError("capacity must be a non-negative integer")
        self.capacity = capacity
        self._map = {}
        self._list = DoublyLinkedList()

    def __len__(self):
        return len(self._map)

    def get(self, key):
        if key not in self._map:
            return -1
        node = self._map[key]
        self._list.move_to_head(node)
        return node.value

    def put(self, key, value):
        if key in self._map:
            node = self._map[key]
            node.value = value
            self._list.move_to_head(node)
            return

        node = Node(key, value)
        self._map[key] = node
        self._list.add_to_head(node)

        if len(self._map) > self.capacity:
            lru_node = self._list.remove_tail()
            del self._map[lru_node.key]