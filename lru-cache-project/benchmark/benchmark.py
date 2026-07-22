"""
Benchmark: LRUCache (O(1)) vs NaiveCache (O(n))

Run with:
    python -m benchmark.benchmark
"""

import random
import time

from src.lru_cache import LRUCache
from src.naive_cache import NaiveCache


def run_put_trial(cache_cls, capacity, num_operations):
    """Time `num_operations` put() calls, with keys wide enough to force evictions."""
    cache = cache_cls(capacity)
    keys = [random.randint(0, capacity * 4) for _ in range(num_operations)]

    start = time.perf_counter()
    for key in keys:
        cache.put(key, key)
    end = time.perf_counter()

    return end - start


def run_get_trial(cache_cls, capacity, num_operations):
    """Pre-populate a cache, then time `num_operations` get() calls against it."""
    cache = cache_cls(capacity)
    for i in range(capacity):
        cache.put(i, i)

    keys = [random.randint(0, capacity - 1) for _ in range(num_operations)]

    start = time.perf_counter()
    for key in keys:
        cache.get(key)
    end = time.perf_counter()

    return end - start


def main():
    sizes = [100, 1000, 5000]
    num_operations = 5000

    print(f"{'Capacity':<10}{'LRU put (s)':<15}{'Naive put (s)':<15}{'LRU get (s)':<15}{'Naive get (s)':<15}")
    print("-" * 70)

    for capacity in sizes:
        lru_put = run_put_trial(LRUCache, capacity, num_operations)
        naive_put = run_put_trial(NaiveCache, capacity, num_operations)
        lru_get = run_get_trial(LRUCache, capacity, num_operations)
        naive_get = run_get_trial(NaiveCache, capacity, num_operations)

        print(f"{capacity:<10}{lru_put:<15.5f}{naive_put:<15.5f}{lru_get:<15.5f}{naive_get:<15.5f}")


if __name__ == "__main__":
    main()