/*
=== 221. Maximal Square ===

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
    Input: 
        1 0 1 0 0
        1 0 1 1 1
        1 1 1 1 1
        1 0 0 1 0
    Output: 4
*/
// === 64ms(5.26%) && 8.7MB(100%) === //
int maximalSquare(char** matrix, int matrixSize, int* matrixColSize){
    if(matrixSize == 0 || matrixColSize[0] == 0){
        return 0;
    }
    int row = matrixSize, col = matrixColSize[0];
    int cumsum[row+1][col+1];
    for(int j=0; j<=col; ++j){
        cumsum[0][j] = 0;
    }
    
    for(int i=1; i<=row; ++i){
        cumsum[i][0] = 0;
        for(int j=1; j<=col; ++j){
            cumsum[i][j] = matrix[i-1][j-1] - '0' + cumsum[i-1][j] + cumsum[i][j-1] - cumsum[i-1][j-1];
        }
    }
    
    int n = row < col ? row : col;
    int ans = 0;
    for(int l=1; l<=n; ++l){
        int size = l*l;
        bool has_square = false;
        for(int i=0; i+l<=row; ++i){
            for(int j=0; j+l<=col; ++j){
                if(cumsum[i+l][j+l] + cumsum[i][j] - cumsum[i+l][j] - cumsum[i][j+l] == size){
                    has_square = true;
                    break;
                }
            }
            if(has_square){
                ans = size;
                break;
            }
        }
    }
    return ans;
}

