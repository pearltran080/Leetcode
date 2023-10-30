class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def inorderHelper(node):
            if node is None:
                return

            inorderHelper(node.left)
            result.append(node.val)
            inorderHelper(node.right)

        inorderHelper(root)
        return result