"""
Doubly Linked List with sentinel head/tail nodes.
This is the ordering structure behind the LRU Cache.
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
    """
    def __init__(self):
        self.head = Node()  # sentinel, no real data
        self.tail = Node()  # sentinel, no real data
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def __len__(self):
        return self.size

    def add_to_head(self, node):
        """Insert `node` right after the head sentinel (most recently used position)."""
        old_first = self.head.next
        node.prev = self.head
        node.next = old_first
        self.head.next = node
        old_first.prev = node
        self.size += 1

    def remove(self, node):
        """Unlink `node` from wherever it currently is in the list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None
        node.next = None
        self.size -= 1

    def remove_tail(self):
        """Remove and return the least recently used node. Returns None if empty."""
        if self.head.next == self.tail:
            return None
        tail_node = self.tail.prev
        self.remove(tail_node)
        return tail_node

    def move_to_head(self, node):
        """Move an existing node to the head position (mark as most recently used)."""
        self.remove(node)
        self.add_to_head(node)

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