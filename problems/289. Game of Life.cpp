/*
=== 289. Game of Life ===

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
- Any live cell with fewer than two live neighbors dies, as if caused by under-population.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by over-population..
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:
Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:
- Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
- In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
*/
// === 4ms(22.58%) & 7.3MB(16.67%) === //
int nextstate(int** board, int boardRowSize, int *boardColSizes, int row, int col){
    int aliveNeighbor = 0;
    for(int i=row-1; i<=row+1; ++i){
        for(int j=col-1; j<=col+1; ++j){
            if(i==row && j==col){
                continue;
            }
            else if(i < 0 || i >= boardRowSize || j < 0 || j >= boardColSizes[i]){
                continue;
            }
            else{
                aliveNeighbor += board[i][j];
            }
        }
    }
    if(board[row][col] == 1){
        return aliveNeighbor<2 || aliveNeighbor>3 ? 0 : 1;
    }
    else{
        return aliveNeighbor==3 ? 1 : 0;
    }
}
void gameOfLife(int** board, int boardRowSize, int *boardColSizes) {
    int** nextboard = (int**)malloc(boardRowSize*sizeof(int*));
    for(int i=0; i<boardRowSize; ++i){
        nextboard[i] = (int*)malloc(boardColSizes[i]*sizeof(int));
        for(int j=0; j<boardColSizes[i]; ++j){
            nextboard[i][j] = nextstate(board, boardRowSize, boardColSizes, i, j);
        }
    }
    for(int i=0; i<boardRowSize; ++i){
        for(int j=0; j<boardColSizes[i]; ++j){
            board[i][j] = nextboard[i][j];
        }
        free(nextboard[i]);
    }
    free(nextboard);
}