"""

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique positive integer identifier.

For example, in this diagram, 6 and 8 have common ancestors of 4 and 14.

               15
              / \
         14  13  21
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

parent_child_pairs_2 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (15, 21), (4, 8), (4, 9), (9, 11), (14, 4), (13, 12),
    (12, 9), (15, 13)
]

Write a function that takes this data and the identifiers of two individuals as inputs and returns true if and only if they share at least one ancestor. 

Sample input and output:

has_common_ancestor(parent_child_pairs_2, 3, 8)   => false
has_common_ancestor(parent_child_pairs_2, 5, 8)   => true
has_common_ancestor(parent_child_pairs_2, 6, 8)   => true
has_common_ancestor(parent_child_pairs_2, 6, 9)   => true
has_common_ancestor(parent_child_pairs_2, 1, 3)   => false
has_common_ancestor(parent_child_pairs_2, 3, 1)   => false
has_common_ancestor(parent_child_pairs_2, 7, 11)  => true
has_common_ancestor(parent_child_pairs_2, 6, 5)   => true
has_common_ancestor(parent_child_pairs_2, 5, 6)   => true
has_common_ancestor(parent_child_pairs_2, 3, 6)   => true
has_common_ancestor(parent_child_pairs_2, 21, 11) => true

n: number of pairs in the input


"""

def add_people(people, target):
    
    if target not in people:
        people.append(target)
    
    

def output(pairs, input1, input2):
    
    # validations 
    if len(pairs) == 0:
        return False
    
    
    # main logic 
    res = []
    child_parent_mapping = {}
    #people = []
    # presumptions
    # no duplicate input
    
    
    
    #O(pairs)
    
    for pair in pairs:
        
#         add_people(people, pair[0]) # convert people to set to reduce O(people) to O(1)
#         add_people(people, pair[1])
        
        mapping = []
        
        if pair[1] in child_parent_mapping: # O(1)
            mapping = child_parent_mapping[pair[1]]
        
        mapping.append(pair[0]) # append at end o(1)
        child_parent_mapping[pair[1]] = mapping
    
    
#     one_parent = []
#     zero_parent = []
    
    
#     for child in child_parent_mapping:
#         if len(child_parent_mapping[child]) == 1:
#             one_parent.append(child)
            
#     # O(people)
#     for person in people:
#         if person not in child_parent_mapping:
#             zero_parent.append(person)
    
       
#     res = [zero_parent, one_parent]        

    # main logic 
    
    if input1 not in child_parent_mapping or input2 not in child_parent_mapping:
        return False
    

    anc_input1 = get_anc(child_parent_mapping, input1)
    anc_input2 = get_anc(child_parent_mapping, input2)
    
    # sort these first or just run a double loop O(n2)
    # sort can be done in o(nlogn)
    anc_input1.sort()
    anc_input2.sort()
    
    for person in anc_input1:
        if person in anc_input2:
            return True
    for person in anc_input2:
        if person in anc_input1:
            return True
    # return response 

    return False
    
def get_anc(mapping, target):
    
    anc = []
    # handle edge cases here 
    print(mapping, target)
    
    while target in mapping:
        if mapping[target] == None:
            break
        target = mapping[target]
        anc.append(target)
            
    return anc


    
    
parent_child_pairs_2 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (15, 21),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9),
    (15, 13)
]

assert output(parent_child_pairs_2,3, 8 ) == False 
assert output(parent_child_pairs_2,5, 8 ) == True 
# assert output(parent_child_pairs) == [[1, 2, 4, 15, 30], [5, 7, 9, 16]]




