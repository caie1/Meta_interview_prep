/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
};
*/

class Solution {
    public Node lowestCommonAncestor(Node p, Node q) {
        Node p1 = p, p2 = q;
        
        while (p1 != p2){
            p1 = (p1.parent != null) ? p1.parent : q;
            p2 = (p2.parent != null) ? p2.parent : p;
        }
        return p1;
    }
}