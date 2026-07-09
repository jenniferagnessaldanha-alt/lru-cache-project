"""
DAY 1 TASKS: write tests for DoublyLinkedList.
Run with: pytest tests/test_linked_list.py -v
"""

import pytest
from src.linked_list import DoublyLinkedList, Node


def test_add_to_head_single_node():
    dll = DoublyLinkedList()
    n1 = Node(1, "a")
    dll.add_to_head(n1)
    assert dll.to_list() == [1]


def test_add_to_head_multiple_nodes_order():
    dll = DoublyLinkedList()
    n1, n2, n3 = Node(1, "a"), Node(2, "b"), Node(3, "c")
    dll.add_to_head(n1)
    dll.add_to_head(n2)
    dll.add_to_head(n3)
    # most recently added should be closest to head
    assert dll.to_list() == [3, 2, 1]


def test_remove_middle_node():
    dll = DoublyLinkedList()
    n1, n2, n3 = Node(1, "a"), Node(2, "b"), Node(3, "c")
    dll.add_to_head(n1)
    dll.add_to_head(n2)
    dll.add_to_head(n3)
    dll.remove(n2)
    assert dll.to_list() == [3, 1]


def test_move_to_head():
    dll = DoublyLinkedList()
    n1, n2, n3 = Node(1, "a"), Node(2, "b"), Node(3, "c")
    dll.add_to_head(n1)
    dll.add_to_head(n2)
    dll.add_to_head(n3)
    dll.move_to_head(n1)
    assert dll.to_list() == [1, 3, 2]


def test_remove_tail_returns_least_recent():
    dll = DoublyLinkedList()
    n1, n2 = Node(1, "a"), Node(2, "b")
    dll.add_to_head(n1)
    dll.add_to_head(n2)
    removed = dll.remove_tail()
    assert removed.key == 1
    assert dll.to_list() == [2]


def test_remove_tail_on_empty_list_does_not_crash():
    dll = DoublyLinkedList()
    result = dll.remove_tail()
    assert result is None
