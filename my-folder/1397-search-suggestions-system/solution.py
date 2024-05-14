from bisect import bisect_left
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        # 1. Sort the products
        # 2. For every prefix, 

        products.sort()
        result = []
        for i in range(1, len(searchWord)+1):
            prefix = searchWord[:i]
            idx = bisect_left(products, prefix)

            suggestions = []
            for j in range(idx, len(products)):
                if j-idx == 3: break
                if products[j].startswith(prefix):
                    suggestions.append(products[j])

            result.append(suggestions)
        
        return result



        
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        def insertWord(word, i, trieNode):
            if i == len(word):
                trieNode.isEnd = True
                return

            ch = word[i]
            if ch not in trieNode.children:
                trieNode.children[ch] = TrieNode()
            
            insertWord(word, i+1, trieNode.children[ch])
        
        insertWord(word, 0, self.root)
    
    def searchWords(self, subStr, i, trieNode, wordList):
        if i < len(subStr):
            if not trieNode or subStr[i] not in trieNode.children:
                wordList.append([])
                searchWords(self, subStr, i, None, wordList)
            else:
                searchWords(self, subStr, i+1, trieNode.children[subStr[i]], wordList)
        
        # at this point, we just want 3 words
        # so, we traverse the tree and get three words
        for child in sorted(trieNode.children):
            pass
'''

