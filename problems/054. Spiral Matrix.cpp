/*
=== 54. Spiral Matrix ===

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
    Input:
    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]
Example 2:
    Input:
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int** initial_state_matrix(int m, int n){
    int** state = (int**)malloc(m*sizeof(int*));
    for(int i=0; i<m; ++i){
        state[i] = (int*)malloc(n*sizeof(int));
        for(int j=0; j<n; ++j){
            state[i][j] = 0;
        }
    }
    return state;
}

int go_straight(int** matrix, int* ans, int* flag, int m, int n, int** state, int direction, int* row, int* col){
    if(direction == 0){
        while(*col<n && state[*row][*col] == 0){
            state[*row][*col] = 1;
            ans[*flag] = matrix[*row][*col];
            ++ *flag;
            ++ *col;
        }
        -- *col;
        ++ *row;
    }
    else if(direction == 1){
        while(*row<m && state[*row][*col] == 0){
            state[*row][*col] = 1;
            ans[*flag] = matrix[*row][*col];
            ++ *flag;
            ++ *row;
        }
        -- *row;
        -- *col;
    }
    else if(direction == 2){
        while(*col>=0 && state[*row][*col] == 0){
            state[*row][*col] = 1;
            ans[*flag] = matrix[*row][*col];
            ++ *flag;
            -- *col;
        }
        ++ *col;
        -- *row;
    }
    else{
        while(*row>=0 && state[*row][*col] == 0){
            state[*row][*col] = 1;
            ans[*flag] = matrix[*row][*col];
            ++ *flag;
            -- *row;
        }
        ++ *row;
        ++ *col;
    }
    return (direction + 1) % 4;
}
// === 5ms(57.38%) && 7MB(100%) === //
int* spiralOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize){
    int* ans = NULL;
    int m = matrixSize;
    if(m == 0){
        *returnSize = 0;
        return ans;
    }
    int n = matrixColSize[0];
    if(n == 0){
        *returnSize = 0;
        return ans;
    }
    *returnSize = m * n;
    ans = (int*) malloc(*returnSize * sizeof(int));
    int** state = initial_state_matrix(m, n);
    int flag = 0;
    int direction[4] = {0,1,2,3}, tmp = 0;
    int col=0, row=0;
    while(flag < *returnSize){
        // printf("direction = %d\t", tmp);
        tmp = go_straight(matrix, ans, &flag, m, n, state, tmp, &row, &col);
        // printf("walked %d steps.\n", flag);
    }
    return ans;
}

