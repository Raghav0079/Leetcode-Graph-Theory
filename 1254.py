class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def is_closed(r, c):
      
            stack = [(r, c)]
            visit.add((r, c))
            closed = True
            
            while stack:
                curr_r, curr_c = stack.pop()
                
                if curr_r == 0 or curr_r == ROWS - 1 or curr_c == 0 or curr_c == COLS - 1:
                    closed = False
                
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        grid[nr][nc] == 0 and (nr, nc) not in visit):
                        visit.add((nr, nc))
                        stack.append((nr, nc))
            
            return 1 if closed else 0

        res = 0 
        for r in range(ROWS):
            for c in range(COLS):
                
                if grid[r][c] == 0 and (r, c) not in visit:
                    res += is_closed(r, c)

        return res
