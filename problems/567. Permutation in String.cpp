/*
=== 567. Permutation in String ===

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:
    Input: s1 = "ab" s2 = "eidbaooo"
    Output: True
    Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
    Input:s1= "ab" s2 = "eidboaoo"
    Output: False
 
Note:
    1. The input strings only contain lower case letters.
    2. The length of both given strings is in range [1, 10,000].
*/
bool is_equal(int* alphabet, int* window){
    for(int i=0; i<26; ++i){
        if(alphabet[i] != window[i]){
            return false;
        }
    }
    return true;
}
// === 4ms(85.42%) && 7.2MB(50%) === //
bool checkInclusion(char * s1, char * s2){
    int l1 = strlen(s1), l2 = strlen(s2);
    if(l1 > l2){
        return false;
    }
    if(l1 == 0){
        return true;
    }
    int alphabet[26] = {0}, window[26] = {0};
    for(int i=0; i<l1; ++i){
        ++ alphabet[s1[i]-'a'];
        ++ window[s2[i]-'a'];
    }
    if(is_equal(alphabet, window)){
        return true;
    }
    for(int i=l1; i<l2; ++i){
        -- window[s2[i-l1]-'a'];
        ++ window[s2[i]-'a'];
        if(is_equal(alphabet, window)){
            return true;
        }
    }
    return false;
}

