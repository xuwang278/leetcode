"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    # Sol 1: dfs
    def cloneGraph(self, node: 'Node') -> 'Node':
        dict = {}
        return self.dfs(node, dict)
    
    def dfs(self, node, dict):
        if node in dict:
            return dict[node]
        
        copy = Node(node.val, [])
        dict[node] = copy
        for next in node.neighbors:
                copy.neighbors.append(self.dfs(next, dict))
        
        return copy

    # Sol 2: bfs / iterative dfs
    def cloneGraph(self, node: 'Node') -> 'Node':
        dict, q = {}, []
        dict[node] = Node(node.val, [])
        q.append(node)
        while q:
            top = q.pop(0) # q.pop() - iterative dfs
            for next in top.neighbors:
                if next not in dict:
                    dict[next] = Node(next.val, [])
                    q.append(next)
                dict[top].neighbors.append(dict[next])
        return dict[node]

        