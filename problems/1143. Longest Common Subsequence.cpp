/*
=== 1143. Longest Common Subsequence ===

Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.
If there is no common subsequence, return 0.

Example 1:
    Input: text1 = "abcde", text2 = "ace" 
    Output: 3  
    Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:
    Input: text1 = "abc", text2 = "abc"
    Output: 3
    Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:
    Input: text1 = "abc", text2 = "def"
    Output: 0
    Explanation: There is no such common subsequence, so the result is 0.
 
Constraints:
    1. 1 <= text1.length <= 1000
    2. 1 <= text2.length <= 1000
    3. The input strings consist of lowercase English characters only.
*/
int max(x, y){
    return x > y ? x : y;
}
// === 8ms(97.22%) && 9.6MB(47.89%) === //
int longestCommonSubsequence(char * text1, char * text2){
    int l1 = strlen(text1);
    int l2 = strlen(text2);
    int dp[l1+1][l2+1];
    for(int i=0; i<=l1; ++i){
        dp[i][l2] = 0;
    }
    for(int i=0; i<l2; ++i){
        dp[l1][i] = 0;
    }
    for(int i=l1-1; i>=0; --i){
        for(int j=l2-1; j>=0; --j){
            if(text1[i] == text2[j]){
                dp[i][j] = 1 + dp[i+1][j+1];
            }
            else{
                dp[i][j] = max(dp[i][j+1], dp[i+1][j]);
            }
        }
    }
    return dp[0][0];
}