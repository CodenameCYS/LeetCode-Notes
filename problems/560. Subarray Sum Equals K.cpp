/*
=== 560. Subarray Sum Equals K ===

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
    Input:nums = [1,1,1], k = 2
    Output: 2

Note:
    1. The length of the array is in range [1, 20,000].
    2. The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
*/
// === 876ms(11.76%) && 8.2MB(100%) === //
int subarraySum(int* nums, int numsSize, int k){
    int cumsum[numsSize+1];
    cumsum[0] = 0;
    int ans = 0;
    for(int i=0; i<numsSize; ++i){
        cumsum[i+1] = cumsum[i] + nums[i];
        if(cumsum[i+1] == k){
            ++ ans;
        }
    }
    // printf("%d\n", ans);
    for(int l=1; l<numsSize; ++l){
        for(int i=1; i+l<=numsSize; ++i){
            if(cumsum[i+l] - cumsum[i] == k){
                ++ ans;
            }
        }
    }
    // printf("%d\n", ans);
    return ans;
}

