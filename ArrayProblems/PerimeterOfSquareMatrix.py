class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0 
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    ans+=4
                    # Checks if the upper row must be the shaded part it will be subtratcted from ans 
                    if r>0 and grid[r-1][c]==1:
                        ans-=2
                    #  Checks if the side row must be the shaded part it will be subtratcted from ans 
                    if c>0 and grid[r][c-1]==1:
                        ans-=2
        # Return thr perimeter
        return ans

        