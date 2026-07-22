import java.util.HashMap;

public class LRUCache {
    private int capacity;
    private HashMap<Integer, Node> map;
    private DoublyLinkedList list;
    private int hits;
    private int misses;

    public LRUCache(int capacity) {
        if (capacity <= 0) {
            throw new IllegalArgumentException("capacity must be a positive integer");
        }
        this.capacity = capacity;
        this.map = new HashMap<>();
        this.list = new DoublyLinkedList();
        this.hits = 0;
        this.misses = 0;
    }

    public int size() {
        return map.size();
    }

    public int get(int key) {
        if (!map.containsKey(key)) {
            misses++;
            return -1;
        }
        Node node = map.get(key);
        list.moveToHead(node);
        hits++;
        return node.value;
    }

    public void put(int key, int value) {
        if (map.containsKey(key)) {
            Node node = map.get(key);
            node.value = value;
            list.moveToHead(node);
            return;
        }

        Node node = new Node(key, value);
        map.put(key, node);
        list.addToHead(node);

        if (map.size() > capacity) {
            Node lruNode = list.removeTail();
            map.remove(lruNode.key);
        }
    }

    public double hitRate() {
        int total = hits + misses;
        if (total == 0) {
            return 0.0;
        }
        return (double) hits / total;
    }
}