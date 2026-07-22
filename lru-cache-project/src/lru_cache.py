from .linked_list import DoublyLinkedList, Node


class LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        self.capacity = capacity
        self._map = {}
        self._list = DoublyLinkedList()
        self.hits = 0
        self.misses = 0

    def __len__(self):
        return len(self._map)

    def get(self, key):
        if key not in self._map:
            self.misses += 1
            return -1
        node = self._map[key]
        self._list.move_to_head(node)
        self.hits += 1
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

    def hit_rate(self):
        """Return the fraction of get() calls that were hits, as a float 0.0-1.0.
        Returns 0.0 if get() has never been called (avoids division by zero)."""
        total = self.hits + self.misses
        if total == 0:
            return 0.0
        return self.hits / total