/*
=== 859. Buddy Strings ===

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:
    Input: A = "ab", B = "ba"
    Output: true
Example 2:
    Input: A = "ab", B = "ab"
    Output: false
Example 3:
    Input: A = "aa", B = "aa"
    Output: true
Example 4:
    Input: A = "aaaaaaabc", B = "aaaaaaacb"
    Output: true
Example 5:
    Input: A = "", B = "aa"
    Output: false
 
Constraints:
    1. 0 <= A.length <= 20000
    2. 0 <= B.length <= 20000
    3. A and B consist only of lowercase letters.
*/
// === 0ms(100%) && 5.5MB(37.50%) === //
bool buddyStrings(char * A, char * B){
    if(strlen(A) != strlen(B)){
        return false;
    }
    int diff[2], size=0;
    int counter[26] = {0};
    for(int i=0; A[i]; ++i){
        if(A[i] != B[i]){
            if(size >= 2){
                return false;
            }
            diff[size] = i;
            ++ size;
        }
        ++ counter[A[i]-'a'];
    }
    if(size == 2){
        return A[diff[0]] == B[diff[1]] && A[diff[1]] == B[diff[0]];
    }
    else if(size == 0){
        for(int i=0; i<26; ++i){
            if(counter[i] >= 2){
                return true;
            }
        }
        return false;
    }
    return false;
}