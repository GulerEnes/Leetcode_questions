# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def notMarked(self, node):
        return -100 <= node.val <= 100

    def visit(self, node):
        node.val += 200 * (1 if node.val >= 0 else -1)

    def unvisit(self, node):
        node.val -= 200 * (1 if node.val >= 0 else -1)

    def bfs(self, head):
        levels_sorted = {0: [head]}
        levels_nodes = {head: 0}

        queue = [head]
        while len(queue) > 0:
            node = queue.pop(0)
            if self.notMarked(node):
                self.visit(node)
                if node.left != None and self.notMarked(node.left):
                    queue.append(node.left)
                    levels_nodes[node.left] = levels_nodes[node] + 1
                    if levels_nodes[node.left] in levels_sorted:
                        levels_sorted[levels_nodes[node.left]].append(node.left)
                    else:
                        levels_sorted[levels_nodes[node.left]] = [node.left]
                if node.right != None and self.notMarked(node.right):
                    queue.append(node.right)
                    levels_nodes[node.right] = levels_nodes[node] + 1
                    if levels_nodes[node.right] in levels_sorted:
                        levels_sorted[levels_nodes[node.right]].append(node.right)
                    else:
                        levels_sorted[levels_nodes[node.right]] = [node.right]
        return levels_sorted

    def connect(self, root: 'Node') -> 'Node':
        levels = self.bfs(root)

        for level in levels.values():
            print(level)
            level.append(None)
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]
                self.unvisit(level[i])
        return root


_7 = Node(val=7)
_5 = Node(val=5)
_4 = Node(val=4)
_3 = Node(val=3, right=_7)
_2 = Node(val=2, left=_4, right=_5)
_1 = Node(val=1, left=_2, right=_3)

s = Solution()
s.connect(_1)
