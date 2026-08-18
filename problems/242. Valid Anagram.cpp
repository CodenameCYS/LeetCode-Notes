/*
=== 242. Valid Anagram ===

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true
Example 2:
    Input: s = "rat", t = "car"
    Output: false

Note:
    - You may assume the string contains only lowercase alphabets.

Follow up:
    - What if the inputs contain unicode characters? How would you adapt your solution to such case?
*/
// === 4ms(94.01%) && 7.4MB(6.25%) === //
bool isAnagram(char * s, char * t){
    if(strlen(s) != strlen(t)){
        return false;
    }
    int alphabet[26];
    for(int i=0; i<26; ++i){
        alphabet[i] = 0;
    }
    
    int len = strlen(s);
    for(int i=0; i<len; ++i){
        ++ alphabet[s[i]-'a'];
        -- alphabet[t[i]-'a'];
    }
    
    for(int i=0; i<26; ++i){
        if(alphabet[i] != 0){
            return false;
        }
    }
    return true;
}

