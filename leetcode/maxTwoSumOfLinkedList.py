# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # at this point slow points to median
        max = 0

        while slow != None:
            sum = slow.val + head.val
            max = max(sum, max)
            slow = slow.next
            head = head.next
        
        return max

sol = Solution()
sol.pairSum([5,4,2,1])