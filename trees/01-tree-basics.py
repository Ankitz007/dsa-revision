# One way to define it!
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """
        Maximum Depth/Height of Binary Tree
        Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

        Given the root of a binary tree, return its maximum depth.
        """
        if not root:
            return 0

        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)

        return 1 + max(leftHeight, rightHeight)

    def minDepth(self, root: TreeNode | None) -> int:
        """
        Minimum Depth of Binary Tree
        Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

        Given a binary tree, find its minimum depth.

        The minimum depth is the number of nodes along the shortest
        path from the root node down to the nearest leaf node.
        """
        if not root:
            return 0

        if root.left is None or root.right is None:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        """
        Diameter of a Binary Tree
        Link: https://leetcode.com/problems/diameter-of-binary-tree/description/

        Given the root of a binary tree, return the length of the diameter
        of the tree.

        The diameter of a binary tree is the length of the longest path between
        any two nodes in a tree. This path may or may not pass through the root.

        The length of a path between two nodes is represented by the number of
        edges between them.
        """
        # If there is only one node, diameter will be 0
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            leftH = dfs(node.left)
            rightH = dfs(node.right)

            self.diameter = max(self.diameter, leftH + rightH)

            return 1 + max(leftH, rightH)

        dfs(root)
        return self.diameter

    def isBalanced(self, root: TreeNode | None) -> bool:
        """
        Balanced Binary Tree
        Link: https://leetcode.com/problems/balanced-binary-tree/description/

        Given a binary tree, determine if it is height-balanced.

        A height-balanced binary tree is a binary tree in which the
        depth of the two subtrees of every node never differs by more
        than one.
        """

        def dfs(node: TreeNode | None):
            if not node:
                return 0

            leftHeight = dfs(node.left)
            if leftHeight == -1:
                return -1

            rightHeight = dfs(node.right)
            if rightHeight == -1:
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1

            return 1 + max(leftHeight, rightHeight)

        return dfs(root) != -1

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        Same Tree
        Link: https://leetcode.com/problems/same-tree/description/

        Given the roots of two binary trees p and q, write a function
        to check if they are the same or not.

        Two binary trees are considered the same if they are
        structurally identical, and the nodes have the same value.
        """
        if p is None or q is None:
            return p is None and q is None

        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
            and p.val == q.val
        )
