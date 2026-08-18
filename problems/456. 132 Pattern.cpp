/*
=== 456. 132 Pattern ===

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

- Note: n will be less than 15,000.

Example 1:
    Input: [1, 2, 3, 4]
    Output: False
    Explanation: There is no 132 pattern in the sequence.
Example 2:
    Input: [3, 1, 4, 2]
    Output: True
    Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
    Input: [-1, 3, 2, 0]
    Output: True
    Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
*/
// === 612ms(19.05%) && 8MB(100%) === //
bool find132pattern(int* nums, int numsSize){
    if(numsSize < 3){
        return false;
    }
    int min[numsSize];
    min[0] = nums[0];
    for(int i=1; i<numsSize; ++i){
        min[i] = min[i-1] < nums[i] ? min[i-1] : nums[i];
    }
    for(int i=1; i<numsSize-1; ++i){
        if(nums[i] == min[i]){
            continue;
        }
        for(int j=i+1; j<numsSize; ++j){
            if(nums[j] < nums[i] && nums[j] > min[i]){
                return true;
            }
        }
    }
    return false;
}
// ==================================================================================== //
// === 28ms(95.24%) && 7.9MB(100%) === // 网上大神的解法
bool find132pattern(int* nums, int numsSize){
    if(!numsSize){
        return false;
    }
    int less[numsSize];
    int stack[numsSize];
    int right = 0;
    int min = nums[0];
    for(int i = 1; i < numsSize; ++i){
        less[i] = min;
        min = min > nums[i] ? nums[i] : min;
    }
    for(int i = numsSize-1; i > 0; --i){
        while(right && stack[right-1]<nums[i]){
            if(stack[right-1] > less[i]){
                return true;
            }
            --right;
        }
        stack[right++] = nums[i];
    }
    return false;
}