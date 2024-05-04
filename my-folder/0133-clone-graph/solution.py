"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        if not node.neighbors:
            return Node(node.val)

        # 1. DFS on the Graph
        # 2. Make adjacency list of all nodes using Hashtable
        # 3. Recreate the graph off of the Adj list

        def dfs(v, adj):
            vis.add(v.val)

            # O(E)
            for u in v.neighbors:
                adj[v.val].append(u.val)
            
            # O(E)
            for u in v.neighbors:
                if u.val not in vis:
                    dfs(u, adj)
        
        
        adj = defaultdict(list)
        vis = set()
        dfs(node, adj)

        # Create individual nodes for corresponding values
        valNodes = {}
        for v in adj:
            valNodes[v] = Node(v)

        # vis = set()
        # def dfs(v, valNodes):
        for v in adj:
            for u in adj[v]:
                valNodes[v].neighbors.append(valNodes[u])

        return valNodes[1]


