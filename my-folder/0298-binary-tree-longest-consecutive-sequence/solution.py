# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root, parentVal, currLongest, longest):
            if not root: return

            if root.val == parentVal+1:
                currLongest += 1
                longest[0] = max(longest[0], currLongest)
            else:
                currLongest = 1
            
            traverse(root.left, root.val, currLongest, longest)
            traverse(root.right, root.val, currLongest, longest)
        

        longest = [1]
        traverse(root, root.val, 1, longest)
        return longest[0]
        
