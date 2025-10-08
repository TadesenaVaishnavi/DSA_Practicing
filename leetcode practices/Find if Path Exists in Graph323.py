##$ question - 
# 🔍 Problem (LeetCode style)

# Title: Find if Path Exists in Graph

# Problem Statement:
# You are given an integer n representing the number of nodes in a graph (labelled from 0 to n - 1) and a 2D array edges, where edges[i] = [u, v] indicates there is an undirected edge between nodes u and v. You are also given two nodes: source and destination.

# Return true if there is a path from source to destination, or false otherwise.

# Example:

# Input:
# n = 6
# edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
# source = 0
# destination = 5

# Output:
# false

# Explanation:
# There is no path connecting node 0 to node 5.

# Constraints:
# 1 <= n <= 2 * 10^5
# 0 <= edges.length <= 2 * 10^5
# edges[i].length == 2
# 0 <= u, v < n
# 0 <= source, destination < n


#### DFS

def valid_path(n, edges, source, destination):
    # Build adjacency list
    graph = { i: [] for i in range(n) }
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    
    def dfs(node):
        if node == destination:
            return True
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei):
                    return True
        return False
    
    return dfs(source)

#### BFS


from collections import deque

def valid_path(n, edges, source, destination):
    graph = { i: [] for i in range(n) }
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set([source])
    queue = deque([source])
    
    while queue:
        node = queue.popleft()
        if node == destination:
            return True
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
    
    return False



# n → number of nodes (labeled from 0 to n-1)
# edges → list of connections (pairs [u, v] meaning an edge between u and v)
# source → starting node
# destination → target node

# n = 6
# edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
# source = 0
# destination = 5

# Component 1:  0 -- 1
#                \
#                 2

# Component 2:  3 -- 4
#                \  /
#                 5
# Nodes 0, 1, 2 are connected.
# Nodes 3, 4, 5 are connected.
# But 0 and 5 are in different components, so → no path exists.

# What’s happening here:
# -----------------------
# ➤ What’s happening here:

# We’re creating a dictionary called graph that maps each node → list of its neighbors.

# { i: [] for i in range(n) }
# means create empty lists for nodes 0, 1, 2, ..., n-1.
# Then, for every pair [u, v] in edges:
# Add v to u’s list.
# Add u to v’s list (since the graph is undirected).
# 👉 So after this step, graph becomes:
# {
#   0: [1, 2],
#   1: [0],
#   2: [0],
#   3: [5, 4],
#   4: [5, 3],
#   5: [3, 4]
# }
# visited keeps track of nodes we’ve already explored (to avoid revisiting).
# queue is used for Breadth-First Search (BFS) —
# it stores nodes to be visited next.

#     # 3️⃣ BFS traversal
#     while queue:
#         node = queue.popleft()
#         if node == destination:
#             return True

# Take one node (node) from the queue.
# If it’s equal to destination, we found a path — return True.

#         for nei in graph[node]:
#             if nei not in visited:
#                 visited.add(nei)
#                 queue.append(nei)
# Loop through all neighbors (nei) of the current node.
# If the neighbor isn’t visited:
# Mark it as visited.
# Add it to the queue (to explore it later).
# This ensures we gradually explore all reachable nodes from source.
