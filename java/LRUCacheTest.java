public class LRUCacheTest {

    public static void main(String[] args) {
        testRejectsZeroCapacity();
        testRejectsNegativeCapacity();
        testStartsEmpty();
        testGetMissingKeyReturnsNegativeOne();
        testPutThenGet();
        testPutUpdatesExistingKey();
        testEvictionAtCapacity();
        testGetRefreshesRecency();
        testPutOnExistingKeyRefreshesRecency();
        testCapacityOne();
        testHitRateTracking();

        System.out.println("All tests passed!");
    }

    static void testRejectsZeroCapacity() {
        try {
            new LRUCache(0);
            throw new AssertionError("Expected IllegalArgumentException for capacity 0");
        } catch (IllegalArgumentException e) {
            System.out.println("PASS: testRejectsZeroCapacity");
        }
    }

    static void testRejectsNegativeCapacity() {
        try {
            new LRUCache(-5);
            throw new AssertionError("Expected IllegalArgumentException for negative capacity");
        } catch (IllegalArgumentException e) {
            System.out.println("PASS: testRejectsNegativeCapacity");
        }
    }

    static void testStartsEmpty() {
        LRUCache cache = new LRUCache(3);
        assert cache.size() == 0;
        System.out.println("PASS: testStartsEmpty");
    }

    static void testGetMissingKeyReturnsNegativeOne() {
        LRUCache cache = new LRUCache(2);
        assert cache.get(99) == -1;
        System.out.println("PASS: testGetMissingKeyReturnsNegativeOne");
    }

    static void testPutThenGet() {
        LRUCache cache = new LRUCache(2);
        cache.put(1, 100);
        assert cache.get(1) == 100;
        System.out.println("PASS: testPutThenGet");
    }

    static void testPutUpdatesExistingKey() {
        LRUCache cache = new LRUCache(2);
        cache.put(1, 100);
        cache.put(1, 200);
        assert cache.get(1) == 200;
        assert cache.size() == 1;
        System.out.println("PASS: testPutUpdatesExistingKey");
    }

    static void testEvictionAtCapacity() {
        LRUCache cache = new LRUCache(2);
        cache.put(1, 10);
        cache.put(2, 20);
        cache.put(3, 30);  // evicts key 1
        assert cache.get(1) == -1;
        assert cache.get(2) == 20;
        assert cache.get(3) == 30;
        System.out.println("PASS: testEvictionAtCapacity");
    }

    static void testGetRefreshesRecency() {
        LRUCache cache = new LRUCache(2);
        cache.put(1, 10);
        cache.put(2, 20);
        cache.get(1);       // 1 is now most recently used
        cache.put(3, 30);   // evicts 2, not 1
        assert cache.get(1) == 10;
        assert cache.get(2) == -1;
        assert cache.get(3) == 30;
        System.out.println("PASS: testGetRefreshesRecency");
    }

    static void testPutOnExistingKeyRefreshesRecency() {
        LRUCache cache = new LRUCache(2);
        cache.put(1, 10);
        cache.put(2, 20);
        cache.put(1, 999);  // refreshes 1's recency
        cache.put(3, 30);   // evicts 2, not 1
        assert cache.get(1) == 999;
        assert cache.get(2) == -1;
        assert cache.get(3) == 30;
        System.out.println("PASS: testPutOnExistingKeyRefreshesRecency");
    }

    static void testCapacityOne() {
        LRUCache cache = new LRUCache(1);
        cache.put(1, 10);
        cache.put(2, 20);  // evicts 1 immediately
        assert cache.get(1) == -1;
        assert cache.get(2) == 20;
        System.out.println("PASS: testCapacityOne");
    }

    static void testHitRateTracking() {
        LRUCache cache = new LRUCache(2);
        cache.put(1, 10);
        cache.get(1);   // hit
        cache.get(2);   // miss
        cache.get(1);   // hit
        assert cache.hitRate() == 2.0 / 3.0;
        System.out.println("PASS: testHitRateTracking");
    }
}