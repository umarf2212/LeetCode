# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.ar = []
        self.traverse(self.root, 0)
        self.ar.sort()
    
    def traverse(self, root, currVal):
        if not root: return
        
        root.val = currVal
        self.ar.append(currVal)
        self.traverse(root.left, 2*currVal+1)
        self.traverse(root.right, 2*currVal+2)


    def find(self, target: int) -> bool:
        for num in self.ar:
            if num == target:
                return True
            elif num > target:
                return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)