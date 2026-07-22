import pytest

from src.lru_cache import LRUCache


class TestConstruction:
    def test_rejects_zero_capacity(self):
        with pytest.raises(ValueError):
            LRUCache(0)

    def test_rejects_negative_capacity(self):
        with pytest.raises(ValueError):
            LRUCache(-5)

    def test_starts_empty(self):
        cache = LRUCache(3)
        assert len(cache) == 0


class TestBasicGetPut:
    def test_get_missing_key_returns_negative_one(self):
        cache = LRUCache(2)
        assert cache.get("missing") == -1

    def test_put_then_get(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        assert cache.get("a") == 1

    def test_put_updates_existing_key(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("a", 2)
        assert cache.get("a") == 2
        assert len(cache) == 1  # still only one entry

    def test_multiple_keys(self):
        cache = LRUCache(3)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)
        assert cache.get("a") == 1
        assert cache.get("b") == 2
        assert cache.get("c") == 3


class TestEviction:
    def test_eviction_at_capacity(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)  # should evict "a" (least recently used)
        assert cache.get("a") == -1
        assert cache.get("b") == 2
        assert cache.get("c") == 3
        assert len(cache) == 2

    def test_get_refreshes_recency(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.get("a")       # "a" is now most recently used; "b" is LRU
        cache.put("c", 3)    # should evict "b", not "a"
        assert cache.get("a") == 1
        assert cache.get("b") == -1
        assert cache.get("c") == 3

    def test_put_on_existing_key_refreshes_recency(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("a", 10)   # updating "a" should refresh its recency
        cache.put("c", 3)    # should evict "b", not "a"
        assert cache.get("a") == 10
        assert cache.get("b") == -1
        assert cache.get("c") == 3

    def test_capacity_one(self):
        cache = LRUCache(1)
        cache.put("a", 1)
        cache.put("b", 2)  # evicts "a" immediately
        assert cache.get("a") == -1
        assert cache.get("b") == 2
        assert len(cache) == 1

    def test_repeated_eviction_under_sustained_load(self):
        cache = LRUCache(3)
        for i in range(10):
            cache.put(f"key{i}", i)
        # only the last 3 keys should survive
        for i in range(7):
            assert cache.get(f"key{i}") == -1
        for i in range(7, 10):
            assert cache.get(f"key{i}") == i
        assert len(cache) == 3


class TestRecencyOrderingIntegration:
    def test_interleaved_get_and_put_sequence(self):
        # Mirrors the classic LeetCode 146 walkthrough example.
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1        # recency: 1, 2
        cache.put(3, 3)                  # evicts 2 -> recency: 3, 1
        assert cache.get(2) == -1
        cache.put(4, 4)                  # evicts 1 -> recency: 4, 3
        assert cache.get(1) == -1
        assert cache.get(3) == 3
        assert cache.get(4) == 4


class TestHitRateTracking:
    def test_starts_at_zero(self):
        cache = LRUCache(2)
        assert cache.hits == 0
        assert cache.misses == 0
        assert cache.hit_rate() == 0.0

    def test_hit_and_miss_counted_correctly(self):
        cache = LRUCache(2)
        cache.put(1, "a")
        cache.get(1)       # hit
        cache.get(2)       # miss
        cache.get(1)       # hit
        assert cache.hits == 2
        assert cache.misses == 1
        assert cache.hit_rate() == 2 / 3

    def test_put_does_not_affect_hit_rate(self):
        cache = LRUCache(2)
        cache.put(1, "a")
        cache.put(2, "b")
        cache.put(3, "c")  # triggers eviction, but no get() calls yet
        assert cache.hits == 0
        assert cache.misses == 0
        