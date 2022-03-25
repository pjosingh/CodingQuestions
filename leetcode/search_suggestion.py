class TrieNode:
    def __init__(self) -> None:
        self.children = [None]*26
        self.eow = False

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()


    def add(self, target):
        it = self.root

        for el in target:
            if (it.children[ord(el)-ord('a')] == None):
                it.children[ord(el)-ord('a')] = TrieNode()
            it = it.children[ord(el)-ord('a')]
        it.eow = True
        

    def get(self, target):
        pass

    def print(self):
        print(f' children: {self.root.children} root: {self.root}')

class Solution:
    def suggestedProducts(self, products, searchWord):
        trie = Trie()
        for product in products:
            trie.add(product)
        trie.print()
        


Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"],"mouse") 

# assert Solution.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse") == [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]