/*
=== 205. Isomorphic Strings ===

Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:
    Input: s = "egg", t = "add"
    Output: true

Example 2:
    Input: s = "foo", t = "bar"
    Output: false

Example 3:
    Input: s = "paper", t = "title"
    Output: true

Note:
    - You may assume both s and t have the same length.
*/
bool isIsomorphic(char* s, char* t) {
    int pstate[127], nstate[127];
    for(int i=0; i<127; ++i){
        pstate[i] = 127;
        nstate[i] = 127;
    }
    int i = 0;
    while(s[i] != '\0'){
        if(pstate[s[i]] == 127 && nstate[t[i]] == 127){
            pstate[s[i]] = s[i] - t[i];
            nstate[t[i]] = t[i] - s[i];
        }
        else if(pstate[s[i]] == 127 || nstate[t[i]] == 127 || pstate[s[i]] != s[i] - t[i] || nstate[t[i]] != t[i] - s[i]){
            return false;
        }
        ++i;
    }
    return true;
}