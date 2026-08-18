/*
=== 796. Rotate String ===

We are given two strings, A and B.
A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
    Input: A = 'abcde', B = 'cdeab'
    Output: true
Example 2:
    Input: A = 'abcde', B = 'abced'
    Output: false

Note:
    1. A and B will have length at most 100.
*/
// === 0ms(100%) && 5.1MB(100%) === //
bool rotateString(char * A, char * B){
    int la = strlen(A), lb = strlen(B);
    if(la != lb){
        return false;
    }
    if(la == 0 && lb == 0){
        return true;
    }
    for(int i=0; i<lb; ++i){
        bool is_rotate=true;
        for(int j=0; j<la && is_rotate; ++j){
            if(A[j] != B[(i+j) % lb]){
                is_rotate = false;
            }
        }
        if(is_rotate){
            return true;
        }
    }
    return false;
}
