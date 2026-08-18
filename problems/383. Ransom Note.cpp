/*
=== 383. Ransom Note ===

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.

Note:
- You may assume that both strings contain only lowercase letters.

Example:
    1. canConstruct("a", "b") -> false
    2. canConstruct("aa", "ab") -> false
    3. canConstruct("aa", "aab") -> true
*/
// === 8ms(54.69%) && 7.9MB(100%) === //
bool canConstruct(char * ransomNote, char * magazine){
    int alphabet[26];
    for(int i=0; i<26; ++i){
        alphabet[i] = 0;
    }
    int len = strlen(magazine);
    for(int i=0; i<len; ++i){
        ++ alphabet[magazine[i] - 'a'];
    }
    len = strlen(ransomNote);
    for(int i=0; i<len; ++i){
        -- alphabet[ransomNote[i] - 'a'];
        if(alphabet[ransomNote[i] - 'a'] < 0){
            return false;
        }
    }
    return true;
}

