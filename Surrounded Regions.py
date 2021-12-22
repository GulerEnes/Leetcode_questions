class Solution:
    def neighboors(self, grid, x, y):
        arr = []
        if 0 <= y - 1 and grid[x][y - 1] == 'O':
            arr.append((x, y - 1))
        if y + 1 < len(grid[0]) and grid[x][y + 1] == 'O':
            arr.append((x, y + 1))
        if x + 1 < len(grid) and grid[x + 1][y] == 'O':
            arr.append((x + 1, y))
        if 0 <= x - 1 and grid[x - 1][y] == 'O':
            arr.append((x - 1, y))
        return arr

    def DFS(self, m, row, col):
        m[row][col] = 'K'
        for n_row, n_col in self.neighboors(m, row, col):
            self.DFS(m, n_row, n_col)

    def solve(self, grid) -> None:
        # print(len(grid), len(grid[0])) = 1x4 mxn
        for col in range(len(grid[0])):
            if grid[0][col] == 'O':
                self.DFS(grid, 0, col)
        for col in range(len(grid[0])):
            if grid[-1][col] == 'O':
                self.DFS(grid, len(grid) - 1, col)
        for row in range(len(grid)):
            if grid[row][0] == 'O':
                self.DFS(grid, row, 0)
        for row in range(len(grid)):
            if grid[row][-1] == 'O':
                self.DFS(grid, row, len(grid[0]) - 1)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 'K':
                    grid[row][col] = 'O'
                elif grid[row][col] == 'O':
                    grid[row][col] = 'X'


s = Solution()

grid = [["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]]

s.solve(grid)

print(grid)
