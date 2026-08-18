/*
=== 821. Shortest Distance to a Character ===

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:
    Input: S = "loveleetcode", C = 'e'
    Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 
Note:
    1. S string length is in [1, 10000].
    2. C is a single character, and guaranteed to be in string S.
    3. All letters in S and C are lowercase.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int min(x, y){
    return x < y ? x : y;
}
// === 4ms(100%) && 6MB(100%) === //
int* shortestToChar(char * S, char C, int* returnSize){
    int n = strlen(S);
    int flag[n+2], size=1;
    flag[0] = -10000;
    for(int i=0; i<n; ++i){
        if(S[i] == C){
            flag[size] = i;
            ++ size;
        }
    }
    flag[size] = 20001;
    int* ans = (int*)malloc(n * sizeof(int));
    *returnSize = n;
    int sflag = 0;
    for(int i=0; i<n; ++i){
        if(i >= flag[sflag+1]){
            ans[i] = 0;
            ++ sflag;
        }
        else{
            ans[i] = min(i-flag[sflag], flag[sflag+1] - i);
        } 
    }
    return ans;
}