class Solution {
    private char[][] board;
    private int ROWS;
    private int COLS;
    
    public boolean exist(char[][] board, String word) {
        this.board = board;
        this.ROWS = board.length;
        this.COLS = board[0].length;
        
        for (int i = 0; i < this.ROWS; i++){
            for (int j = 0; j < this.COLS; j++){
                if (dfs(i,j,0,word)) return true;
            }
        }
        return false;
    }
    
    private boolean dfs(int row, int col, int ind, String word){
        if (ind >= word.length()) return true;
        
        if ((row < 0 || row >= this.ROWS) || (col < 0 || col >= this.COLS) || (word.charAt(ind) != this.board[row][col])) return false;
        
        boolean ret = false;
        this.board[row][col] = '#';
        
        int[] rowOffset = {0, -1, 0, 1};
        int[] colOffset = {1, 0, -1, 0};
        
        for (int d = 0; d < 4; d++){
            ret = dfs(row + rowOffset[d], col + colOffset[d], ind + 1, word);
            if (ret) break;
        }
        this.board[row][col] = word.charAt(ind);
        return ret;
    }
}