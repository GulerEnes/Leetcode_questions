class Solution:
    def DFS(self, grid, node):
        x, y = node
        neighboors = []
        if x + 1 < len(grid):
            neighboors.append((x + 1, y))
        if x - 1 >= 0:
            neighboors.append((x - 1, y))
        if y + 1 < len(grid[0]):
            neighboors.append((x, y + 1))
        if y - 1 >= 0:
            neighboors.append((x, y - 1))

        grid[x][y] = '-1'
        for n in neighboors:
            print(n)
            if grid[n[0]][n[1]] == '1':
                self.DFS(grid, n)

    def numIslands(self, grid) -> int:
        count = 0
        for x, val_x in enumerate(grid):
            for y, val_y in enumerate(val_x):
                if val_y == '1':
                    self.DFS(grid, (x, y))
                    count += 1
        return count


s = Solution()

grid = [["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]]

print(s.numIslands(grid))
