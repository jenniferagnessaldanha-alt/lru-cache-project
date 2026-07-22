# LRU Cache Project

An LRU (Least Recently Used) Cache implemented from scratch using a hash table +
doubly linked list, achieving O(1) time complexity for both `get` and `put`.

Built as a DSA practice project for Google STEP interview prep.

## Status
- [✔️] Day 1 — Doubly linked list with sentinel nodes
- [✔️] Day 2 — Basic get/put logic
- [✔️] Day 3 — Eviction logic
- [✔️] Day 4 — Full test suite
- [✔️] Day 5 — Naive O(n) baseline cache
- [✔️] Day 6 — Benchmarking (LRU vs naive)
- [✔️] Day 7 — Extension feature
- [✔️] Day 8 — Java reimplementation
- [✔️] Day 9 — Documentation
- [✔️] Day 10 — Polish

## How to Run

```bash
# Run all tests
pytest tests/ -v

# Run benchmark
python benchmark/benchmark.py
```

## Project structure

```
lru-cache-project/
├── src/                    Python implementation (linked_list, lru_cache, naive_cache)
├── tests/                  pytest test suites
├── benchmark/              LRU vs naive timing comparison
├── java/                   Java reimplementation + test harness
├── requirements.txt
└── README.md
```

## Design (fill in as you build)
- **Hash table**: maps key -> Node, gives O(1) lookup
- **Doubly linked list**: maintains recency order, gives O(1) reordering/eviction
- **Sentinel nodes**: dummy head/tail nodes avoid null-checks at list boundaries
### Why a doubly linked list + hash map?

The hash map gives O(1) lookup by key, but a plain dict has no concept of
"order" — you can't cheaply find or update the least-recently-used entry.
The doubly linked list gives O(1) reordering (move a node to the front,
or drop the last node) but O(n) lookup by key on its own.

Combining them: the dict stores `key -> Node`, so lookup is O(1), and the
node itself lives in the linked list, so once you have it, moving it to
the front or evicting it is also O(1). Neither structure alone is enough
— together they cover both requirements.
### Why sentinel head/tail nodes instead of `None` boundaries?

Without sentinels, `add_to_head`/`remove` need special-case branches for
"is the list currently empty?" and "am I removing the only node?". With
sentinel nodes, `head` and `tail` always exist and are always linked to
something real (each other, if the list is empty), so every node -
including the first one ever added - has a real `.prev` and `.next` to
rewire. This removes an entire category of edge-case bugs.

### Benchmark results

Capacity  LRU put (s)    Naive put (s)  LRU get (s)    Naive get (s)
----------------------------------------------------------------------
100       0.00261        0.00201        0.00160        0.00375
1000      0.00513        0.00867        0.00143        0.02807
5000      0.00315        0.01562        0.00237        0.14722

The `get` columns show the clearest picture: LRUCache stays roughly flat
as capacity grows, while NaiveCache's time grows sharply (~40x slower at
capacity 5000), confirming the O(1) vs O(n) difference in practice.

## Java port

`java/` contains a parallel implementation of the same LRUCache in Java,
built to compare the same algorithm across languages. Compile and run
with:

\`\`\`bash
cd java
javac Node.java DoublyLinkedList.java LRUCache.java LRUCacheTest.java
java -ea LRUCacheTest
\`\`\`


## Complexity

| Operation | Time | Space |
|---|---|---|
| get | O(1) | O(capacity) |
| put | O(1) | O(capacity) |

### Complexity by cache type

| Operation      | LRUCache | NaiveCache |
|----------------|----------|------------|
| `get` (hit)    | O(1)     | O(n)       |
| `get` (miss)   | O(1)     | O(1)       |
| `put` (new)    | O(1)     | O(1)       |
| `put` (update) | O(1)     | O(n)       |
| `put` (evict)  | O(1)     | O(n)       |

## Real-world applications
- Browser cache
- Database query cache
- OS page replacement algorithm
