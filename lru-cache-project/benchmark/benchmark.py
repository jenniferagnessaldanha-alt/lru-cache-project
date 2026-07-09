"""
DAY 6 TASKS: benchmark LRUCache vs NaiveCache and plot the results.
Run with: python benchmark/benchmark.py
"""

import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.lru_cache import LRUCache
from src.naive_cache import NaiveCache

# import matplotlib only when actually plotting (Day 6)
# import matplotlib.pyplot as plt


def time_cache(cache_class, num_ops, capacity=1000):
    """Run num_ops put/get operations on the given cache and return elapsed time."""
    # TODO (Day 6): implement timing loop using time.perf_counter()
    raise NotImplementedError


def run_benchmark():
    op_counts = [100, 500, 1000, 5000, 10000]
    lru_times = []
    naive_times = []

    for n in op_counts:
        # TODO (Day 6): call time_cache() for both cache types, append results
        pass

    # TODO (Day 6): plot op_counts vs lru_times and naive_times with matplotlib
    # TODO (Day 6): save to benchmark/results.png
    print("Benchmark not yet implemented — see TODOs.")


if __name__ == "__main__":
    run_benchmark()
