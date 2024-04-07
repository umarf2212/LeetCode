# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        

        def inorder(root, nodes):
            if not root: return
            inorder(root.left, nodes)
            nodes.append(root)
            inorder(root.right, nodes)
        
        nodes = []
        inorder(root, nodes)

        for i in range(len(nodes)):
            node = nodes[i]

            if node.val == p.val:
                if i < len(nodes)-1:
                    return nodes[i+1]
                else:
                    return None
