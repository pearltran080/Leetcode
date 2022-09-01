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
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        if (root.left == null && root.right == null) {
            return 1;
        }
        else if (root.left == null && root.right != null) {
            return 1 + minDepth(root.right);
        }
        else if (root.left != null && root.right == null) {
            return 1 + minDepth(root.left);
        }
        // (root.left != null && root.right != null)
        else {
            int left = 1 + minDepth(root.left);
            int right = 1 + minDepth(root.right);
            if (left > right) {
                return right;
            }
            else {
                return left;
            }
        }
    }
}