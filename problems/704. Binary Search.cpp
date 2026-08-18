/*
=== 704. Binary Search ===

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4
Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1
 
Note:
    1. You may assume that all elements in nums are unique.
    2. n will be in the range [1, 10000].
    3. The value of each element in nums will be in the range [-9999, 9999].
*/
// === 32ms(96.19%) && 6.6MB(100%) === //
int my_search(int* nums, int st, int ed, int target){
    if(st > ed){
        return -1;
    }
    int mid = (st + ed) / 2;
    if(nums[mid] == target){
        return mid;
    }
    else if(nums[mid] < target){
        return my_search(nums, mid+1, ed, target);
    }
    else{
        return my_search(nums, st, mid-1, target);
    }
}
int search(int* nums, int numsSize, int target){
    return my_search(nums, 0, numsSize-1, target);
}

