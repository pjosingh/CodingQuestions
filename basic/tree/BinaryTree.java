package basic.tree;

class BinaryTree {
    Node root;

    public void printBinaryTree() {
        if (root == null) {
            System.out.println("There are no nodes in the tree");
            return;
        }

        // TODO : to be implemented

        printInoder(root);
        System.out.println();
    }

    private void printInoder(Node node) {
        if (node == null) {
            return;
        }

        //left
        printInoder(node.left);
        
        //center
        System.out.print(node.data+" ");

        //right
        printInoder(node.right);
    }
}

class Node {
    int data;
    Node left, right;

    public Node(int data) {
        this.data = data;
    }
}