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
    Map <Integer, ArrayList<Pair<Integer, Integer>>> columnTable = new HashMap<>();
    int minCol = Integer.MAX_VALUE, maxCol = Integer.MIN_VALUE;
    
    private void BFS(TreeNode node){
        Queue <Pair<TreeNode, Pair<Integer, Integer>>> queue = new ArrayDeque<>();
        int row = 0, col = 0;
        queue.offer(new Pair<>(node, new Pair<>(row, col)));
        
        while (!queue.isEmpty()){
            Pair<TreeNode, Pair<Integer, Integer>> p = queue.poll();
            node = p.getKey();
            row = p.getValue().getKey();
            col = p.getValue().getValue();
            
            if (node != null){
                if (!columnTable.containsKey(col)){
                    columnTable.put(col, new ArrayList<Pair<Integer, Integer>>());
                }
                columnTable.get(col).add(new Pair<>(row, node.val));
                minCol = Math.min(minCol, col);
                maxCol = Math.max(maxCol, col);
                
                queue.offer(new Pair<>(node.left, new Pair<>(row + 1, col - 1)));
                queue.offer(new Pair<>(node.right, new Pair<>(row + 1, col + 1)));
            }
        }
    }
    
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        if (root == null) return Collections.emptyList();
        List<List<Integer>> output = new ArrayList<>();
        this.BFS(root);
        
        for (int i = minCol; i < maxCol + 1; i++){
            Collections.sort(columnTable.get(i), new Comparator<Pair<Integer, Integer>>(){
                @Override
                public int compare(Pair<Integer, Integer> p1, Pair<Integer, Integer> p2){
                    if (p1.getKey().equals(p2.getKey())){
                        return p1.getValue() - p2.getValue();
                    }
                    else{
                        return p1.getKey() - p2.getKey();
                    }
                }
            });
            List<Integer> sortedColumn = new ArrayList<>();
            for (Pair<Integer, Integer> p : columnTable.get(i)){
                sortedColumn.add(p.getValue());
            }
            output.add(sortedColumn);
        }
        return output;
    }
}