/*
=== 1007. Minimum Domino Rotations For Equal Row ===

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
We may rotate the i-th domino, so that A[i] and B[i] swap values.
Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.
If it cannot be done, return -1.

Example 1:
    Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
    Output: 2
- Explanation: 
    The first figure represents the dominoes as given by A and B: before we do any rotations.
    If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:
    Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
    Output: -1
- Explanation: 
    In this case, it is not possible to rotate the dominoes to make one row of values equal.
 
Note:
    1. 1 <= A[i], B[i] <= 6
    2. 2 <= A.length == B.length <= 20000
*/
// === 32ms & 10.2MB === //
int minDominoRotations(int* A, int ASize, int* B, int BSize) {
    int ans = -1;
    
    int tgt1=A[0], tgt2=B[0];
    bool aispossible = true, bispossible = true;
    int acount = 0, bcount = 0;
    for(int i=0; i<ASize; ++i){
        if(A[i] == tgt1){
            continue;
        }
        else if(B[i] == tgt1){
            ++acount;
        }
        else{
            aispossible = false;
            // printf("a is not possible, tgt = %d : a = %d , b = %d\n", tgt1, A[i], B[i]);
            break;
        }
    }
    for(int i=0; i<ASize; ++i){
        if(A[i] == tgt2){
            continue;
        }
        else if(B[i] == tgt2){
            ++bcount;
        }
        else{
            bispossible = false;
            // printf("b is not possible, tgt = %d : a = %d , b = %d\n", tgt2, A[i], B[i]);
            break;
        }
    }
    if(aispossible && bispossible){
        ans = acount < bcount ? acount : bcount;
    }
    else if(aispossible){
        ans = acount;
    }
    else if(bispossible){
        ans = bcount;
    }
    // printf("A = %d or %d -> ans = %d\n", acount, bcount, ans);
    
    acount = 0, bcount = 0;
    aispossible = true, bispossible = true;
    for(int i=0; i<BSize; ++i){
        if(B[i] == tgt1){
            continue;
        }
        else if(A[i] == tgt1){
            ++acount;
        }
        else{
            aispossible = false;
            // printf("a is not possible, tgt = %d : a = %d , b = %d\n", tgt1, A[i], B[i]);
            break;
        }
    }
    for(int i=0; i<BSize; ++i){
        if(B[i] == tgt2){
            continue;
        }
        else if(A[i] == tgt2){
            ++bcount;
        }
        else{
            bispossible = false;
            // printf("b is not possible, tgt = %d : a = %d , b = %d\n", tgt2, A[i], B[i]);
            break;
        }
    }
    if(aispossible && bispossible){
        int tempans = acount < bcount ? acount : bcount;
        ans = ans == -1? tempans : (tempans < ans ? tempans : ans);
    }
    else if(aispossible){
        int tempans = acount;
        ans = ans == -1? tempans : (tempans < ans ? tempans : ans);
    }
    else if(bispossible){
        int tempans = bcount;
        ans = ans == -1? tempans : (tempans < ans ? tempans : ans);
    }
    // printf("B = %d or %d -> ans = %d\n", acount, bcount, ans);
    return ans;
}