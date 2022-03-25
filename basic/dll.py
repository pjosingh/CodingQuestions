class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None
        self.next = None


class Dll:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def remove(self, node):
        if node == None:
            return
        if self.head == None:
            return
        
        if self.head == self.tail:
            if self.head == node:
                self.head = None
                self.tail = None
            else:
                return
        
        if self.head == node:
            self.head = node.next
        elif self.tail == node:
            self.tail = self.tail.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
    
    def addToFront(self, val):
        node = Node(val)
        if self.head == None:
            # adding for first time
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        return node

    def addToBack(self, val):
        pass

    def print(self):
        if self.head == None:
            print("Empty list")
        else:
            temp  = self.head
            while temp:
                print(temp.val)
                temp = temp.next
            