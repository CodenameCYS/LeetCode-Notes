/*
=== 994. Rotting Oranges ===

In a given grid, each cell can have one of three values:
    - the value 0 representing an empty cell;
    - the value 1 representing a fresh orange;
    - the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
    Input: [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4
Example 2:
    Input: [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:
    Input: [[0,2]]
    Output: 0
    Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:
    1. 1 <= grid.length <= 10
    2. 1 <= grid[0].length <= 10
    3. grid[i][j] is only 0, 1, or 2.
*/
// === 8ms & 8.6MB === //
void count(int** grid, int gridRowSize, int *gridColSizes, int* rottennum, int* orangenum){
    *rottennum = 0, *orangenum = 0;
    for(int row=0; row<gridRowSize; ++row){
        for(int col=0; col<gridColSizes[row]; ++col){
            if(grid[row][col] == 2){
                ++ *rottennum;
                ++ *orangenum;
            }
            else if(grid[row][col] == 1){
                ++ *orangenum;
            }
        }
    }
}
bool isRotten(int** grid, int gridRowSize, int *gridColSizes, int row, int col){
    if(row < 0 || row >= gridRowSize || col < 0 || col >= gridColSizes[row]){
        return false;
    }
    return grid[row][col] == 2;
}
bool isAdjacentToRotten(int** grid, int gridRowSize, int *gridColSizes, int row, int col){
    return isRotten(grid, gridRowSize, gridColSizes, row-1, col) || isRotten(grid, gridRowSize, gridColSizes, row+1, col) 
        || isRotten(grid, gridRowSize, gridColSizes, row, col-1) || isRotten(grid, gridRowSize, gridColSizes, row, col+1);
}
int update(int** grid, int gridRowSize, int *gridColSizes){
    int rottennum = 0;
    int rottingnum = 0;
    int rottinglist[100][2];
    for(int row=0; row<gridRowSize; ++row){
        for(int col=0; col<gridColSizes[row]; ++col){
            if(grid[row][col] == 2){
                ++ rottennum;
            }
            else if(grid[row][col] == 1 && isAdjacentToRotten(grid, gridRowSize, gridColSizes, row, col)){
                rottinglist[rottingnum][0] = row;
                rottinglist[rottingnum][1] = col;
                ++ rottingnum;
            }
        }
    }
    for(int i=0; i<rottingnum; ++i){
        grid[rottinglist[i][0]][rottinglist[i][1]] = 2;
    }
    return rottennum + rottingnum;
}
int orangesRotting(int** grid, int gridRowSize, int *gridColSizes) {
    int rottennum, orangenum;
    count(grid, gridRowSize, gridColSizes, &rottennum, &orangenum);
    
    int time = 0;
    while(true){
        int temp = update(grid, gridRowSize, gridColSizes);
        if(temp == rottennum){
            break;
        }
        else{
            rottennum = temp;
            ++time;
        }
    }
    
    if(rottennum == orangenum){
        return time;
    }
    else{
        return -1;
    }
}