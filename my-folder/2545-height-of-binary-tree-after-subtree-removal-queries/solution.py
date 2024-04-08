# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
    
        # heights = [0] * (n + 1)

        '''
        1. We first calculate depth and height of each node.

        2. Then we find all the cousins at every depth
           Per depth, we just need only two highest cousins
        
        3. Removing a node has 3 possibilities:
            - Node doesn't have any cousins - means it's automatically 
              a part of the max path (observe carefully)
              Removing it removes its height and also iteself
              So the max height of tree becomes depth-1

            - Node is part of the max path - we need its highest cousin 
              that now contributes to overall height of the tree.
            
            - Node is not part of the max path - so we get the path that
              has the max path

        '''

        # Node.val
        Heights = defaultdict(int)

        # Node.val
        Depths = defaultdict(int)

        def dfs(root, depth):
            if not root: return -1

            Depths[root.val] = depth

            curHeight = max(dfs(root.left, depth+1), dfs(root.right, depth+1)) + 1

            Heights[root.val] = curHeight

            return curHeight
        
        dfs(root, 0)

        # key: depth, height: [Heights[Node.val], Node.val]
        cousins = defaultdict(list)
        for val, depth in Depths.items():
            cousins[depth].append( (Heights[val], val) )

            # sort by height
            # at most 3 elements at any given time
            cousins[depth].sort(reverse=True)

            # if the cousin count increases to 3, immediately pop third largest
            if len(cousins[depth]) > 2:
                cousins[depth].pop()

        # height of the overall tree 
        ans = []

        # Process the queries
        # q: Node.val
        for q in queries:
            depth = Depths[q]

            if len(cousins[depth]) == 1:
                ans.append( depth-1 )
            
            elif cousins[depth][0][1] == q:
                # second maxHeight+depth = overall height of the tree
                ans.append( cousins[depth][1][0] + depth ) 
            
            else:
                ans.append( cousins[depth][0][0] + depth )
        
        return ans
