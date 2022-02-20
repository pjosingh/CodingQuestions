package basic.tree;

public class UsingBinaryTree {

    public static void main(String ar[]) {
        System.out.println("Hello world");
        BinaryTree obj = new BinaryTree();
        obj.root = new Node(1);
        obj.root.left = new Node(2);
        obj.root.right = new Node(3);
        obj.root.left.left = new Node(4);
        obj.root.right.left = new Node(6);
        obj.root.right.right = new Node(7);

        obj.printBinaryTree();
    }
    
}
