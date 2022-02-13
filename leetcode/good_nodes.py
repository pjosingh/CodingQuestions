from logging import RootLogger


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    count = 0

    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        print("hello")

        # root is always good
        global count
        count = 1 
        self.count_good_nodes(root, root.val)
        print(count)
        return count 

    def count_good_nodes(self, root, current_max):
        global count
        if not root:
            return

        if root.val >= current_max:
            count += 1
            current_max = root.val

        self.count_good_nodes(root.left, current_max)
        self.count_good_nodes(root.right, current_max)

        


sol = Solution()

assert sol.goodNodes([3,1,4,3,None,1,5]) == 4

        