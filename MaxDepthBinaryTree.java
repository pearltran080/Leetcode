/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        if (root.left == null && root.right == null) {
            return 1;
        }
        else if (root.left == null && root.right != null) {
            return 1 + maxDepth(root.right);
        }
        else if (root.left != null && root.right == null) {
            return 1 + maxDepth(root.left);
        }
        // (root.left != null && root.right != null)
        else {
            int left = 1 + maxDepth(root.left);
            int right = 1 + maxDepth(root.right);
            if (left > right) {
                return left;
            }
            else {
                return right;
            }
        }
    }
}