import random
class RandomizedSet:

    def __init__(self):
        self._mapping = {}
        self._arr = []

    def print(self):
        print(f'mapping: {self._mapping}  arr: {self._arr}')

    def insert(self, val: int) -> bool:
        if val in self._mapping:
            return False
        else:
            self._arr.append(val)
            self._mapping[val] = len(self._arr)-1
            return True

    def remove(self, val: int) -> bool:
        if val not in self._mapping:
            return False
        else:
            index = self._mapping[val]
            del(self._mapping[val])
            
            if len(self._arr) == 1:
                del(self._arr[index])
                return True

            self._arr[index] = self._arr[len(self._arr)-1]
            self._mapping[self._arr[index]] = index
            del(self._arr[len(self._arr)-1])
            return True

    def getRandom(self) -> int: 
        if len(self._arr) == 1:
            return self._arr[0]
        else:
            ran = self.getRandomNumber()
            return self._arr[ran]

    def getRandomNumber(self) -> int:
        return random.randint(0, len(self._arr)-1)


ran = RandomizedSet()
ran.insert(0)
ran.print()
ran.insert(1)
ran.print()
ran.remove(0)
ran.print()
ran.insert(2)
ran.print()
ran.remove(1)
ran.print()
print(ran.getRandom())