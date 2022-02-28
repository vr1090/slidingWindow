class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        island = [[0] * len(grid[0]) for i in range(len(grid)) ]
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def dfs(r,c, no):
            if (r,c) in visited:
                return
            if r < 0 or c < 0 or r == rows or c == cols:
                return
            
            if(grid[r][c] == "0"):
                return
            
            visited.add((r,c))
            island[r][c] = no
            
            dfs(r+1,c, no)
            dfs(r-1,c,no)
            dfs(r,c+1,no)
            dfs(r,c-1,no)
            
            
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    count += 1
                    dfs(r,c,count)
        
        

        
        return count