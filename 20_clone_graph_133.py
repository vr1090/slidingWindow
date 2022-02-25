"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        if node is None:
            return node
        
        def dfs(node):
            
            if node in oldToNew:
                return oldToNew[node]
            
            newNode = Node(node.val)
            
            oldToNew[node] = newNode
            
            for n in node.neighbors:        
                nodeN = dfs(n)
                newNode.neighbors.append(nodeN)
            
            
            return newNode
        
        return dfs(node)
        
                
        
        