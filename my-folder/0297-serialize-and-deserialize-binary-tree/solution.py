# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return []
        
        q = deque([root])
        arr = []
        while q:
            curr = q.popleft()
            
            if curr:
                arr.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                arr.append('null')
                    
        while arr[-1] is 'null':
            arr.pop()
                
        return arr

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        
        q = deque(data)
        root = TreeNode(q.popleft())
        roots = deque([root])
        while q:
            curr = roots.popleft()
            
            left = None
            right = None
            
            if q: 
                left = TreeNode(q.popleft())
            if q:
                right = TreeNode(q.popleft())
            
            if left: 
                curr.left = left
                roots.append(left)
            
            if right: 
                curr.right = right
                roots.append(right)
                
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
