/*
=== 119. Pascal's Triangle II ===

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]

Follow up:
Could you optimize your algorithm to use only O(k) extra space?
*/

# include <stdio.h>
# include <stdlib.h>

int* getRow(int rowIndex, int* returnSize);

int main(){

    int rowIndex = 8;
    int returnSize;
    int* ans = getRow(rowIndex, &returnSize);

    for(int i=0; i<returnSize; ++i){
        printf("%d\t", ans[i]);
    }
    printf("\n");

    system("pause");
    return 1;
}

int* getRow(int rowIndex, int* returnSize) {
    *returnSize = rowIndex + 1;

    int* ans = (int*) malloc(*returnSize * sizeof(int));
    int pascalTriangle[rowIndex+1][rowIndex+1];
    pascalTriangle[0][0] = 1;
    for(int i=1; i<rowIndex; ++i){
        pascalTriangle[i][0] = 1,   pascalTriangle[i][i] = 1;
        for(int j=1; j<i; ++j){
            pascalTriangle[i][j] = pascalTriangle[i-1][j-1] + pascalTriangle[i-1][j];
        }
    }
    ans[0] = 1, ans[rowIndex] = 1;
    for(int i=1; i<rowIndex; ++i){
        ans[i] = pascalTriangle[rowIndex-1][i-1] + pascalTriangle[rowIndex-1][i];
    }

    return ans;
}