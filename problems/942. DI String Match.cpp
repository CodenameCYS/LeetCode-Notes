/*
=== 942. DI String Match ===

Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
- If S[i] == "I", then A[i] < A[i+1]
- If S[i] == "D", then A[i] > A[i+1]
 
Example 1:
Input: "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: "III"
Output: [0,1,2,3]

Example 3:
Input: "DDI"
Output: [3,2,0,1]
 
Note:
1. 1 <= S.length <= 10000
2. S only contains characters "I" or "D".
*/
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* diStringMatch(char* S, int* returnSize) {
    int len = 0;
    int Dnum = 0;
    while(S[len]){
        if(S[len] == 'D'){
            ++ Dnum;
        }
        ++len;
    }
    *returnSize = len + 1;
    int* ans = (int*)malloc((*returnSize)*sizeof(int));
    int ivalue = len, dvalue = 0;
    for(int i=len; i>0; --i){
        if(S[i-1] == 'D'){
            ans[i] = dvalue;
            ++ dvalue;
        }
        else{
            ans[i] = ivalue;
            -- ivalue;
        }
    }
    ans[0] = ivalue;
    return ans;
}