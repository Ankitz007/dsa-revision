from __future__ import annotations

from collections import deque


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightViewM1(self, root: TreeNode):
        """
        Right View of Binary Tree
        Link: https://www.geeksforgeeks.org/problems/right-view-of-binary-tree/1

        Given the root of a binary Tree. Your task is to return the
        right view of the binary tree. The right view of a Binary
        Tree is the set of nodes visible when the tree is viewed
        from the right side.

        Note: Can also be done via DFS, similar to below.
        """
        queue = deque([(root, 0)])
        result = []
        while queue:
            node, level = queue.popleft()

            # This is a neat trick to avoid having much more
            # space usage if we were to save all nodes!
            if len(result) == level:
                result.append(node.val)

            # Check how we reversed the traversal to go to
            # right subtree first!
            if node.right:
                queue.append((node.right, level + 1))
            if node.left:
                queue.append((node.left, level + 1))

        return result

    def leftView(self, root: TreeNode):
        """
        Left View of Binary Tree via DFS

        Note: Can also be done via BFS, similar to above.
        """

        def dfs(node: TreeNode | None, level: int):
            if not node:
                return

            if level == len(result):
                result.append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        result = []
        dfs(root, 0)
        return result

    def topView(self, root: TreeNode):
        """
        Top View of Binary Tree via BFS
        Link: https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1

        You are given the root of a binary tree, and your task is
        to return its top view. The top view of a binary tree is
        the set of nodes visible when the tree is viewed from the top.
        """
        queue = deque([(root, 0)])
        # The usage of this is tricky!
        # You can actually use max_x as well.
        # And then result will be formed
        # using range(mix_x, max_x)
        min_x = 0
        level_map = {}
        while queue:
            node, x = queue.popleft()
            # Tracking min_x
            min_x = min(min_x, x)

            if x not in level_map:
                level_map[x] = node.val
            if node.left:
                queue.append((node.left, x - 1))
            if node.right:
                queue.append((node.right, x + 1))

        result = [0] * len(level_map)
        for key, value in level_map.items():
            # See the usage, damn!
            result[key - min_x] = value

        return result

    def topViewM2(self, root: TreeNode):
        def dfs(node: TreeNode | None, x, y):
            if not node:
                return

            if x not in level_map or level_map[x][1] > y:
                level_map[x] = (node.val, y)

            if node.left:
                dfs(node.left, x - 1, y + 1)

            if node.right:
                dfs(node.right, x + 1, y + 1)

        level_map = {}
        dfs(root, 0, 0)
        result = []

        for key in sorted(level_map.keys()):
            result.append(level_map[key][0])

        return result

    def bottomView(self, root: TreeNode):
        """
        Bottom View of Binary Tree
        Link: https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

        You are given the root of a binary tree, and your task is
        to return its bottom view. The bottom view of a binary
        tree is the set of nodes visible when the tree is viewed
        from the bottom.
        """
        queue = deque([(root, 0)])
        min_x = 0
        level_map = {}
        while queue:
            node, x = queue.popleft()

            min_x = min(min_x, x)
            # The only change is this, lol!
            level_map[x] = node.val

            if node.left:
                queue.append((node.left, x - 1))
            if node.right:
                queue.append((node.right, x + 1))

        result = [0] * len(level_map)
        for key, value in level_map.items():
            result[key - min_x] = value

        return result
