def numIslands(grid):
    if grid is None:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    def dfs(i,j):
        if i<0 or i>rows-1 or j<0 or j>cols-1 or grid[i][j]!='1':
            return
        grid[i][j]="visited"
        dfs(i+1,j)
        dfs(i,j+1)
        dfs(i-1,j)
        dfs(i,j-1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j]=='1':
                islands+=1
                dfs(i,j)

    return islands

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

num = numIslands(grid)
print(num)
