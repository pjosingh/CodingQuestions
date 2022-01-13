# check if string has duplicate
class OnePointOne:
    def __init__(self) -> None:
        pass

    def check(self, target):
        target = sorted(target)        
        prev = None
        for char in target:
            if prev:
                if prev == char:
                    return True
            prev = char

        return False

one = OnePointOne()
print(one.check("abc"))
print(one.check("aabc"))
print(one.check("abcaaa"))