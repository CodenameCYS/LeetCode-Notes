/*
=== 852. Peak Index in a Mountain Array ===

Let's call an array A a mountain if the following properties hold:
    - A.length >= 3
    - There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:
    Input: [0,1,0]
    Output: 1
Example 2:
    Input: [0,2,1,0]
    Output: 1

Note:
    1. 3 <= A.length <= 10000
    2. 0 <= A[i] <= 10^6
    3. A is a mountain, as defined above.
*/
// === 12ms(22.73%) && 6MB(72.06%) === //
int peakIndexInMountainArray(int* A, int ASize){
    int st = 0, ed = ASize-1;
    while(st < ed-1){
        int mid = (st+ed) / 2;
        if(A[mid-1] < A[mid] && A[mid] > A[mid+1]){
            return mid;
        }
        else if(A[mid] < A[mid+1]){
            st = mid;
        }
        else{
            ed = mid;
        }
    }
    return 0;
}