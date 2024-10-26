class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isEnd = False

class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:

        folders = [tuple(folder[1:].split('/')) for folder in folders]
        folders.sort(key=lambda x:len(x))
        
        remove = set()
        for i in range(len(folders)):
            if i in remove: 
                continue

            curLen = len(folders[i])
            for j in range(i+1, len(folders)):
                if j in remove:
                    continue

                if folders[j][:curLen] == folders[i]:
                    remove.add(j)

        result = ['/'+ '/'.join(folders[i]) for i in range(len(folders)) if i not in remove]

        return result

        
