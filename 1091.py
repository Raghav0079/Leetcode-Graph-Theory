'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 
'''


from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        N = len(grid)
        # Check if start or end is blocked immediately
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        
        # (row, col, current_path_length)
        q = deque([(0, 0, 1)])
        visit = set([(0, 0)])
        
        # 8 directions
        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0), 
            (1, 1), (-1, 1), (1, -1), (-1, -1)
        ]

        while q:
            r, c, length = q.popleft()
            
            # Since we check the start, if we reach this, we are at (N-1, N-1)
            if r == N - 1 and c == N - 1:
                return length
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Validation: In bounds, is a '0', and not visited
                if (0 <= nr < N and 0 <= nc < N and 
                    grid[nr][nc] == 0 and (nr, nc) not in visit):
                    
                    q.append((nr, nc, length + 1))
                    visit.add((nr, nc)) # Mark visited immediately upon adding to queue

        return -1
