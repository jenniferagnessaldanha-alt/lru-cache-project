"""
Doubly Linked List with sentinel head/tail nodes.
This is the ordering structure behind the LRU Cache.

DAY 1 TASKS (fill in the methods below):
- add_to_head(node)
- remove(node)
- remove_tail()
- move_to_head(node)
"""


class Node:
    """A single node in the doubly linked list. Represents one cache entry."""

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    Doubly linked list using sentinel (dummy) head and tail nodes.

    Layout:  head <-> [most recent] <-> ... <-> [least recent] <-> tail

    Using sentinels means add/remove never has to check "is this the
    first/last real node?" — there's always a real prev/next to link to.
    """

    def __init__(self):
        self.head = Node()  # sentinel, no real data
        self.tail = Node()  # sentinel, no real data
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node):
        """Insert `node` right after the head sentinel (most recently used position)."""
        # TODO: implement
        raise NotImplementedError

    def remove(self, node):
        """Unlink `node` from wherever it currently is in the list."""
        # TODO: implement
        raise NotImplementedError

    def remove_tail(self):
        """
        Remove and return the node just before the tail sentinel
        (the least recently used real node). Returns None if list is empty.
        """
        # TODO: implement
        raise NotImplementedError

    def move_to_head(self, node):
        """Move an existing node to the head position (mark as most recently used)."""
        # TODO: implement (hint: this is just remove() + add_to_head())
        raise NotImplementedError

    def is_empty(self):
        return self.size == 0

    def to_list(self):
        """Helper for debugging/tests: returns keys from head to tail as a list."""
        result = []
        current = self.head.next
        while current != self.tail:
            result.append(current.key)
            current = current.next
        return result
