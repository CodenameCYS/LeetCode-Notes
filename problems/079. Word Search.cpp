/*
=== 79. Word Search ===

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:
    board =
    [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    Given word = "ABCCED", return true.
    Given word = "SEE", return true.
    Given word = "ABCB", return false.
 
Constraints:
    1. board and word consists only of lowercase and uppercase English letters.
    2. 1 <= board.length <= 200
    3. 1 <= board[i].length <= 200
    4. 1 <= word.length <= 10^3
*/
int** build_state(int rowSize, int colSize){
    int** state = (int**)malloc(rowSize*sizeof(int*));
    for(int i=0; i<rowSize; ++i){
        state[i] =  (int*)malloc(colSize*sizeof(int));
        for(int j=0; j<colSize; ++j){
            state[i][j] = 0;
        }
    }
    return state;
}

void free_state(int** state, int rowSize){
    for(int i=0; i<rowSize; ++i){
        free(state[i]);
    }
    free(state);
}

bool find_word(char** board, int** state, int rowSize, int colSize, char * word, int row, int col){
    // printf("need find: %s, next char is %c\n", &word[1], word[1]);
    state[row][col] = 1;
    char next_char = word[1];
    if(next_char == '\0'){
        state[row][col] = 0;
        return true;
    }
    bool ans = false;
    if(row-1>=0 && state[row-1][col]==0 && board[row-1][col]==next_char){
        ans = ans || find_word(board, state, rowSize, colSize, &word[1], row-1, col);
    }
    if(row+1<rowSize && state[row+1][col]==0 && board[row+1][col]==next_char){
        ans = ans || find_word(board, state, rowSize, colSize, &word[1], row+1, col);
    }
    if(col-1>=0 && state[row][col-1]==0 && board[row][col-1]==next_char){
        ans = ans || find_word(board, state, rowSize, colSize, &word[1], row, col-1);
    }
    if(col+1<colSize && state[row][col+1]==0 && board[row][col+1]==next_char){
        ans = ans || find_word(board, state, rowSize, colSize, &word[1], row, col+1);
    }
    state[row][col] = 0;
    return ans;
}
// === 12ms(100%) && 6.8MB(100%) === //
bool exist(char** board, int boardSize, int* boardColSize, char * word){
    if(word[0] == '\0'){
        return true;
    }
    
    int** state = build_state(boardSize, *boardColSize);
    for(int i=0; i<boardSize; ++i){
        for(int j=0; j<*boardColSize; ++j){
            if(board[i][j] == word[0] && find_word(board, state, boardSize, *boardColSize, word, i, j)){
                free(state);
                return true;
            }
        }
    }
    free(state);
    return false;
}

