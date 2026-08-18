/*
=== 794. Valid Tic-Tac-Toe State ===

A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.
The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.
Here are the rules of Tic-Tac-Toe:
    1. Players take turns placing characters into empty squares (" ").
    2. The first player always places "X" characters, while the second player always places "O" characters.
    3. "X" and "O" characters are always placed into empty squares, never filled ones.
    4. The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
    5. The game also ends if all squares are non-empty.
    6. No more moves can be played if the game is over.

Example 1:
    Input: board = ["O  ", "   ", "   "]
    Output: false
    Explanation: The first player always plays "X".
Example 2:
    Input: board = ["XOX", " X ", "   "]
    Output: false
    Explanation: Players take turns making moves.
Example 3:
    Input: board = ["XXX", "   ", "OOO"]
    Output: false
Example 4:
    Input: board = ["XOX", "O O", "XOX"]
    Output: true

Note:
    1. board is a length-3 array of strings, where each string board[i] has length 3.
    2. Each board[i][j] is a character in the set {" ", "X", "O"}.
*/
int count_line(char ** board, int boardSize, char c){
    int line = 0;
    for(int i=0; i<3; ++i){
        if(board[i][0]==c && board[i][1]==c && board[i][2]==c){
            ++ line;
        }
        if(board[0][i]==c && board[1][i]==c && board[2][i]==c){
            ++ line;
        }
    }
    if(board[0][0]==c && board[1][1]==c && board[2][2]==c){
        ++ line;
    }
    if(board[2][0]==c && board[1][1]==c && board[0][2]==c){
        ++ line;
    }
    return line;
}
// === 0ms(1000%) && 5.2MB(100%) === //
bool validTicTacToe(char ** board, int boardSize){
    int x_num=0, o_num=0;
    for(int i=0; i<3; ++i){
        for(int j=0; j<3; ++j){
            if(board[i][j] == 'X'){
                ++ x_num;
            }
            else if(board[i][j] == 'O'){
                ++ o_num;
            }
        }
    }
    if(x_num-o_num<0 || x_num-o_num>1){
        return false;
    }
    int x_line = count_line(board, boardSize, 'X');
    int o_line = count_line(board, boardSize, 'O');
    if(x_line * o_line != 0){
        return false;
    }
    else if(x_line > 0){
        return x_num - o_num == 1;
    }
    else if(o_line > 0){
        return x_num - o_num == 0;
    }
    else{
        return true;
    }
}

