
class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree(object):

    def __init__(self) -> None:
        super().__init__()
        self.root = None
        self.__testing = "Hello world"

    def inorder(self):
        self.__inorderUtil(self.root)

    def __inorderUtil(self, root):
        if root:
            self.__inorderUtil(root.left)
            print(root.value)
            self.__inorderUtil(root.right)

    def check_balanced(self):
        if self.max_h(self.root) - self.min_h(self.root) == 1:
            return True
        else:
            return False

    def max_h(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.max_h(root.left), self.max_h(root.right))
    
    def min_h(self, root):
        if root is None:
            return 0
        else:
            return 1 + min(self.min_h(root.left), self.min_h(root.right))
    #def isBalanced(self):

## Testing 

tree = Tree()
tree.root = TreeNode(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.right.left = TreeNode(4)
tree.root.right.left.right = TreeNode(5)
tree.inorder()
print(tree.check_balanced())