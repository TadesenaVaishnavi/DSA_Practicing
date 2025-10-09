# DFS
def countComponents(n, edges):
    # 1️⃣ Build adjacency list
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    count = 0
    
    # 2️⃣ DFS function
    def dfs(node):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)
    
    # 3️⃣ Iterate all nodes
    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1  # New component found
    
    return count

# BFS
from collections import deque

def countComponents(n, edges):
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    count = 0
    
    for i in range(n):
        if i not in visited:
            queue = deque([i])
            visited.add(i)
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            count += 1  # Finished exploring one component
    
    return count

# Title: Number of Connected Components in an Undirected Graph

# Problem Statement:
# You are given an integer n representing the number of nodes in an undirected graph (labeled 0 to n-1) and a 2D array edges, where edges[i] = [u, v] indicates an edge between nodes u and v.

# Return the number of connected components in the graph.
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2

# Explanation:
# There are two connected components:
# Component 1: 0-1-2
# Component 2: 3-4

# Represent the graph using an adjacency list.
# Keep a visited set to track nodes we have explored.
# Initialize a count = 0 for connected components.
# Iterate over all nodes 0 to n-1:
# If a node is not visited, it’s a new component:
# Run DFS or BFS from that node to mark all reachable nodes as visited.
# Increment count.
# Return count after checking all nodes.
# Key Idea: Every time we start DFS/BFS from an unvisited node, we’ve found a new connected component.


###### DT
#1) 2D array edges and u & v means each end of edge
# In a graph:
# Nodes are points (0, 1, 2, …).
# Edges are connections between nodes.
# A 2D array edges stores all edges in the graph.
# Each element [u, v] represents one edge connecting node u to node v.

#2) adjacency list?
# An adjacency list is a way to represent a graph efficiently:



