# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []

        def preorderHelp(node):
            if node is None:
                return

            result.append(node.val)
            preorderHelp(node.left)
            preorderHelp(node.right)

        preorderHelp(root)
        return result