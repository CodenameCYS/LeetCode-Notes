/*
=== 387. First Unique Character in a String ===

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
    s = "leetcode"
    return 0.
    
    s = "loveleetcode",
    return 2.

- Note: You may assume the string contain only lowercase letters.
*/
// === 4ms(99.09%) && 8.3MB(66.67%) === //
int firstUniqChar(char * s){
    int alphabet[26];
    for(int i=0; i<26; ++i){
        alphabet[i] = 0;
    }
    for(int i=0; s[i]; ++i){
        ++ alphabet[s[i] - 'a'];
    }
    for(int i=0; s[i]; ++i){
        if(alphabet[s[i] - 'a'] == 1){
            return i;
        }
    }
    return -1;
}

