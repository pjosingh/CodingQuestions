from re import L


def check_sorted_insert(target):

    
    map = {}
    map[tuple(sorted(target))] = True
    print(map)
    print(map.get(tuple(sorted(target)), False))
    return str(tuple(sorted(target)))



assert check_sorted_insert("eat") == "aet"