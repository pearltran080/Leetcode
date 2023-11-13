# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def countHelper(root):
            if root is not None:
                return 1 + countHelper(root.left) + countHelper(root.right)
            else:
                return 0

        return countHelper(root)