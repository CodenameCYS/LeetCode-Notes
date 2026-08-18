/*
=== 459. Repeated Substring Pattern ===

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
    Input: "abab"
    Output: True
    Explanation: It's the substring "ab" twice.
Example 2:
    Input: "aba"
    Output: False
Example 3:
    Input: "abcabcabcabc"
    Output: True
    Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
*/
// === 16ms(31.24%) && 7.8MB(100%) === //
bool repeatedSubstringPattern(char * s){
    int len = strlen(s);
    for(int i=1; i<=len/2; ++i){
        if(len % i != 0){
            continue;
        }
        bool find_substring = true;
        for(int j=0; j<len; ++j){
            if(s[j] != s[j%i]){
                find_substring = false;
                break;
            }
        }
        if(find_substring){
            return true;
        }
    }
    return false;
}

