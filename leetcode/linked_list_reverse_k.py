class List(object):
    def __init__(self) -> None:
        self.head = None
        self.rear = None
    def add_rear(self, val):
        node = ListNode(val, None)
        if self.rear is None:
            self.head = node
            self.rear = node
            return
        
        self.rear.next = node
        self.rear = node
    
    def print(self):
        temp = self.head

        while temp:
            print(f'el: {temp.val}')
            temp = temp.next

    

class ListNode(object):
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def convert_to_list(self, head):

        temp = head
        res = []
        while temp:
            res.append(temp.val)
            temp = temp.next
        return res
        
    
    
    

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        count = 0
        temp = head
        prev = None
        next = head
        while count<k and next:
            temp = next
            next = next.next
            temp.next = prev
            prev = temp
            count +=1 
        if next:
            temp = next.next
            

        
        print(f' temp {temp.val} prev: {prev.val}')

        return None

    def call(self, nums, k):
        list = List()
        
        for el in nums:
            list.add_rear(el)
        list.print()
        reversed = self.reverseKGroup(list.head, k)
        node = ListNode()
        return node.convert_to_list(reversed)


assert Solution().call([1,2,3,4,5], 2) == [2,1,4,3,5]
        




