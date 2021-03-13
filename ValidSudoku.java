class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean validBoard = true;

        for (int r=0; r<9; r++){
            for (int c=0; c < 9; c++){
                if (board[r][c] != '.'){
                    char num = board[r][c];
                    boolean validRow = checkRow(board, r, num);
                    boolean validCol = checkCol(board, c, num);
                    boolean validBox = checkBox(board, r, c, num);
                    if (!(validRow) || !(validCol) || !(validBox)) validBoard = false;
                }
            }
        }
        return validBoard;
    }

    public boolean checkRow (char[][] b, int row, char n){
        int count = 0;
        for (int i=0; i < b[row].length; i++){
            if ((b[row][i]) == n){
                count++;
            }

        }

        if (count > 1) return false;
        return true;
    }

    public boolean checkCol (char[][] b, int col, char n){
        int count = 0;
        for (int i=0; i < b.length; i++){
            if ((b[i][col]) == n){
                count++;
            }
        }
        if (count > 1) return false;
            return true;
    }

    public boolean checkBox (char[][] b, int row, int col, char n){
        int r = row - (row % 3);
        int c = col - (col % 3);
        int count = 0;

        for (int i = r; i < r+3; i++){
            for (int j = c; j < c+3; j++){
                if (b[i][j] == n){
                    count++;
                }
            }
        }

        if (count > 1) return false;
        return true;
    }
}
