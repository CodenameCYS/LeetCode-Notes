/*
=== 941. Valid Mountain Array ===

Given an array A of integers, return true if and only if it is a valid mountain array.
Recall that A is a mountain array if and only if:
1. A.length >= 3
2. There exists some i with 0 < i < A.length - 1 such that:
    A[0] < A[1] < ... A[i-1] < A[i]
    A[i] > A[i+1] > ... > A[B.length - 1]
 
Example 1:
Input: [2,1]
Output: false

Example 2:
Input: [3,5,5]
Output: false

Example 3:
Input: [0,3,2,1]
Output: true

Note:
1. 0 <= A.length <= 10000
2. 0 <= A[i] <= 10000 
*/
bool validMountainArray(int* A, int ASize) {
    if(ASize <= 2){
        return false;
    }
    bool up = true;
    int h = A[0];
    for(int i=1; i<ASize; ++i){
        if(up){
            if(A[i] > h){
                h = A[i];
            }
            else if(A[i] == h){
                return false;
            }
            else{
                if(i == 1){
                    return false;
                }
                h = A[i];
                up = false;
            }
        }
        else{
            if(A[i] < h){
                h = A[i];
            }
            else{
                return false;
            }
        }
    }
    return (!up) && true;
}