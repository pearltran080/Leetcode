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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // will remain unchanged if vals are not identical
        boolean left = false;
        boolean right = false;

        if (p == null && q != null) {
            return false;
        }
        else if (p != null && q == null) {
            return false;
        }
        else if (p == null && q == null) {
            return true;
        }

        else if (p.val == q.val) {
            left = isSameTree(p.left, q.left);
            right = isSameTree(p.right, q.right);
        }

        return (left && right);

    }
}