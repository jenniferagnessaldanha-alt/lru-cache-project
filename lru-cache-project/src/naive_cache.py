"""
Naive Cache (baseline for benchmarking)

A deliberately "obvious but slow" LRU implementation: a plain dict for
values plus a plain list to track usage order. Same external interface as
LRUCache, but get() and put()-with-eviction are O(n) instead of O(1)
because list.remove() does a linear scan.

This exists so benchmark.py has something slow to compare LRUCache
against, making the O(1) vs O(n) difference visible in real numbers.
"""


class NaiveCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        self.capacity = capacity
        self._data = {}          # key -> value
        self._usage_order = []   # least recently used first, most recently used last

    def __len__(self):
        return len(self._data)

    def get(self, key):
        """Return the value for `key`, or -1 if not present."""
        if key not in self._data:
            return -1
        self._usage_order.remove(key)   # O(n) scan -- this is the "naive" part
        self._usage_order.append(key)
        return self._data[key]

    def put(self, key, value):
        """Insert or update `key` with `value`."""
        if key in self._data:
            self._data[key] = value
            self._usage_order.remove(key)   # O(n) scan
            self._usage_order.append(key)
            return

        self._data[key] = value
        self._usage_order.append(key)

        if len(self._data) > self.capacity:
            lru_key = self._usage_order.pop(0)   # remove least recently used
            del self._data[lru_key]