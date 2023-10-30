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
    private List<Integer> sums = new ArrayList<Integer>();

    public boolean hasPathSum(TreeNode root, int targetSum) {

        if (root == null) { return false; }

        sumHelper(root, 0);

        if (sums.contains(targetSum)) { return true; }
        return false;
    }

    private void sumHelper(TreeNode node, int sum) {
        if (node == null) { return; }

        if (node.left == null && node.right == null) {
            sums.add(sum+node.val);
            return;
        }

        sumHelper(node.left, sum+node.val);
        sumHelper(node.right, sum+node.val);
    }
}