class Solution:
    def allPathsSourceTarget(self, graph):
        result = []
        queue = [[0]]
        while len(queue) > 0:
            path = queue.pop(0)
            if path[-1] == len(graph) - 1:
                result.append(path)
            else:
                for n in graph[path[-1]]:
                    queue.append(path + [n])
        return result


s = Solution()

inp = [[4, 3, 1], [3, 2, 4], [3], [4], []]

print(s.allPathsSourceTarget(inp))
