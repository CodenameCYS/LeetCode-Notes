/*
=== 219. Contains Duplicate II ===

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true
Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true
Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false

*/
// === 1276ms(41.89%) === //
bool FindDuplicate(int* nums, int tgt, int loc, int k){
    if(loc < k){
        for(int i=0; i<loc; ++i){
            if(nums[i] == tgt){
                return true;
            }
        }
        nums[loc] = tgt;
    }
    else{
        for(int i=0; i<k; ++i){
            if(i == loc % k){
                nums[i] = tgt;
            }
            else{
                if(nums[i] == tgt){
                    return true;
                }
            }
        }
    }
    return false;
}
bool containsNearbyDuplicate(int* nums, int numsSize, int k) {
    int knums[k+1];
    for(int i=0; i<numsSize; ++i){
        bool state = FindDuplicate(knums, nums[i], i, k+1);
        if(state){
            return true;
        }
    }
    return false;
}