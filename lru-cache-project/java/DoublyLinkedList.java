public class DoublyLinkedList {
    Node head;
    Node tail;
    int size;

    public DoublyLinkedList() {
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
        size = 0;
    }

    public void addToHead(Node node) {
        Node oldFirst = head.next;
        node.prev = head;
        node.next = oldFirst;
        head.next = node;
        oldFirst.prev = node;
        size++;
    }

    public void remove(Node node) {
        Node prevNode = node.prev;
        Node nextNode = node.next;
        prevNode.next = nextNode;
        nextNode.prev = prevNode;
        node.prev = null;
        node.next = null;
        size--;
    }

    public Node removeTail() {
        if (head.next == tail) {
            return null;
        }
        Node tailNode = tail.prev;
        remove(tailNode);
        return tailNode;
    }

    public void moveToHead(Node node) {
        remove(node);
        addToHead(node);
    }
}