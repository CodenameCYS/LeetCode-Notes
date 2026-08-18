/*
=== 14. Longest Common Prefix ===

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
    Input: ["flower","flow","flight"]
    Output: "fl"
Example 2:
    Input: ["dog","racecar","car"]
    Output: ""
    - Explanation: There is no common prefix among the input strings.

Note:
    1. All given inputs are in lowercase letters a-z.
*/
char * my_copy(char* str){
    int n = strlen(str);
    char* ans = (char*)malloc((n+1)*sizeof(char));
    for(int i=0; i<n; ++i){
        ans[i] = str[i];
    }
    ans[n] = '\0';
    return ans;
}
// === 4ms(64.71%) && 7.1MB(87.50%) === //
char * longestCommonPrefix(char ** strs, int strsSize){
    if(strsSize == 0){
        char* ans = (char*)malloc(sizeof(char));
        ans[0] = '\0';
        return ans;
    }
    if(strsSize == 1){
        return my_copy(strs[0]);
    }
    char* ans = my_copy(strs[0]);
    int n = strlen(ans);
    for(int i=1; i<strsSize; ++i){
        for(int j=0; j<n; ++j){
            if(ans[j] != strs[i][j]){
                ans[j] = '\0';
                n = j;
            }
        }
    }
    return ans;
}

