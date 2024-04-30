class FileSystem:

    def __init__(self):
        self.basePath = {} # Trie
    
    # def traverseTrie(self, paths, i, curFolder):
    #     if i<len(paths)-1 and paths[i] not in curFolder:
    #         return False
        
    #     curFolder = curFolder[paths[i]]
    #     return self.traverseTrie(paths, i+1, curFolder)

    def createPath(self, path: str, value: int) -> bool:
        paths = path.split('/')[1:]


        curFolder = self.basePath
        for i in range(len(paths)):
            path = paths[i]
            
            if path in curFolder:
                curFolder = curFolder[path]
            elif len(paths) > 1 and i < len(paths)-1:
                return False
            else:
                curFolder[path] = {}
                curFolder = curFolder[path]
        
        if '_value' in curFolder:
            return False
        
        curFolder['_value'] = value
        return True

    def get(self, paths: str) -> int:
        paths = paths.split('/')[1:]

        curFolder = self.basePath
        for i in range(len(paths)):
            path = paths[i]
            
            if path in curFolder:
                curFolder = curFolder[path]
            else:
                return -1

        if '_value' in curFolder:
            return curFolder['_value']
        else: 
            return -1


        
'''

# /path/to/file => 10
# ['', 'path', 'to', 'file]

# folderName: [value, {}]

# ['path', 'to', 'file']

{
    path: [
            -1, 
            {
                to: 
                    [
                        -1, 
                        {
                            file:[
                                    10, 
                                    {}
                                ]
                        }
                    ]
            }
    ]
}


'''

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
