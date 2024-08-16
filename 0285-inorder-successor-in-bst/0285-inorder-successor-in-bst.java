/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    TreeNode res = null;
    
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if (root == null) return null;
        helper(root, p);
        return res;
    }
    
    private void helper(TreeNode node, TreeNode p){
        if (node == null) return;
        if (node.val > p.val){
            res = node;
            helper(node.left, p);
        }
        else{
            helper(node.right, p);
        }
    }
}