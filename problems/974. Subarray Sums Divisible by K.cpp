/*
=== 974. Subarray Sums Divisible by K ===

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

Example 1:
    Input: A = [4,5,0,-2,-3,1], K = 5
    Output: 7
Explanation: 
    There are 7 subarrays with a sum divisible by K = 5:
    [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 
Note:
    1. 1 <= A.length <= 30000
    2. -10000 <= A[i] <= 10000
    3. 2 <= K <= 10000
*/
// === 20 ms === //
int subarraysDivByK(int* A, int ASize, int K) {
    int cumsum[ASize];
    int count[K];
    for(int i=0; i<K ; ++i){
        count[i] = 0;
    }
    count[0] = 1;
    
    cumsum[0] = ((A[0] % K) + K) % K;
    ++ count[cumsum[0]];
    for(int i=1; i<ASize; ++i){
        cumsum[i] = ((cumsum[i-1] + A[i]) % K + K) % K;
        ++ count[cumsum[i]];
    }
    int ans = 0;
    for(int i=0; i<K; ++i){
        ans += count[i] * (count[i]-1) / 2;
    }
    return ans;
}