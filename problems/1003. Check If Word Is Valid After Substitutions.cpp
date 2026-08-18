/*
=== 1003. Check If Word Is Valid After Substitutions ===

We are given that the string "abc" is valid.
From any valid string V, we may split V into two pieces X and Y such that X + Y (X concatenated with Y) is equal to V.  (X or Y may be empty.)  Then, X + "abc" + Y is also valid.
If for example S = "abc", then examples of valid strings are: "abc", "aabcbc", "abcabc", "abcabcababcc".  Examples of invalid strings are: "abccba", "ab", "cababc", "bac".
Return true if and only if the given string S is valid.

Example 1:
    Input: "aabcbc"
    Output: true
- Explanation: 
    We start with the valid string "abc".
    Then we can insert another "abc" between "a" and "bc", resulting in "a" + "abc" + "bc" which is "aabcbc".
Example 2:
    Input: "abcabcababcc"
    Output: true
- Explanation: 
    "abcabcabc" is valid after consecutive insertings of "abc".
    Then we can insert "abc" before the last letter, resulting in "abcabcab" + "abc" + "c" which is "abcabcababcc".
Example 3:
    Input: "abccba"
    Output: false
Example 4:
    Input: "cababc"
    Output: false
 
Note:
    1. 1 <= S.length <= 20000
    2. S[i] is 'a', 'b', or 'c'
*/
// === 8ms & 7.8MB === //
bool isValid(char* S) {
    int len = strlen(S);
    if(len % 3 != 0){
        return false;
    }
    
    bool isused[len];
    for(int i=0; i<len; ++i){
        isused[i] = false;
    }
    int left = len;
    bool isfinished = false;
    while(!isfinished){
        // printf("start!\n");
        int state = 0;
        isfinished = true;
        int record[3];
        for(int i=0; i<len; ++i){
            if(isused[i]){
                continue;
            }
            else if(S[i] == 'a'){
                record[0] = i;
                state = 1;
            }
            else if(state == 1 && S[i] == 'b'){
                record[1] = i;
                state = 2;
            }
            else if(state == 2 && S[i] == 'c'){
                record[2] = i;
                state = 0;
                isfinished = false;
                left -= 3;
                for(int j=0; j<3; ++j){
                    isused[record[j]] = true;
                    // printf("%d:%c\t", record[j],S[record[j]]);
                }
                // printf("\n");
            }
            else{
                state = 0;
            }
        }
    }
    return left == 0;
}

// === 12ms & 7.8MB === //
bool isValid(char* S) {
    int len = strlen(S);
    if(len % 3 != 0){
        return false;
    }
    
    bool isused[len];
    for(int i=0; i<len; ++i){
        isused[i] = false;
    }
    int left = len;
    bool isfinished = false;
    while(!isfinished){
        int state = 0;
        isfinished = true;
        int record[3];
        for(int i=0; i<len; ++i){
            if(isused[i]){
                continue;
            }
            if(state == 0){
                if(S[i] == 'a'){
                    record[state] = i;
                    state = 1;
                }
            }
            else if(state == 1){
                if(S[i] == 'b'){
                    record[state] = i;
                    state = 2;
                }
                else if(S[i] == 'a'){
                    record[0] = i;
                    state = 1;
                }
                else{
                    state = 0;
                }
            }
            else{
                if(S[i] == 'c'){
                    record[state] = i;
                    state = 0;
                    isfinished = false;
                    left -= 3;
                    for(int j=0; j<3; ++j){
                        isused[record[j]] = true;
                        // printf("%d:%c\t", record[j],S[record[j]]);
                    }
                    // printf("\n");
                }
                else if(S[i] == 'a'){
                    record[0] = i;
                    state = 1;
                }
                else{
                    state = 0;
                }
            }
        }
    }
    return left == 0;
}