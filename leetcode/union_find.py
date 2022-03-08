

def minIncrementForUnique(A):
        root = {}
        def find(x):
            root[x] = find(root[x] + 1) if x in root else x
            print(f'root: {root}')
            return root[x]
        
        return sum(find(a) - a for a in A)


print(minIncrementForUnique([1,2,2]))
print(minIncrementForUnique([3,2,1,2,1,7]))