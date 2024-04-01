# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        # 1. To delete current root
        # -> remove reference from parent
        # 2. Not to delete current root
        # 3. Traverse hashset, do DFS on each node
        
        def traverse(root, parent):
            if not root: return

            # delete current root
            if root.val in to_delete:

                # remove reference
                if parent.left == root:
                    parent.left = None
                else:
                    parent.right = None

            
            else:
                roots.add(root)

            traverse(root.left, root)
            traverse(root.right, root)

        roots = set()
        if root.val not in to_delete:
            roots.add(root)
        
        traverse(root.left, root)
        traverse(root.right, root)

        def removeNodes(root):
            if not root: return

            nodesToRemove.add(root)
            
            removeNodes(root.left)
            removeNodes(root.right)

        nodesToRemove = set()
        for root in roots:
            if root.left:
                removeNodes(root.left)
            
            if root.right:
                removeNodes(root.right)
        
        for nodes in nodesToRemove:
            roots.remove(nodes)
        
        return list(roots)
            

                



