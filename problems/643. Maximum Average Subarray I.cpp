/*
=== 643. Maximum Average Subarray I ===

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
    Input: [1,12,-5,-6,50,3], k = 4
    Output: 12.75
    Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 
Note:
    1. 1 <= k <= n <= 30,000.
    2. Elements of the given array will be in the range [-10,000, 10,000].
*/
// === 120ms(85%) && 10.2MB(100%) === //
double findMaxAverage(int* nums, int numsSize, int k){
    double max;
    int window = 0;
    for(int i=0; i<k; ++i){
        window += nums[i];
    }
    max = window;
    for(int i=k; i<numsSize; ++i){
        window = window + nums[i] - nums[i-k];
        max = max > window ? max : window;
    }
    return max / k;
}

