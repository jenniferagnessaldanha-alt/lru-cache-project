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

    def __init__(self):
        self.head = Node()  # sentinel, no real data
        self.tail = Node()  # sentinel, no real data
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def __len__(self):
        """Returns the current number of elements in the list."""
        return self.size

    def __str__(self):
        """Returns a user-friendly string representation of the list."""
        nodes = []
        current = self.head.next
        while current != self.tail:
            nodes.append(f"({current.key}: {current.value})")
            current = current.next
        return " -> ".join(nodes) if nodes else "Empty List"

    def __repr__(self):
        """Returns an unambiguous string representation for debugging."""
        return f"DoublyLinkedList(size={self.size}, items={self.__str__()})"
    def add_to_front(self, node):
        """Insert `node` right after the head sentinel (most recently used position)."""
        old_first=self.head.next
        node.prev=self.head
        node.next=old_first

        self.head.next=node
        old_first.prev=node
        self.size += 1
        

    def remove(self, node):
        """Unlink `node` from wherever it currently is in the list."""
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node
        node.prev=None
        node.next=None
        self.size -= 1
        

    def remove_last(self):
        """
        Remove and return the node just before the tail sentinel
        (the least recently used real node). Returns None if list is empty.
        """
        if self.head.next==self.tail:
            return None
        tail_node=self.tail.prev
        self.remove(tail_node)
        return tail_node
        

    def move_to_front(self, node):
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
    def get(self, key):
    if key not in self._map:
        return -1
    node = self._map[key]
    self._list.move_to_front(node)
    return node.value
