'''
Tree (Binary tree, N-Array Tree)
Basic algorithms - inorder traversal, post-order, pre-order traversal

Binary Search Tree (BST)
Basic algorithms - 
inorder traversal - sorted manner

Binary search tree 


sorted list: [1,2,3,4,5,6,7,8,9]

[6,7,8,9]


[8,9]

8

number of comparisons: 5, 7, 8 - 3 (time complexity is less here)
old method: 1,2,3,4,5,6,7,8  - 8 (time complexity is more here)


Two child- binary tree
Three child -ternary tree 
N-child - N-ary tree

Binary tree - Complete binary tree, incomplete binary tree
Green - leave node
Red - Root node

Binary Tree- Data structure , traversal, what are usages of binary tree?
Binary Search Tree- Data structure , traversal, what are usages of binary tree?


'''
import time

class Solution(object):
    
    '''
    search a elementn in a list
    Time complexity: i have to go through all elements to find a element at max
    Space complexity:
    '''
    def search1(self, nums, target):
        
        for el in nums:
            print(el)
            time.sleep(1)
            if el == target:
                print("Number found")
                return

        print("Number not found")
            



object = Solution()
#object.search1([1,2,3,4,5,6,7,8,9], 8)
object.search1([1,2,3,4,5,6,7,8,9], 100)