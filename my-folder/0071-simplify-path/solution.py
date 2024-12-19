class Solution:
    def simplifyPath(self, path: str) -> str:

        # /home/user///Documents/..///Pictures


        # result = '/home/user/Documents/../../Pictures/./' 

        # /home/user///Documents/../..//Pictures/./

        stack = []
        curFolder = ''
        for i in range(len(path)):
            if path[i] == '/':
                if curFolder and curFolder == '..' and stack:
                    stack.pop()
                    curFolder = ''
                elif curFolder:
                    if curFolder != '.':
                        stack.append(curFolder)
                    curFolder = ''

            else:
                curFolder += path[i]
        
        print(curFolder, stack)

        if curFolder:
            if curFolder == '..' and stack:
                stack.pop()
            elif curFolder != '.':
                stack.append(curFolder)
                

        result = ''
        for folder in stack:
            if folder == '..':
                continue

            result += '/' + folder

        return result if result else '/'




