/*
=== 896. Monotonic Array ===

An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
Return true if and only if the given array A is monotonic.

Example 1:
Input: [1,2,2,3]
Output: true

Example 2:
Input: [6,5,4,4]
Output: true

Example 3:
Input: [1,3,2]
Output: false

Example 4:
Input: [1,2,4,5]
Output: true

Example 5:
Input: [1,1,1]
Output: true
 
Note:
1. 1 <= A.length <= 50000
2. -100000 <= A[i] <= 100000
*/
bool isMonotonic(int* A, int ASize) {
    int temp = A[0];
    int state = 0; // 0 stands for unknown
    for(int i=1; i<ASize; ++i){
        if(state == 0){
            if(A[i] == temp){
                continue;
            }
            else if(A[i] > temp){
                temp = A[i];
                state = 1; // 1 stands for greater
            }
            else{
                temp = A[i];
                state = 2; // 2 stands for less
            }
        }
        else if(state == 1){
            if(A[i] >= temp){
                temp = A[i];
            }
            else{
                return false;
            }
        }
        else{
            if(A[i] <= temp){
                temp = A[i];
            }
            else{
                return false;
            }
        }
    }
    return true;
}