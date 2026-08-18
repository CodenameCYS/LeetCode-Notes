/*
=== 1417. Reformat The String ===

Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.
Return the reformatted string or return an empty string if it is impossible to reformat the string.

Example 1:
    Input: s = "a0b1c2"
    Output: "0a1b2c"
    Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Example 2:
    Input: s = "leetcode"
    Output: ""
    Explanation: "leetcode" has only characters so we cannot separate them by digits.
Example 3:
    Input: s = "1229857369"
    Output: ""
    Explanation: "1229857369" has only digits so we cannot separate them by characters.
Example 4:
    Input: s = "covid2019"
    Output: "c2o0v1i9d"
Example 5:
    Input: s = "ab123"
    Output: "1a2b3"
 
Constraints:
    1. 1 <= s.length <= 500
    2. s consists of only lowercase English letters and/or digits.
*/
// === 4ms && 5.9MB === //
char * reformat(char * s){
    int n = strlen(s);
    char chars[n], digit[n];
    int csize=0, dsize=0;
    for(int i=0; s[i]; ++i){
        if(s[i]>='0' && s[i]<='9'){
            digit[dsize] = s[i];
            ++ dsize;
        }
        else{
            chars[csize] = s[i];
            ++ csize;
        }
    }
    if(abs(csize-dsize) > 1){
        char* ans = malloc(sizeof(char));
        ans[0] = '\0';
        return ans;
    }
    else if(csize >= dsize){
        char* ans = malloc((n+1)*sizeof(char));
        ans[n] = '\0';
        for(int i=0; i<dsize; ++i){
            ans[2*i] = chars[i];
            ans[2*i+1] = digit[i];
        }
        if(csize > dsize){
            ans[n-1] = chars[csize-1];
        }
        return ans;
    }
    else{
        char* ans = malloc((n+1)*sizeof(char));
        ans[n] = '\0';
        for(int i=0; i<csize; ++i){
            ans[2*i] = digit[i];
            ans[2*i+1] = chars[i];
        }
        ans[n-1] = digit[dsize-1];
        return ans;
    }
}