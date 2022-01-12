
class OnePointFour:
    def __init__(self) -> None:
        pass

    # check two strings if they are anagrams 
    def check(self, string1, string2):
        
        print(sorted(string1))
        print(sorted(string2))
        return sorted(string1) == sorted(string2)


one = OnePointFour()
print(one.check("abc","cba"))
print(one.check("abc","cbaa"))
print(one.check("abc","pqr"))
