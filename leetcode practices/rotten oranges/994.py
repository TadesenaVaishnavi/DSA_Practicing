from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # Step 1: Count fresh and enqueue all rotten
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    time = 0
    directions = [(0,1),(1,0),(-1,0),(0,-1)]

    # Step 2: BFS from rotten oranges
    while queue and fresh > 0:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
        time += 1

    return time if fresh == 0 else -1

# ✅ Test Input
grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]

print("Minutes to rot all oranges:", orangesRotting(grid))


# output
# Minutes to rot all oranges: 4