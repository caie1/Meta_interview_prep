class Solution {
    boolean foundP = false;
    boolean foundQ = false;
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode lca = helper(root, p, q);
        System.out.print(foundQ);
        return (this.foundP && this.foundQ ? lca : null);
    }
    
    private TreeNode helper(TreeNode node, TreeNode p, TreeNode q){
        if (node == null) return null;
        
        TreeNode left = helper(node.left, p, q);
        TreeNode right = helper(node.right, p, q);
        
        if (node.val == p.val){
            this.foundP = true;
            return node;
        }
        if (node.val == q.val){
            this.foundQ = true;
            return node;
        }
         
        
        if ((left != null) && (right != null)) return node;
        
        return (left != null ? left : right);
    }
}
