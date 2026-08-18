/*
=== 944. Delete Columns to Make Sorted ===

We are given an array A of N lowercase letter strings, all of the same length.
Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.
For example, if we have a string "abcdef" and deletion indices {0, 2, 3}, then the final string after deletion is "bef".
Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.
Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]]
Return the minimum possible value of D.length.

Example 1:
Input: ["cba","daf","ghi"]
Output: 1

Example 2:
Input: ["a","b"]
Output: 0

Example 3:
Input: ["zyx","wvu","tsr"]
Output: 3
 
Note:
1. 1 <= A.length <= 100
2. 1 <= A[i].length <= 1000
*/
int minDeletionSize(char** A, int ASize) {
    int ans = 0;
    for(int i=0; A[0][i]!='\0'; ++i){
        bool state = true;
        int v = A[0][i];
        for(int j=1; j<ASize; ++j){
            if(A[j][i] >= v){
                v = A[j][i];
            }
            else{
                state = false;
                break;
            }
        }
        if(!state){
            ++ ans;
        }
    }
    return ans;
}