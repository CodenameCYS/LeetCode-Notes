/*
=== 494. Target Sum ===

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
    Input: nums is [1, 1, 1, 1, 1], S is 3. 
    Output: 5
    Explanation: 
    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3
    There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:
    1. The length of the given array is positive and will not exceed 20.
    2. The sum of elements in the given array will not exceed 1000.
    3. Your output answer is guaranteed to be fitted in a 32-bit integer.
*/
// === 456ms(40%) && 7MB(100%) === //
int solution(int* nums, int numsSize, int target, int tmp){
    if(numsSize == 0){
        return 0;
    }
    else if(numsSize == 1){
        int ans = 0;
        ans += tmp + nums[0] == target;
        ans += tmp - nums[0] == target;
        return ans;
    }
    else{
        return solution(&nums[1], numsSize-1, target, tmp + nums[0]) 
            + solution(&nums[1], numsSize-1, target, tmp-nums[0]);
    }
}
int findTargetSumWays(int* nums, int numsSize, int S){
    return solution(nums, numsSize, S, 0);
}

