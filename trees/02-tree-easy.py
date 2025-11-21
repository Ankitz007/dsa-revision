from __future__ import annotations


# Another way to define it!
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
    def goodNodes(self, root: TreeNode) -> int:
        """
        Count Good Nodes in Binary Tree

        Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

        Given a binary tree root, a node X in the tree is
        named good if in the path from root to X there are
        no nodes with a value greater than X.

        Return the number of good nodes in the binary tree.
        """

        def dfs(node: TreeNode | None, max_value: int):
            if not node:
                return

            # See how nonlocal is used!
            # The nonlocal keyword in Python is used within nested functions
            # to indicate that a variable refers to a previously bound variable
            # in the nearest enclosing but non-global scope. This allows
            # modification of variables in an outer function from within an
            # inner function without making them global.
            nonlocal good_nodes
            if node.val >= max_value:
                good_nodes += 1
                max_value = node.val

            dfs(node.left, max_value)
            dfs(node.right, max_value)

        good_nodes = 0
        dfs(root, root.val)
        return good_nodes

    def isSymmetric(self, root: TreeNode) -> bool:
        """
        Symmetric Tree
        Link: https://leetcode.com/problems/symmetric-tree/description/

        Given the root of a binary tree, check whether it is
        a mirror of itself (i.e., symmetric around its center).
        """

        def dfs(leftNode: TreeNode | None, rightNode: TreeNode | None):
            # Both are none, cool!
            if not leftNode and not rightNode:
                return True

            # One of them is none, not cool!
            if leftNode is None or rightNode is None:
                return False

            # Values and subtrees check
            return (
                leftNode.val == rightNode.val
                and dfs(leftNode.left, rightNode.right)
                and dfs(leftNode.right, rightNode.left)
            )

        return dfs(root.left, root.right)

    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        """
        Binary Tree Paths
        Link: https://leetcode.com/problems/binary-tree-paths/description/

        Given the root of a binary tree, return all root-to-leaf paths in any order.
        """

        def dfs(node: TreeNode | None, path: list[str]):
            if node is None:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                paths.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            path.pop()

        paths = []
        dfs(root, [])
        return paths

    def sumEvenGrandparent(self, root: TreeNode | None) -> int:
        """
        Sum of Nodes with Even-Valued Grandparent
        Link: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/

        Given the root of a binary tree, return the sum of values of nodes with
        an even-valued grandparent. If there are no nodes with an even-valued
        grandparent, return 0.
        """

        def dfs(node: TreeNode | None, p: TreeNode | None, gp: TreeNode | None):
            if not node:
                return 0

            result = 0
            # Actually, we don't need to check p!
            if gp and not gp.val % 2:
                result += node.val

            result += dfs(node.left, node, p)
            result += dfs(node.right, node, p)

            return result

        return dfs(root, None, None)

    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        """
        Subtree of Another Tree
        Link: https://leetcode.com/problems/subtree-of-another-tree/description/

        Given the roots of two binary trees root and subRoot, return true
        if there is a subtree of root with the same structure and node
        values of subRoot and false otherwise.

        A subtree of a binary tree tree is a tree that consists of a node
        in tree and all of this node's descendants. The tree tree could
        also be considered as a subtree of itself.
        """

        def isSame(p: TreeNode | None, q: TreeNode | None):
            """
            This checks if two trees are identical.
            """
            if not (p and q):
                return p is None and q is None

            return (
                p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)
            )

        if root is None:
            return False

        # If both are already same, return true!
        if isSame(root, subRoot):
            return True

        # Check tree1's subtrees for a match!
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def maxPathSum(self, root: TreeNode | None):
        """
        Maximum sum leaf to root path
        Link: http://geeksforgeeks.org/problems/maximum-sum-leaf-to-root-path/1

        Given a Binary Tree, find the maximum sum path from a leaf to root.
        """

        def dfs(node: TreeNode | None):
            # Pretty easy except this condition:
            # Try the example [10, N, -20, -30] whose
            # expected output is -40.
            if not node:
                return float("-inf")
            if not node.left and not node.right:
                return node.val
            left = dfs(node.left)
            right = dfs(node.right)
            return node.val + max(left, right)

        return dfs(root)
