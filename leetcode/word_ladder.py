import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        print(wordList)
        queue = collections.deque([[beginWord, 1]])
        print("starting: ", queue)
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0



divider = ['-']*10
print(Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(divider)

print(Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))