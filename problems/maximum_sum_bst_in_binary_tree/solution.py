# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        # return: [True, maxSum, Min, Max]
        def traverse(root, ans):
            if not root: return
            if not root.left and not root.right:
                ans[0] = max( ans[0], root.val )
                return [True, root.val, root.val, root.val]
            
            left = traverse(root.left, ans)
            right = traverse(root.right, ans)

            isBST = True

            if left:
                isBST = isBST and left[0] and root.val > left[3]
            
            if right:
                isBST = isBST and right[0] and root.val < right[2]
            
            # Is not a BST
            if not isBST:
                maxSum = float('-inf')
                if left: 
                    maxSum = max(maxSum, left[1], ans[0])
                if right: 
                    maxSum = max(maxSum, right[1], ans[0])
                
                return [False, maxSum, -1, -1]
            
            # Is a BST
            curSum = root.val
            curMin = root.val
            curMax = root.val
            if left:
                curSum += left[1]
                curMin = left[2]
            if right:
                curSum += right[1]
                curMax = right[3]
            
            ans[0] = max( ans[0], curSum )

            return [True, curSum, curMin, curMax]
        
        ans = [0]
        ret = traverse(root, ans)
        ans = max(ans[0], ret[1])
        return ans if ans > 0 else 0

