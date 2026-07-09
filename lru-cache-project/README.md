# LRU Cache Project

An LRU (Least Recently Used) Cache implemented from scratch using a hash table +
doubly linked list, achieving O(1) time complexity for both `get` and `put`.

Built as a DSA practice project for Google STEP interview prep.

## Status
- [ ] Day 1 — Doubly linked list with sentinel nodes
- [ ] Day 2 — Basic get/put logic
- [ ] Day 3 — Eviction logic
- [ ] Day 4 — Full test suite
- [ ] Day 5 — Naive O(n) baseline cache
- [ ] Day 6 — Benchmarking (LRU vs naive)
- [ ] Day 7 — Extension feature
- [ ] Day 8 — Java reimplementation
- [ ] Day 9 — Documentation
- [ ] Day 10 — Polish

## How to Run

```bash
# Run all tests
pytest tests/ -v

# Run benchmark
python benchmark/benchmark.py
```

## Design (fill in as you build)
- **Hash table**: maps key -> Node, gives O(1) lookup
- **Doubly linked list**: maintains recency order, gives O(1) reordering/eviction
- **Sentinel nodes**: dummy head/tail nodes avoid null-checks at list boundaries

## Complexity
| Operation | Time | Space |
|---|---|---|
| get | O(1) | O(capacity) |
| put | O(1) | O(capacity) |

## Real-world applications
- Browser cache
- Database query cache
- OS page replacement algorithm
