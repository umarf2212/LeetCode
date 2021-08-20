# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    totalLeavesFound = False
    totalLeaves = 0
        
    def findMaxDepth(self, root):
        if not root: return 0
        return 1 + self.findMaxDepth(root.left)
    
    
    def countLeaves(self, root, level, maxLevel):
        if not root: return
        
        if level == maxLevel-1 and not root.right:
            self.totalLeavesFound = True
        
        elif not root.left and not root.right:
            self.totalLeaves += 1
            
        self.countLeaves(root.left, level+1, maxLevel)
        
        if not self.totalLeavesFound:
            self.countLeaves(root.right, level+1, maxLevel)

    
    def countNodes(self, root: TreeNode) -> int:
        
        maxLevel = self.findMaxDepth(root)
        
        self.countLeaves(root, 1, maxLevel)
                
        totalNodes = 0
        for i in range(0, maxLevel-1):
            totalNodes += 2**i
            
        totalNodes += self.totalLeaves
        
        return totalNodes