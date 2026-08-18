/*
=== 1047. Remove All Adjacent Duplicates In String ===

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

Example 1:
    Input: "abbaca"
    Output: "ca"
    - Explanation: 
    For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
 
Note:
    1. 1 <= S.length <= 20000
    2. S consists only of English lowercase letters.
*/
// === 4ms & 8.6MB === //
char * removeDuplicates(char * S){
    int len = strlen(S);
    char* ans = (char*)malloc((len+1)*sizeof(char));
    int ed = 0;
    for(int i=0; i<len; ++i){
        if(ed == 0){
            ans[ed] = S[i];
            ++ed;
        }
        else{
            if(S[i] == ans[ed-1]){
                --ed;
            }
            else{
                ans[ed] = S[i];
                ++ed;
            }
        }
    }
    ans[ed] = '\0';
    return ans;
}