class Trie:
    def __init__(self):
        self.trie = {'children': {}, 'isEnd': False}

    def insert(self, word: str) -> None:
        root = self.trie
        for i in range(len(word)):
            ch = word[i]
            if ch not in root['children']:
                root['children'][ch] = {'children':{}, 'isEnd': False}

            if i == len(word)-1:
                root['children'][ch]['isEnd'] = True
            else:
                root = root['children'][ch]

    def search(self, word: str) -> bool:
        root = self.trie
        for i in range(len(word)):
            ch = word[i]
            if ch not in root['children']:
                return False

            if i < len(word)-1:
                root = root['children'][ch]

        return root['children'][ch]['isEnd']

    def startsWith(self, prefix: str) -> bool:
        root = self.trie
        for i in range(len(prefix)):
            ch = prefix[i]
            if ch not in root['children']:
                return False

            if i < len(prefix)-1:
                root = root['children'][ch]
                
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
'''
s = "apple"
{"a": {
        children:{
            "p": {
                children: {
                    "p": {
                        children: {
                            "l": {
                                children: {
                                    "e": {
                                        children:{},
                                        isEnd: True
                                    }
                                },
                                isEnd: False
                            }
                        },
                        isEnd: False
                    }
                },
                isEnd: False
            }
        }, 
        isEnd:False
    }
}
'''
