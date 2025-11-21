from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def preorderTraversalM1(self, root: TreeNode | None) -> List[int]:
        """
        Preorder Traversal using recursion
        Link: https://leetcode.com/problems/binary-tree-preorder-traversal/description/

        Given the root of a binary tree, return the preorder traversal
        of its nodes' values.
        """

        def traverse(node: TreeNode | None):
            # Early termination, generally a good practice.
            if not node:
                return
            preorder.append(node.val)
            traverse(node.left)
            traverse(node.right)

        # preorder list's scope is global so accessible
        # across recursive stack layers
        preorder = []
        traverse(root)
        return preorder

    def preorderTraversalM2(self, root: TreeNode | None) -> List[int]:
        """
        Preorder Traversal using a stack
        """
        stack, preorder = [root], []
        while stack:
            node = stack.pop()
            # Early termination!
            if not node:
                continue
            preorder.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return preorder

    def inorderTraversalM1(self, root: TreeNode | None) -> List[int]:
        """
        Inorder traversal using recursion
        Link: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

        Given the root of a binary tree, return the inorder traversal
        of its nodes' values.
        """

        def traverse(node: TreeNode | None):
            # Again, early termination!
            # Helps with the indentation too - lesser the better
            if not node:
                return
            traverse(node.left)
            inorder.append(node.val)
            traverse(node.right)

        inorder = []
        traverse(root)
        return inorder

    def inorderTraversalM2(self, root: TreeNode | None) -> List[int]:
        """
        Inorder traversal using a stack
        """
        inorder, node = [], root
        # The annotation helps the type checker to
        # infer that stack.pop() will not be None
        stack: List[TreeNode] = []
        # This while condition takes care of both:
        # an empty stack as well as backtracking to parent
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            inorder.append(node.val)
            node = node.right
        return inorder

    def postorderTraversalM1(self, root: TreeNode | None) -> List[int]:
        """
        Postorder Traversal using recursion
        Link: https://leetcode.com/problems/binary-tree-postorder-traversal/description/

        Given the root of a binary tree, return the postorder traversal
        of its nodes' values.
        """

        def traverse(node: TreeNode | None):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            postorder.append(node.val)

        postorder = []
        traverse(root)
        return postorder

    def postorderTraversalM2(self, root: TreeNode | None) -> List[int]:
        """
        Postorder Traversal using stacks
        """
        stack, postorder = [root], []
        while stack:
            node = stack.pop()
            if not node:
                continue

            postorder.append(node.val)
            stack.append(node.left)
            stack.append(node.right)

        postorder.reverse()
        return postorder

    def levelOrderM1(self, root: TreeNode | None) -> List[List[int]]:
        """
        Iterative level order traversal of a binary tree
        Link: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

        Given the root of a binary tree, return the level order traversal
        of its nodes' values. (i.e., from left to right, level by level).
        """
        result = []
        if not root:
            return result

        queue = deque([root])
        while queue:
            currentLevel = []
            for _ in range(len(queue)):
                node = queue.popleft()
                currentLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(currentLevel)
        return result
