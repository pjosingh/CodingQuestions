import random
class RandomizedSet:

    def __init__(self):
        self.mapping = {}
        self.stack = []


    def insert(self, val):
        if val in self.mapping:
            return False

        self.stack.append(val)
        self.mapping[val] = len(self.stack)-1

        return True

    
    def remove(self, val):
        if val not in self.mapping:
            return False
        
        index = self.mapping[val]
        del(self.mapping[val])
        self.stack[index] = self.stack[-1]

        if self.stack[index] == val:
            del(self.stack[index])
            return True 
            
        self.mapping[self.stack[index]] = index
        self.stack.pop()
        return True
    
    def getRandom(self) -> int: 
        if len(self.stack) == 1:
            return self.stack[0]
        else:
            ran = self.getRandomNumber()
            if self.stack[ran] != None:
                return self.stack[ran]
            else:
                self.getRandom()

    def getRandomNumber(self) -> int:
        #self.print()
        return random.randint(0, len(self.stack)-1)