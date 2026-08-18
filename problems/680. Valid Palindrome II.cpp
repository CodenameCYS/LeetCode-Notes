/*
=== 680. Valid Palindrome II ===

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
    Input: "aba"
    Output: True
Example 2:
    Input: "abca"
    Output: True
    Explanation: You could delete the character 'c'.

Note:
    - The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
*/
bool is_palidrome(char* s, int st, int ed){
    while(st < ed){
        if(s[st] == s[ed]){
            ++ st, --ed;
        }
        else{
            return false;
        }
    }
    return true;
}
// === 16ms(75.96%) && 8.7MB(100%) === //
bool validPalindrome(char * s){
    int l = strlen(s);
    for(int i=0, j=l-1;i<j; ++i, --j){
        if(s[i] == s[j]){
            continue;
        }
        else{
            return is_palidrome(s, i+1, j) || is_palidrome(s, i, j-1);
        }
    }
    return true;
}

