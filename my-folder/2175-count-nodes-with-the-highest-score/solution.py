class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:

        # 1. Build the tree from array to Tree structure
        #    - Create nodes from 0 to n-1 and store in a hashmap
        #    - Add left and right child connections

        # 2. Do DFS on the tree
        # 3. Calculate size of the whole tree
        # 4. For any node, we can get it's left & right subtree's
        #    size and subtract from size of the whole tree to 
        #    get the sizes of left, right and parent subtrees.


        # parents[i] is the parent of i

        # create nodes from 0 to n-1
        n = len(parents)
        tree = {}
        for i in range(n):
            tree[i] = TreeNode(i)
        
        # build the tree edges
        for i in range(1, n):
            if not tree[parents[i]].left:
                tree[parents[i]].left = tree[i]
            else:
                tree[parents[i]].right = tree[i]
        
        root = tree[0]
        
        totalTreeSize = len(parents)

        def countScores(root, scores, totalTreeSize, maxScore):
            if not root: return 0

            left = countScores(root.left, scores, totalTreeSize, maxScore)
            right = countScores(root.right, scores, totalTreeSize, maxScore)


            restTreeSize = totalTreeSize - 1 - left - right or 1

            # print(root.val, left, right, restTreeSize)

            scores[root.val] = restTreeSize 
            scores[root.val] *= 1 if left==0 else left 
            scores[root.val] *= 1 if right==0 else right
            maxScore[0] = max(maxScore[0], scores[root.val])

            return 1 + left + right
        
        scores = {}
        maxScore = [0]
        countScores(root, scores, totalTreeSize, maxScore)
        ans = sum([1 if score==maxScore[0] else 0 for score in scores.values()])

        return ans
