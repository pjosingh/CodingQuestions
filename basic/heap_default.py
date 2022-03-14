
class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None
        
        def get_prev(self):
            return self.prev

        def set_prev(self, node):
            self.prev = node
        
        def set_next(self, node):
            self.next = node

        def get_next(self):
            return self.next

        def __str__(self) -> str:
            return self.key

class DLL(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        temp = self.head
        res = []
        while temp:
            res.append(temp.key)
            temp = temp.get_next()
        return str(res)
    
    def remove(self, node):
        if node is None:
            return

        if (node == self.head):
            self.head = node.get_next()
            
            if (self.head):
                self.head.set_prev(None)
            
            
        else:
            node.get_prev().set_next(node.get_next())
            if (node.get_next()):
                node.get_next().set_prev(node.get_prev())
        
        if (node == self.tail):
                self.tail = node.get_prev()

    
    def remove_tail(self):
        response = self.tail
        prev = self.tail.get_prev()
        self.remove(self.tail)
        self.tail = prev

        return response

    
    
    def add(self, key, value):
        if self.head is None:
            self.head = Node(key, value)
            self.tail = self.head
            #print("added 1")
        else:
            #self.head.prev = node
            added = Node(key, value)
            self.head.set_prev(added)
            added.set_next(self.head)
            self.head = added

        return self.head

class FreqStack:

    def __init__(self):
        self.mapping = {}
        self.dll = DLL()
        self.freq = {}

    def push(self, val: int) -> None:
        node = self.dll.add(val, 0)
        list = self.mapping.get(val, [])
        list.append(node)
        self.mapping[val] = list

        current_freq = self.freq.get(val, 0)
        current_freq += 1
        self.freq[val] = current_freq


    def pop(self) -> int:
        

input = ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
values = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]

obj = None
output = []

for i in range(len(input)):
    if input[i] == "FreqStack":
        obj = FreqStack()
        output.append(None)
    elif input[i] == "push":
        obj.push(values[i][0])
        output.append(None)
    elif input[i] == "pop":
        output.append(obj.pop())
    print(f' dll: {obj.dll} freq {obj.freq}')

print(output)