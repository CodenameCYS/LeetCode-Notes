/*
=== 718. Maximum Length of Repeated Subarray ===

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
    Input:
    A: [1,2,3,2,1]
    B: [3,2,1,4,7]
    Output: 3
    Explanation: 
    The repeated subarray with maximum length is [3, 2, 1].
 
Note:
    1. 1 <= len(A), len(B) <= 1000
    2. 0 <= A[i], B[i] < 100
*/
// === 124ms(70.59%) && 9.9MB(100%) === // # 网上找到的dp解法
int findLength(int* A, int ASize, int* B, int BSize){
    int L[ASize+1][BSize+1];
    int i,j,result=0;
    for(i=0;i<=ASize;i++)
    {
        for(j=0;j<=BSize;j++)
        {
            if(i==0 || j==0)
                L[i][j]=0;
            else if(A[i-1] == B[j-1])
            {
                L[i][j]=1+L[i-1][j-1];
                result = result > L[i][j] ? result : L[i][j];
            }
            else
                L[i][j]=0;
        }
    }
    return result;
}

