/*
=== 524. Longest Word in Dictionary through Deleting ===

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
    Input:
    s = "abpcplea", d = ["ale","apple","monkey","plea"]
    Output: 
    "apple"
Example 2:
    Input:
    s = "abpcplea", d = ["a","b","c"]
    Output: 
    "a"

Note:
    1. All the strings in the input will only contain lower-case letters.
    2. The size of the dictionary won't exceed 1,000.
    3. The length of all the strings in the input won't exceed 1,000.
*/
// === 36ms(18.75%) && 11.6MB(100%) === //
bool is_subseq(char* s1, char* s2){
    int i=0, j=0;
    for(;s1[i] && s2[j]; ++i){
        if(s1[i] == s2[j]){
            ++ j;
        }
    }
    return !s2[j];
}
bool is_larger(char* s1, char* s2){
    for(int i=0; s1[i]; ++i){
        if(s1[i] > s2[i]){
            return true;
        }
        else if(s1[i] < s2[i]){
            return false;
        }
        else{
            continue;
        }
    }
    return true;
}
char * findLongestWord(char * s, char ** d, int dSize){
    char* ans = (char*)malloc(1001*sizeof(char));
    int len = 0, slen=strlen(s);
    ans[len] = '\0';
    for(int i=0; i<dSize; ++i){
        int dlen = strlen(d[i]);
        if(dlen < len || dlen > slen){
            continue;
        }
        if(is_subseq(s, d[i])){
            if(len == dlen && is_larger(d[i], ans)){
                continue;
            }
            len = dlen;
            for(int j=0; j<dlen; ++j){
                ans[j] = d[i][j];
            }
            ans[len] = '\0';
        }
    }
    return ans;
}

