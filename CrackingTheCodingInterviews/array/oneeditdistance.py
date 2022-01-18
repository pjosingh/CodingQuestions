# insert, remove, replace 

def check(source, target):
    # check if target is one edit distance away from source 
    print(source, target)
    return find_edit_distance(source, target, 0, 0, 0)

def find_edit_distance(source, target, count, index_source, index_target) -> int:
    if (count > 1):
        print(99)
        return 99
    print(source, target, count, index_source, index_target)

    if source == target:
        print(count)
        return count
   
    
    if source[index_source] == target[index_target]:
        index_source += 1
        index_target += 1
        find_edit_distance(source, target, count, index_source, index_target)
    elif source[index_source] != target[index_target]:
        # insert
        min (find_edit_distance( source[0:index_source]+source[index_source+1:], target, count+1 , index_source, index_target),
                find_edit_distance( source[0:index_source]+target[index_target]+source[index_source+1:], target, count+1, index_source+1, index_target),
                find_edit_distance( source[0:index_source]+target[index_target]+source[index_source:], target, count+1, index_source+1, index_target))


## testing 

print(check("ple", "pale"))
#print(check("pale","pale"))