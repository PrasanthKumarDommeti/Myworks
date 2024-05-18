public class Main {
    static class Node {
        //Structure of the Node
        int value;
        Node next;
        // The node is a method
        Node(int val) {
            value = val;
            next = null;
        }
    }

    public static void main(String[] args) {
        // Creating head of the Linked list
        Node head = new Node(1);
        System.out.println("The value at head is " + head.value);
    }
}
