/*
=== 1415. The k-th Lexicographical String of All Happy Strings of Length n ===

A happy string is a string that:
    - consists only of letters of the set ['a', 'b', 'c'].
    - s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

Example 1:
    Input: n = 1, k = 3
    Output: "c"
    Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
Example 2:
    Input: n = 1, k = 4
    Output: ""
    Explanation: There are only 3 happy strings of length 1.
Example 3:
    Input: n = 3, k = 9
    Output: "cab"
    Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
Example 4:
    Input: n = 2, k = 7
    Output: ""
Example 5:
    Input: n = 10, k = 100
    Output: "abacbabacb"
 
Constraints:
    1. 1 <= n <= 10
    2. 1 <= k <= 100
*/
int fill_in_letter(char* s, int flag, int i, int k){
    int n = (k-1) / flag + 1;
    if(i == 0){
        s[i] = 'a' + n - 1;
    }
    else if(n == 1){
        if(s[i-1] == 'a'){
            s[i] = 'b';
        }
        else{
            s[i] = 'a';
        }
    }
    else{
        if(s[i-1] == 'c'){
            s[i] = 'b';
        }
        else{
            s[i] = 'c';
        }
    }
    // printf("s[%d] = %c, flag = %d, k = %d\n", i, s[i], flag, k);
    k = k % flag;
    return k == 0 ? flag : k;
}
// === 0ms(100%) && 5.1MB === //
char * getHappyString(int n, int k){
    int flag[n];
    flag[0] = 1;
    for(int i=1; i<n; ++i){
        flag[i] = 2 * flag[i-1];
    }
    if(k > 3*flag[n-1]){
        char* ans = malloc(sizeof(char));
        ans[0] = '\0';
        return ans;
    }
    char* ans = malloc((n+1) * sizeof(char));
    for(int i=0; i<n; ++i){
        k = fill_in_letter(ans, flag[n-1-i], i, k);
    }
    ans[n] = '\0';
    return ans;
}

