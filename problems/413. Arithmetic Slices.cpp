/*
=== 413. Arithmetic Slices ===

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
For example, these are arithmetic sequence:
    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9
The following sequence is not arithmetic.
    1, 1, 2, 5, 7
A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
- A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

Example:
    A = [1, 2, 3, 4]
    return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
*/
// === 4ms(73.68%) && 7.1MB(100%) === //
int numberOfArithmeticSlices(int* A, int ASize){
    if(ASize < 3){
        return 0;
    }
    int diff[ASize-1];
    for(int i=0; i<ASize-1; ++i){
        diff[i] = A[i+1] - A[i];
    }
    int ans = 0, tmp = diff[0], count = 2;
    for(int i=1; i<ASize-1; ++i){
        if(diff[i] == tmp){
            ++ count;
        }
        else{
            if(count > 2){
                ans += (count-1)*(count-2)/2;
            }
            tmp = diff[i];
            count = 2;
        }
    }
    if(count > 2){
        ans += (count-1)*(count-2)/2;
    }
    return ans;
}

