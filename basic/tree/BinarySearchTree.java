package basic.tree;


/**
 * print in inorder way, and get sorted list
 * 
 */
public class BinarySearchTree {
    BSTNode root;
    
    // insertion
    public void insert(int data) {
        
        // this means, i am adding to the binary search tree for the first time
        if (root == null) {
            root = new BSTNode(data);
            return;
        }
        insertUtil(data, root);
    } 

    // 20, Node(15)
    private BSTNode insertUtil(int data, BSTNode node) {
        
        if (node == null) {
            return new BSTNode(data);
        }

        if (data > node.data) {
            node.right = insertUtil(data, node.right);
        } else {
            node.left = insertUtil(data, node.left);
        }
        return node;
    }

    // searching
    

    // printing

    public void print() {
        if (root == null) {
            System.out.println("There is no data in the tree");

        }


        printInOrder(root);
    }

    private void printInOrder(BSTNode node) {
        if (node == null) {
            return;
        }


        printInOrder(node.left);
        System.out.println(node.data);
        printInOrder(node.right);

    }
}

class BSTNode {
    int data;
    BSTNode left, right;

    public BSTNode(int data) {
        this.data = data;
    }
}
