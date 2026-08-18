/*
=== 647. Palindromic Substrings ===

Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
    Input: "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
    Input: "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 
Note:
    1. The input string length won't exceed 1000.
*/
bool is_palindrome(char* s, int st, int ed){
    while(st < ed){
        if(s[st] != s[ed]){
            return false;
        }
        ++ st;
        -- ed;
    }
    return true;
}
// === 200ms(26.23%) && 5.2MB(100%) === //
int countSubstrings(char * s){
    int len = strlen(s);
    int ans = len;
    for(int i=0; i<len-1; ++i){
        for(int j=i+1; j<len; ++j){
            if(is_palindrome(s, i, j)){
                ++ ans;
            }
        }
    }
    return ans;
}
// === 0ms === // 网上最优的解法
int countSubstrings(char * s){
    int len=strlen(s);
    int res=0;
    for(int i=0;i<len;i++)
    {
        for(int j=0;(i-j)>=0&&(i+j)<len&&s[i+j]==s[i-j];j++)
            res++;
        for(int j=0;i-1-j>=0&&i+j<len&&s[i+j]==s[i-1-j];j++)
            res++;
    }
    return res;
}