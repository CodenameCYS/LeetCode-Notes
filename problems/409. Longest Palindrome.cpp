/*
=== 409. Longest Palindrome ===

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
- Assume the length of given string will not exceed 1,010.

Example:
    Input:
    "abccccdd"
    Output:
    7
    Explanation:
    One longest palindrome that can be built is "dccaccd", whose length is 7.
*/
// === 0ms(100%) && 7.1MB(100%) === //
int longestPalindrome(char * s){
    int alphabet[52] = {0};
    for(int i=0; s[i]; ++i){
        if(s[i] >= 'a' && s[i] <= 'z'){
            ++ alphabet[s[i]-'a'];
        }
        else{
            ++ alphabet[s[i]-'A'+26];
        }
    }
    int ans = 0;
    bool has_odd = false;
    for(int i=0; i<52; ++i){
        if(alphabet[i] % 2 == 0){
            ans += alphabet[i];
        }
        else{
            ans += alphabet[i]-1;
            has_odd = true;
        }
    }
    return has_odd ? ans+1 : ans;
}

