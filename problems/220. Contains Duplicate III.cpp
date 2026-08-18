/*
=== 220. Contains Duplicate III ===

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:
    Input: nums = [1,2,3,1], k = 3, t = 0
    Output: true
Example 2:
    Input: nums = [1,0,1,1], k = 1, t = 2
    Output: true
Example 3:
    Input: nums = [1,5,9,1,5,9], k = 2, t = 3
    Output: false
*/
// === 216ms(63.64%) === //
bool FindAlmostDuplicate(int* nums, long tgt, int loc, long k, long t){
    if(loc < k){
        for(int i=0; i<loc; ++i){
            long diff = nums[i]-tgt;
            if(fabs(diff) <= t){
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
                long diff = nums[i]-tgt;
                if(fabs(diff) <= t){
                    return true;
                }
            }
        }
    }
    return false;
}
bool containsNearbyAlmostDuplicate(int* nums, int numsSize, int k, int t) {
    int knums[k+1];
    for(int i=0; i<numsSize; ++i){
        bool state = FindAlmostDuplicate(knums, nums[i], i, k+1, t);
        if(state){
            return true;
        }
    }
    return false;
}