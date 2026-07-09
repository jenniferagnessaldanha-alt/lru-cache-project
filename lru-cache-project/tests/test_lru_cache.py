"""
DAY 3-4 TASKS: write tests for LRUCache eviction and edge cases.
Run with: pytest tests/test_lru_cache.py -v
"""

import pytest
from src.lru_cache import LRUCache


def test_basic_put_get():
    cache = LRUCache(2)
    cache.put(1, "a")
    assert cache.get(1) == "a"


def test_get_missing_key_returns_negative_one():
    cache = LRUCache(2)
    assert cache.get(99) == -1


def test_update_existing_key_updates_value():
    cache = LRUCache(2)
    cache.put(1, "a")
    cache.put(1, "b")
    assert cache.get(1) == "b"


def test_eviction_removes_least_recently_used():
    cache = LRUCache(2)
    cache.put(1, "a")
    cache.put(2, "b")
    cache.get(1)          # 1 is now most recently used
    cache.put(3, "c")     # should evict 2, not 1
    assert cache.get(2) == -1
    assert cache.get(1) == "a"
    assert cache.get(3) == "c"


def test_capacity_one():
    cache = LRUCache(1)
    cache.put(1, "a")
    cache.put(2, "b")     # evicts 1
    assert cache.get(1) == -1
    assert cache.get(2) == "b"


def test_capacity_zero_stores_nothing():
    cache = LRUCache(0)
    cache.put(1, "a")
    assert cache.get(1) == -1


def test_large_sequence_of_operations():
    cache = LRUCache(3)
    for i in range(100):
        cache.put(i, i * 10)
    # only the last 3 keys should remain
    assert cache.get(97) == 970
    assert cache.get(98) == 980
    assert cache.get(99) == 990
    assert cache.get(50) == -1
