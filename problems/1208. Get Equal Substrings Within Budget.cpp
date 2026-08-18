/*
=== 1208. Get Equal Substrings Within Budget ===

You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.
You are also given an integer maxCost.
Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.
If there is no substring from s that can be changed to its corresponding substring from t, return 0.

Example 1:
    Input: s = "abcd", t = "bcdf", cost = 3
    Output: 3
    - Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.
Example 2:
    Input: s = "abcd", t = "cdef", cost = 3
    Output: 1
    - Explanation: Each charactor in s costs 2 to change to charactor in t, so the maximum length is 1.
Example 3:
    Input: s = "abcd", t = "acde", cost = 0
    Output: 1
    - Explanation: You can't make any change, so the maximum length is 1.
 
Constraints:
    1. 1 <= s.length, t.length <= 10^5
    2. 0 <= maxCost <= 10^6
    3. s and t only contain lower case English letters.
*/
// === 4ms && 7.8MB === //
int equalSubstring(char * s, char * t, int maxCost){
    int n = strlen(s);
    int cumsum[n+1];
    cumsum[0] = 0;
    int st, ans;
    ans = 0, st = 0;
    for(int i=1; i<=n; ++i){
        cumsum[i] = cumsum[i-1] + abs(s[i-1]-t[i-1]);
        // printf("%d , ", cumsum[i]);
        if(cumsum[i] - cumsum[st] > maxCost){
            int tmp = i-1-st;
            ans = ans > tmp ? ans : tmp;
            while(cumsum[i] - cumsum[st] > maxCost){
                ++ st;
            }
        }
        else if(i == n){
            int tmp = i-st;
            ans = ans > tmp ? ans : tmp;
        }
    }
    return ans;
}

