import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  # (cost, point_index)
        total_cost = 0

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue

            # Add the point to MST
            visited.add(i)
            total_cost += cost

            # Check all unvisited neighbors and push their distances
            for j in range(n):
                if j not in visited:
                    xi, yi = points[i]
                    xj, yj = points[j]
                    dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(min_heap, (dist, j))

        return total_cost

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
sol = Solution()
print(sol.minCostConnectPoints(points))



# Input
# points =
# [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output
# 20