# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root, moves):
            if not root: return 0

            left = traverse(root.left, moves)
            right = traverse(root.right, moves)

            moves[0] += abs(left) + abs(right)

            return (root.val - 1) + left + right
        
        moves = [0]
        traverse(root, moves)
        return moves[0]


            
