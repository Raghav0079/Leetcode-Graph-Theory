from collections import deque

class Solution(object):
    def numEnclaves(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def bfs(r, c):
            queue = deque([(r, c)])
            visit.add((r, c))
            count = 0
            
            while queue:
                curr_r, curr_c = queue.popleft()
                count += 1
                
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        grid[nr][nc] == 1 and (nr, nc) not in visit):
                        visit.add((nr, nc))
                        queue.append((nr, nc))
            return count

        land_total = 0
        border_land = 0

        # 1. Total Land Count
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    land_total += 1

        # 2. BFS from all Border Land cells
        for r in range(ROWS):
            for c in range(COLS):
   
                if grid[r][c] == 1 and (r, c) not in visit:
                    if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                        border_land += bfs(r, c)

        return land_total - border_land
