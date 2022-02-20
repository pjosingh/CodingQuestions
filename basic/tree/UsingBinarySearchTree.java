package basic.tree;

public class UsingBinarySearchTree {

    public static void main(String ar[]) {


        System.out.println("\n\n\n\n\t\tUsingBinarySearchTree....");

        BinarySearchTree binarySearchTree = new BinarySearchTree();
        // binarySearchTree.insert(10);
        // binarySearchTree.insert(15);
        // binarySearchTree.insert(20);
        // binarySearchTree.insert(5);
        // binarySearchTree.insert(7);
        // binarySearchTree.insert(9);

        binarySearchTree.insert(10);
        binarySearchTree.insert(15);
        binarySearchTree.insert(7);
        binarySearchTree.insert(20);
        binarySearchTree.insert(5);
        binarySearchTree.insert(9);
        

        binarySearchTree.print();
    }
    
}
