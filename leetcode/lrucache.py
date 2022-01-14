class LRUCache(object):


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dll = DLL()
        self.map = {}
    
    def print_cache(self):
        print("\t Printing cache")
        temp = self.dll.head
        while temp:
            print("\t ", temp.key, temp.value, temp.prev, temp.next)
            temp = temp.get_next()
        print(self.map)
        print("\n\n=====")

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            
            self.dll.remove(self.map[key])
            added_node = self.dll.add(self.map[key].key, self.map[key].value)
            self.map[key] = added_node
            return self.map[key].value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            # element already exists in the cache
            # evict only if capacity constraint is reached, which will not happen in this case 
            self.map[key].value = value
            self.get(key)
            return
        
        if len(self.map) == self.capacity:
            removed = self.dll.remove_tail()
            del self.map[removed.key]
            print("Capacity reached, removing item -> ", removed.key, removed.value)
            
        #print("Adding : ", key, value)
        added = self.dll.add(key, value)
        self.map[key] = added
        #print("\tMap: ", self.map)
        
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

class DLL(object):
    def __init__(self):
        self.head = None
        self.tail = None

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


cache = LRUCache(2)
cache.put(2,1)
cache.print_cache()

cache.put(1,1)
cache.print_cache()

cache.put(2,3)
cache.print_cache()

cache.put(4,1)
cache.print_cache()

print("get", cache.get(1))
cache.print_cache()
print("get", cache.get(2))
cache.print_cache()