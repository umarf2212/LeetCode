# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root):
            nonlocal moves
            if not root: return 0

            left = traverse(root.left)
            right = traverse(root.right)

            excess = root.val - 1
            moves += abs(left) + abs(right)

            return left + right + excess

        moves = 0
        traverse(root)
        return moves