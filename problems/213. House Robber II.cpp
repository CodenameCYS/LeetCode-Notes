/*
=== 213. House Robber II ===

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: [2,3,2]
    Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.

Example 2:
    Input: [1,2,3,1]
    Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
*/
// === 0ms === //
int rob(int* nums, int numsSize) {
    if(numsSize == 0){
        return 0;
    }
    else if(numsSize == 1){
        return nums[0];
    }
    else if(numsSize == 2){
        return nums[0] > nums[1] ? nums[0] : nums[1];
    }
    
    int s1[numsSize-1], s2[numsSize-1];
    s1[0] = nums[0], s2[0] = nums[1];
    s1[1] = nums[0] > nums[1] ? nums[0] : nums[1];
    s2[1] = nums[1] > nums[2] ? nums[1] : nums[2];
    for(int i=2; i<numsSize-1; ++i){
        s1[i] = s1[i-2] + nums[i] > s1[i-1] ? s1[i-2] + nums[i] : s1[i-1];
        s2[i] = s2[i-2] + nums[i+1] > s2[i-1] ? s2[i-2] + nums[i+1] : s2[i-1];
    }
    return s1[numsSize-2] > s2[numsSize-2] ? s1[numsSize-2] : s2[numsSize-2];
}