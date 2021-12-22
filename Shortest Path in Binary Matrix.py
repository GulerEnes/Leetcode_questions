class Solution:

    def neighboors(self, grid, n, x, y):
        return [(i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2) if
                0 <= i < n and 0 <= j < n and grid[i][j] == 0]

    def bfs(self, grid):
        queue = [(0, 0)]
        levels = {(0, 0): 1}
        while len(queue) > 0:
            c_x, c_y = queue.pop(0)
            if c_x == len(grid) - 1 and c_y == len(grid) - 1:
                return levels[(c_x, c_y)]
            if grid[c_x][c_y] == 0:
                grid[c_x][c_y] = 2  # Visit

                for n_x, n_y in self.neighboors(grid, len(grid), c_x, c_y):
                    if grid[n_x][n_y] == 0:  # Not visited
                        queue.append((n_x, n_y))
                        if (n_x, n_y) not in levels:
                            levels[(n_x, n_y)] = levels[(c_x, c_y)] + 1
        return -1

    def shortestPathBinaryMatrix(self, grid):
        return self.bfs(grid)


s = Solution()

grid = [[0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]]

print(s.shortestPathBinaryMatrix(grid))
