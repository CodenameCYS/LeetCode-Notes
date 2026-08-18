/*
=== 955. Delete Columns to Make Sorted II ===

We are given an array A of N lowercase letter strings, all of the same length.
Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.
For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef","vyz"].
Suppose we chose a set of deletion indices D such that after deletions, the final array has its elements in lexicographic order (A[0] <= A[1] <= A[2] ... <= A[A.length - 1]).
Return the minimum possible value of D.length.

Example 1:
Input: ["ca","bb","ac"]
Output: 1
Explanation: 
After deleting the first column, A = ["a", "b", "c"].
Now A is in lexicographic order (ie. A[0] <= A[1] <= A[2]).
We require at least 1 deletion since initially A was not in lexicographic order, so the answer is 1.

Example 2:
Input: ["xc","yb","za"]
Output: 0
Explanation: 
A is already in lexicographic order, so we don't need to delete anything.
Note that the rows of A are not necessarily in lexicographic order:
ie. it is NOT necessarily true that (A[0][0] <= A[0][1] <= ...)

Example 3:
Input: ["zyx","wvu","tsr"]
Output: 3
Explanation: 
We have to delete every column.
 
Note:
1. 1 <= A.length <= 100
2. 1 <= A[i].length <= 100
*/
int minDeletionSize(char** A, int ASize) {
    int len = strlen(A[0]);
    
    // state用于表示间隔，间隔为1时无需再继续判断前后两个元素间的字符连续关系，因为后续的字符顺序已经不会再影响词的顺序。
    int state[ASize];
    state[0] = ASize-1;
    for(int i=1; i<ASize; ++i){
        state[i] = 0;
    }
    
    int ans = 0;
    
    for(int j=0; j<len; ++j){
        bool is_alphabetic = true;
        for(int i=1; i<ASize; ++i){
            if(state[i] == 1){
                continue;
            }
            if(A[i-1][j] > A[i][j]){
                is_alphabetic = false;
                break;
            }
        }
        if(is_alphabetic){
            for(int i=1; i<ASize; ++i){
                if(state[i] == 0 && A[i-1][j] < A[i][j]){
                    state[i] = 1;
                    -- state[0];
                    if(state[0] == 0){
                        return ans;
                    }
                }
            }
        }
        else{
            ++ ans;
        }
    }
    
    return ans;
}