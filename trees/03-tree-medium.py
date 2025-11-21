from __future__ import annotations

from collections import deque


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Node | None = None,
        right: Node | None = None,
        next: Node | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.left = left
        self.right = right
        self.val = val


class Solution:
    def connectM1(self, root: Node | None) -> Node | None:
        """
        Populating Next Right Pointers in Each Node
        Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

        You are given a perfect binary tree where all leaves are on the
        same level, and every parent has two children. The binary tree
        has the following definition:

        struct Node {
            int val;
            Node *left;
            Node *right;
            Node *next;
        }

        Populate each next pointer to point to its next right node. If
        there is no next right node, the next pointer should be set to NULL.

        Initially, all next pointers are set to NULL.
        """
        if not root:
            return root

        leftmost = root
        while leftmost.left:
            current = leftmost
            while current:
                current.left.next = (  # pyright: ignore[reportOptionalMemberAccess]
                    current.right
                )
                if current.next:
                    current.right.next = (  # pyright: ignore[reportOptionalMemberAccess]
                        current.next.left
                    )
                current = current.next
            leftmost = leftmost.left

        return root

    def connectM2(self, root: Node | None) -> Node | None:
        """
        Previous question via BFS and extra space in the form of queue.
        """
        if root is None:
            return root

        queue = deque([root])
        while queue:
            nextL = []
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size - 1:
                    node.next = queue[0]
                if node.left:
                    nextL.append(node.left)
                if node.right:
                    nextL.append(node.right)
            queue = deque(nextL)
        return root

    def maxPathSum(self, root: TreeNode | None) -> int:
        """
        Binary Tree Maximum Path Sum
        Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

        Given the root of a binary tree, return the maximum path sum of any non-empty path.
        """

        def dfs(node: TreeNode | None):
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            nonlocal max_path_sum
            max_path_sum = max(max_path_sum, node.val + left + right)

            return node.val + max(left, right)

        max_path_sum = float("-inf")
        dfs(root)
        return max_path_sum  # pyright: ignore[reportReturnType]
