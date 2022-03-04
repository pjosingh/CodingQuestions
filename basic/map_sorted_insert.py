

def check_sorted_insert(target):

    
    map = {}
    map[tuple(sorted(target))] = True
    print(map)
    print(map.get(tuple(sorted(target)), False))
    #str(tuple(sorted(target)))
    

def update(map:dict, target):
    tup = tuple(sorted(target))
    print(map, target)
    if tup in map:
        print(map[tup])
        out = map[tup]
        out.append(target)

        map[tup] = out
        
    else:
        map[tup] = [target]
    print("\t"+str(map))

def main():

    map = {}
    
    update(map, "ate")
    update(map, "eat")

    print(map)


# assert check_sorted_insert("eat") == None
# assert check_sorted_insert("eeat") == None
assert main() == None