# url :- https://www.interviewbit.com/problems/clone-graph/
# Problem Description
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
# Note: The test cases are generated in the following format (use the following format to use See Expected Output option):
# First integer N is the number of nodes.
# Then, N intgers follow denoting the label (or hash) of the N nodes.
# Then, N2 integers following denoting the adjacency matrix of a graph, where Adj[i][j] = 1 denotes presence of an undirected edge between the ith and jth node, O otherwise.
# Problem Constraints
# 1 <= Number of nodes <= 105
# Input Format
# First and only argument is a node A denoting the root of the undirected graph.
# Output Format
# Return the node denoting the root of the new clone graph.


# Definition for a undirected graph node
from collections import deque


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def cloneGraph(self, node):
        if not node :
            return node

        visited = {}
        def dfs(node) :
            if node.label in visited :
                return visited[node.label]
            
            newNode = UndirectedGraphNode(node.label)
            visited[node.label] = newNode
            for neighbor in node.neighbors :
                newNode.neighbors.append(dfs(neighbor))
            
            return newNode
        
        return dfs(node)
        
parent = UndirectedGraphNode(1)
child1 = UndirectedGraphNode(2)
child2 = UndirectedGraphNode(3)

parent.neighbors = [child1, child2]
child1.neighbors = [parent, child2]
child2.neighbors = [child1, parent]

visited = {}

def printGraph(node) :
    if not node :
        return node 
    if node.label in visited :
        return 
    visited[node.label] = True
    for child in node.neighbors :
        if child != node :
            print(node.label, child.label)
            printGraph(child)

sol = Solution()
head = sol.cloneGraph(parent)
printGraph(head)