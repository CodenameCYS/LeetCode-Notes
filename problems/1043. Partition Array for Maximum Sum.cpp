/*
=== 1043. Partition Array for Maximum Sum ===

Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.  After partitioning, each subarray has their values changed to become the maximum value of that subarray.
Return the largest sum of the given array after partitioning.

Example 1:
    Input: A = [1,15,7,9,2,5,10], K = 3
    Output: 84
    - Explanation: A becomes [15,15,15,9,10,10,10]
 
Note:
    1. 1 <= K <= A.length <= 500
    2. 0 <= A[i] <= 10^6
*/
// === 12ms && 7.3MB === //
int maxSumAfterPartitioning(int* A, int ASize, int K){
    int dp[ASize+1];
    dp[0] = 0;
    for(int i=1; i<=ASize; ++i){
        dp[i] = 0;
        int temp;
        int size = 0;
        int max = 0;
        for(int j=1; j<=K; ++j){
            if(i-j < 0){
                break;
            }
            max = max > A[i-j] ? max : A[i-j];
            temp = max*j + dp[i-j];
            dp[i] = dp[i] > temp ? dp[i] : temp;
            ++size;
        }
    }
    return dp[ASize];
}