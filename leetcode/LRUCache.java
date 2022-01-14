package leetcode;
class MyDLL <T> {

    static class Node {
        Node prev, next;
        int key;
        int value;

        public Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    private Node head;
    private Node tail;
    private int size = 0;

    public void print() {
        Node temp = head;
        while (temp != null) {
            System.out.printf("[%d, %d] -> ", temp.key,  temp.value);
            temp = temp.next;
        }
        System.out.println();
    }
    public void add(Node node) {
        //Node node = new Node(key, value);

        if (head == null) {
            head = node;
            tail = node;

        } else {
            tail.next = node;
            node.prev = tail;
            tail = node;
        }
        size++;
    }

    public Node get() {
        return head;
    }


//     public void remove (Node node) {
//         if (node.prev != null) {
//             node.prev.next = node.next;
            
//         }
        
//         if (node.next != null) {
//             node.next.prev = node.prev;
//         }
        
//         if (node.prev == null) {
//             head = node.next;
//         }
        
//         if (node.next == null) {
//             tail = node.prev;
//         }
//         size --;
//     }
    
    public void remove (Node node) {
        // case its empty list 
        
        // -> this cannot happen as Node exists
        
        // just one node
        
        if (head == node && node == tail) {
            head = null;
            tail = null;
            
        }
        
        // case: its head of the list 
        else if ( node == head && node != tail) {
            head = head.next;
            head.prev = null;
            
            // A B <- head
            
        } 
        // case: its tail of the list 
        else if (node == tail && node != head) {
            tail = tail.prev;
            tail.next = null;
        }
        
        // case: its in the middle of the list 
        else {
            node.prev.next = node.next;
            node.next.prev = node.prev;
        }
        
        
        size --;
    }
    

    public int size() {
        return size;
    }
}


public class LRUCache {

    //private List<Pair> queue;
    private MyDLL<MyDLL.Node> queue;

    private Map<Integer, MyDLL.Node> map;
    private int capacity;

    // size 2
    public LRUCache(int capacity) {

        this.capacity = capacity;
        this.map = new HashMap<>();
        //this.queue = new LinkedList<>();
        this.queue = new MyDLL<>();
    }

    public int get(int key) {

        if (map.get(key) == null) {
            // element doesn't exist in the cache
            return -1;
        }
        MyDLL.Node pair = map.get(key);
        queue.remove(pair);
        queue.add(pair);
        return pair.value;
    }

    public void put(int key, int value) {
        if (queue.size() == capacity) {

            if (map.get(key) == null) {
                MyDLL.Node first = queue.get();
                queue.remove(first);
                map.remove(first);
                map.remove(first.key, first);
                System.out.printf("Removed %d with value %d\n" , first.key, first.value);

                print();
                System.out.println("Capacity fixed");
            }
        }

        if (map.get(key) != null) {
            MyDLL.Node removeThis = map.get(key);
            map.remove(key);
            queue.remove(removeThis);
        }

        MyDLL.Node pair = new MyDLL.Node(key, value);
        queue.add(pair);
        map.put(key, pair);
        print();
    }

    private void print() {
        System.out.println("Map");

        for (Integer key: map.keySet()) {
            System.out.printf("map[%d] -> [%d,%d]\n", key, map.get(key).key, map.get(key).value);
        }
        System.out.println();

        System.out.println("Queue");
        queue.print();
        System.out.println();
        System.out.println();
    }
}
