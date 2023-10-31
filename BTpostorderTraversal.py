# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        result = []

        def postorderHelp(node):
            if node is None:
                return

            postorderHelp(node.left)
            postorderHelp(node.right)
            result.append(node.val)

        postorderHelp(root)
        return result