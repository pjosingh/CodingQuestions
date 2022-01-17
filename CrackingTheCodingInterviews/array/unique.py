

def uniqChars(target):
    map = {}

    for el in range(len(target)):
        if target[el] in map:
            return False
        map[target[el]] = True
    return True


# testing
print(uniqChars("helo"))
print(uniqChars("hello"))
