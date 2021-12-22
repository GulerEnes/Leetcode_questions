# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def isOK(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is not None and node2 is not None and node1.val == node2.val:
            flag1 = self.isOK(node1.left, node2.left)
            flag2 = self.isOK(node1.right, node2.right)
            return flag1 and flag2
        return False

    def isSubtree(self, root, subRoot):
        if root is None:
            return False
        if root.val == subRoot.val and self.isOK(root, subRoot):
            return True
        flag1 = self.isSubtree(root.left, subRoot)
        flag2 = self.isSubtree(root.right, subRoot)

        return flag1 or flag2


_0t = TreeNode(val=0)
_1t = TreeNode(val=1)
_2t = TreeNode(val=2, right=_0t)
_5t = TreeNode(val=5)
_4t = TreeNode(val=4, left=_1t, right=_2t)
_3t = TreeNode(val=3, left=_4t, right=_5t)

r = _3t

_1s = TreeNode(val=1)
_2s = TreeNode(val=2)
_4s = TreeNode(val=4, left=_1s, right=_2s)

s = _4s

sol = Solution()

print(sol.isSubtree(r, s))
