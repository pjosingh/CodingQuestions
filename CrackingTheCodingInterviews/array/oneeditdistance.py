# insert, remove, replace 

def check(source, target):
    # check if target is one edit distance away from source 
    print(source, target)
    dis = find_edit_distance(source, target, 0, 0, 0)
    if dis <=1:
        return True
    else:
        return False


def find_edit_distance(source, target, count, index_source, index_target) -> int:
    if (count > 1):
        #print(99)
        return 99
    #print(source, target, count, index_source, index_target)

    if source == target:
        #print(count)
        return count
   
    if source != target and (index_target == len(target) or index_source == len(source)):
        return 99
    if source[index_source] == target[index_target]:
        index_source += 1
        index_target += 1
        return find_edit_distance(source, target, count, index_source, index_target)
    elif source[index_source] != target[index_target]:
        # insert

        # print("Result:", source[0:index_source]+source[index_source+1:], target, count+1 , index_source, index_target, find_edit_distance( source[0:index_source]+source[index_source+1:], target, count+1 , index_source, index_target))
        # print("Result:", source[0:index_source]+target[index_target]+source[index_source+1:], target, count+1, index_source+1, index_target, find_edit_distance( source[0:index_source]+target[index_target]+source[index_source+1:], target, count+1, index_source+1, index_target))
        # print("Result:", source[0:index_source]+target[index_target]+source[index_source:], target, count+1, index_source+1, index_target, find_edit_distance( source[0:index_source]+target[index_target]+source[index_source:], target, count+1, index_source+1, index_target))
        min_val = min (find_edit_distance( source[0:index_source]+source[index_source+1:], target, count+1 , index_source, index_target),
                find_edit_distance( source[0:index_source]+target[index_target]+source[index_source+1:], target, count+1, index_source+1, index_target),
                find_edit_distance( source[0:index_source]+target[index_target]+source[index_source:], target, count+1, index_source+1, index_target))
        return min_val
## testing 

print(check("ple", "pale"))
print(check("pale","bae"))