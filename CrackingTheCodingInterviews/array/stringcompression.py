def compress(target):
    print("target", target)

    count = 0
    builder = ""
    prev = None
    for el in target:
        if el == prev:
            count +=1
        else:
            prev = el
            if count == 0:
                builder += el
            else:
                builder += prev+str(count)
                count = 0

    print(builder)

compress("aabcccccaaa")