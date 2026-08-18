/*
=== 1030. Matrix Cells in Distance Order ===

We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.
Additionally, we are given a cell in that matrix with coordinates (r0, c0).
Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest distance to largest distance.  Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.  (You may return the answer in any order that satisfies this condition.)

Example 1:
    Input: R = 1, C = 2, r0 = 0, c0 = 0
    Output: [[0,0],[0,1]]
    - Explanation: The distances from (r0, c0) to other cells are: [0,1]
Example 2:
    Input: R = 2, C = 2, r0 = 0, c0 = 1
    Output: [[0,1],[0,0],[1,1],[1,0]]
    - Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2]
    The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
Example 3:
    Input: R = 2, C = 3, r0 = 1, c0 = 2
    Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
    - Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2,2,3]
    There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].
 
Note:
    1. 1 <= R <= 100
    2. 1 <= C <= 100
    3. 0 <= r0 < R
    4. 0 <= c0 < C
*/
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int cal_maxdistance(int R, int C, int r0, int c0){
    int ans = r0 + c0;
    int d1 = abs(R-1-r0) + c0;
    ans = ans > d1 ? ans : d1;
    int d2 = abs(R-1-r0) + abs(C-1-c0);
    ans = ans > d2 ? ans : d2;
    int d3 = r0 + abs(C-1-c0);
    return ans > d3 ? ans : d3;
}

void add_point(int r, int c, int R, int C, int** ans, int** columnSizes, int* returnSize){
    if(r>=0 && r<R && c>=0 && c<C){
        ans[*returnSize] = (int*)malloc(2*sizeof(int));
        ans[*returnSize][0] = r;
        ans[*returnSize][1] = c;
        columnSizes[0][*returnSize] = 2;
        ++ *returnSize;
    }
}
// === 112ms & 21.2MB === //
int** allCellsDistOrder(int R, int C, int r0, int c0, int** columnSizes, int* returnSize) {
    *returnSize = 0;
    int** ans = (int**)malloc(R*C*sizeof(int*));
    *columnSizes = (int*)malloc(R*C*sizeof(int));
    int maxdistance = cal_maxdistance(R, C, r0, c0);
    add_point(r0, c0, R, C, ans, columnSizes, returnSize);
    for(int i=1; i<=maxdistance; ++i){
        for(int j=0; j<i; ++j){
            add_point(r0+j, c0+i-j, R, C, ans, columnSizes, returnSize);
            add_point(r0+i-j, c0-j, R, C, ans, columnSizes, returnSize);
            add_point(r0-j, c0-i+j, R, C, ans, columnSizes, returnSize);
            add_point(r0-i+j, c0+j, R, C, ans, columnSizes, returnSize);
        }
    }
    return ans;
}