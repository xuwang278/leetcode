class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [-1, 0, 1, 0, -1]
        cnt = 0
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'
            for k in range(4):
                dfs(i + dirs[k], j + dirs[k + 1])
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
                    
        return cnt

    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [-1, 0, 1, 0, -1]
        cnt = 0
        
        def bfs(i, j):
            q = [(i, j)]
            grid[i][j] = '0'
            while q:
                i, j = q.pop(0)
                for k in range(4):
                    di, dj = i + dirs[k], j + dirs[k + 1]
                    if di < 0 or di >= len(grid) or dj < 0 or dj >= len(grid[0]) or grid[di][dj] == '0':
                        continue
                    grid[di][dj] = '0'
                    q.append((di, dj))
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i, j)
                    cnt += 1
                    
        return cnt

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        cnt = 0;
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # self.dfs(grid, i, j)
                    self.bfs(grid, i, j)
                    cnt += 1
        return cnt
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dirs = [-1, 0, 1, 0, -1]
        for k in range(4):
            self.dfs(grid, i + dirs[k], j + dirs[k + 1])

    def bfs(self, grid, i, j):
        q, dirs = [(i, j)], [-1, 0, 1, 0, -1]
        grid[i][j] = '0'
        while q:
            i, j = q.pop(0)
            for k in range(4):
                di, dj = i + dirs[k], j + dirs[k + 1]
                if di < 0 or dj < 0 or di >= len(grid) or dj >= len(grid[0]) or grid[di][dj] == '0':
                    continue
                grid[di][dj] = '0'
                q.append((di, dj))
