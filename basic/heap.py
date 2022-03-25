'''
parent is greater than or equal to all its children 
left child 2k+1 
right child 2k+2
parent - arr[(i-1)/2]
'''

class Heap:
    def __init__(self, maxsize) -> None:
        self.size = 0
        self.maxsize = maxsize
        self.heap = [0]*maxsize

    def parent(self, current):
        return int((current-1)/2)
    def left(self, current):
        return 2*current+1
    def right(self, current):
        return 2*current+2

    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    # o(logN)
    def insert(self, val):
        if self.size >= self.maxsize:
            print(f'Heap full {self.heap}')
            return 
        
        self.heap[self.size] = val
        current = self.size
        while self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

        self.size += 1
    
    def remove(self):
        pass

    # o(1)
    def getMax(self):
        if self.size >=1:
            return self.heap[1]
        return None

    def isLeaf(self, index):
        if  (index > (int(self.size/2))and index <= self.size):
            return True
        return False 
    def maxHeapify(self, index):
        if (self.isLeaf(index)):
            return
        
        if (self.heap[index] < self.heap[self.left(index)] or self.heap[index] < self.heap[self.right(index)]):
            if (self.heap[self.left(index)]) > self.heap[self.right(index)]:

                self.swap(index, self.left(index))
                self.maxHeapify(self.left(index))
            else:
                self.swap(index, self.right(index))
                self.maxHeapify(self.right(index))

    def extractMax(self):
        if self.size >=1:
            popped = self.heap[0]
            self.heap[0] = self.heap[self.size-1]
            self.size -= 1
            self.maxHeapify(0)
            return popped
        return None

    def print(self):
        print(f'heap: {self.heap}')

heap = Heap(15)
heap.insert(5)
heap.insert(3)
heap.insert(17)
heap.insert(10)
heap.insert(84)
heap.insert(19)
heap.insert(6)
heap.insert(22)
heap.insert(9)
heap.print()



print(f'max value: {heap.extractMax()}')
heap.print()