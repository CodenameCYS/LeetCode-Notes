/*
=== 300. Longest Increasing Subsequence ===

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
    Input: [10,9,2,5,3,7,101,18]
    Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:
    1. There may be more than one LIS combination, it is only necessary for you to return the length.
    2. Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
*/
// === 28ms(36.75%) & 6.9MB(69.23%) === //
int lengthOfLIS(int* nums, int numsSize) {
    if(numsSize == 0){
        return 0;
    }
    
    int dp[numsSize];
    int ans = 1;
    for(int i=0; i<numsSize; ++i){
        dp[i] = 1;
        for(int j=0; j<i; ++j){
            if(nums[j] < nums[i]){
                dp[i] = dp[i] > dp[j]+1 ? dp[i] : dp[j]+1;
            }
        }
        ans = ans > dp[i] ? ans : dp[i];
    }
    return ans;
}