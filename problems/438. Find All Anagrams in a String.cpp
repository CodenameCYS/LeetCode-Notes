/*
=== 438. Find All Anagrams in a String ===

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
    - Input:
    s: "cbaebabacd" p: "abc"
    - Output:
    [0, 6]
    - Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:
    - Input:
    s: "abab" p: "ab"
    - Output:
    [0, 1, 2]
    - Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool is_anagram(char* s, char* p){
    int alphabet[26] = {0};
    for(int i=0; p[i]; ++i){
        ++ alphabet[s[i] - 'a'];
        -- alphabet[p[i] - 'a'];
    }
    for(int i=0; i<26; ++i){
        if(alphabet[i] != 0){
            return false;
        }
    }
    return true;
}
// === 1660ms(7.27%) && 10.6MB(100%) === //
int* findAnagrams(char * s, char * p, int* returnSize){
    *returnSize = 0;
    int slen = strlen(s), plen = strlen(p);
    if(slen < plen){
        return NULL;
    }
    int* ans = (int*)malloc((slen-plen+1)*sizeof(int));
    for(int i=0; i<=slen-plen; ++i){
        if(is_anagram(&s[i], p)){
            ans[*returnSize] = i;
            ++ *returnSize;
        }
    }
    return ans;
}
// ==================================================================================================== //
bool is_anagram(int* alphabet){
    for(int i=0; i<26; ++i){
        if(alphabet[i] != 0){
            return false;
        }
    }
    return true;
}
// === 32ms(61.86%) && 10.5MB(100%) === //
int* findAnagrams(char * s, char * p, int* returnSize){
    *returnSize = 0;
    int slen = strlen(s), plen = strlen(p);
    if(slen < plen){
        return NULL;
    }
    
    int alphabet[26] = {0};
    for(int i=0; p[i]; ++i){
        ++ alphabet[p[i] - 'a'];
        -- alphabet[s[i] - 'a'];
    }
    
    int* ans = (int*)malloc((slen-plen+1)*sizeof(int));
    if(is_anagram(alphabet)){
        ans[*returnSize] = 0;
        ++ *returnSize;
    }
    for(int i=plen; i<slen; ++i){
        ++ alphabet[s[i-plen] - 'a'];
        -- alphabet[s[i] - 'a'];
        if(is_anagram(alphabet)){
            ans[*returnSize] = i-plen+1;
            ++ *returnSize;
        }
    }
    return ans;
}


