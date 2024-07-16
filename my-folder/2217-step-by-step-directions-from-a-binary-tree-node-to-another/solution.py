# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def findLCA(node, start, dest, lca):
            if not node:
                return False
            
            left = findLCA(node.left, start, dest, lca)
            right = findLCA(node.right, start, dest, lca)

            if left and right:
                lca[0] = node
            
            if node.val == start or node.val == dest:
                if left or right:
                    lca[0] = node
                else:
                    return True
            
            return left or right
        
        lca = [None]
        findLCA(root, startValue, destValue, lca)

        def findStart(node, startValue, curPath, pathCount):
            if not node:
                return
            
            if node.val == startValue:
                for p in curPath:
                    path.append(p)
            
            curPath.append('U')
            findStart(node.left, startValue, curPath, pathCount)
            findStart(node.right, startValue, curPath, pathCount)
            curPath.pop()

        def findDest(node, destValue, curPath, path):
            if not node: return

            if node.val == destValue:
                for p in curPath:
                    path.append(p)
            
            curPath.append('L')
            findDest(node.left, destValue, curPath, path)
            curPath.pop()

            curPath.append('R')
            findDest(node.right, destValue, curPath, path)
            curPath.pop()

        path = []
        curPath = []

        findStart(lca[0], startValue, curPath, path)
        if lca[0].val == destValue:
            return ''.join(path)

        findDest(lca[0], destValue, curPath, path)
        if lca[0].val == startValue:
            return ''.join(path)
        
        return ''.join(path)



