# 543. Diameter of Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def dfs(node) -> int:
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(2 + left + right, self.diameter)

            return 1 + max(left, right)

        dfs(root)

        return self.diameter
