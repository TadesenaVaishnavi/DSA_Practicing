from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        
        # If start or end is blocked
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        # 8 directions
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        # BFS queue → store (row, col, distance)
        q = deque([(0, 0, 1)])  
        visited = set([(0, 0)])

        while q:
            r, c, dist = q.popleft()
            
            # If we reached destination
            if (r, c) == (n-1, n-1):
                return dist

            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, dist + 1))

        return -1




# Explaination:
Why Answer = 4 (not 5)?

BFS counts the number of steps including both start and end cells.

Path taken:
(0,0) → (0,1) → (1,2) → (2,2)

That’s 4 cells in total.

If you were counting just the edges/moves, you’d get 3. But LeetCode defines it as path length in terms of cells visited.
