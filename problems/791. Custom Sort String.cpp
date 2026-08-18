/*
=== 791. Custom Sort String ===

S and T are strings composed of lowercase letters. In S, no letter occurs more than once.
S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.
Return any permutation of T (as a string) that satisfies this property.

Example :
    Input: 
    S = "cba"
    T = "abcd"
    Output: "cbad"
    Explanation: 
    "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
    Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
 
Note:
    1. S has length at most 26, and no character is repeated in S.
    2. T has length at most 200.
    3. S and T consist of lowercase letters only.
*/
// === 0ms(100%) && 5.3MB(100%) === //
char * customSortString(char * S, char * T){
    int len = strlen(T);
    char* ans = (char*)malloc((len+1) * sizeof(char));
    int alphabet[26] = {0};
    for(int i=0; i<len; ++i){
        ++ alphabet[T[i]-'a'];
    }
    int size = 0;
    for(int i=0; S[i]; ++i){
        for(;alphabet[S[i]-'a'] > 0; --alphabet[S[i]-'a']){
            ans[size] = S[i];
            ++ size;
        }
    }
    for(int i=0; i<26; ++i){
        for(;alphabet[i] > 0; --alphabet[i]){
            ans[size] = 'a' + i;
            ++ size;
        }
    }
    ans[size] = '\0';
    return ans;
}

