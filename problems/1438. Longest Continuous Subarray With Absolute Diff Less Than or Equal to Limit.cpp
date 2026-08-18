/*
=== 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit ===

Given an array of integers nums and an integer limit, return the size of the longest continuous subarray such that the absolute difference between any two elements is less than or equal to limit.
In case there is no subarray satisfying the given condition return 0.

Example 1:
    Input: nums = [8,2,4,7], limit = 4
    Output: 2 
    Explanation: All subarrays are: 
    [8] with maximum absolute diff |8-8| = 0 <= 4.
    [8,2] with maximum absolute diff |8-2| = 6 > 4. 
    [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
    [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
    [2] with maximum absolute diff |2-2| = 0 <= 4.
    [2,4] with maximum absolute diff |2-4| = 2 <= 4.
    [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
    [4] with maximum absolute diff |4-4| = 0 <= 4.
    [4,7] with maximum absolute diff |4-7| = 3 <= 4.
    [7] with maximum absolute diff |7-7| = 0 <= 4. 
    Therefore, the size of the longest subarray is 2.
Example 2:
    Input: nums = [10,1,2,4,7,2], limit = 5
    Output: 4 
    Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:
    Input: nums = [4,2,2,2,4,4,2,2], limit = 0
    Output: 3
 
Constraints:
    1. 1 <= nums.length <= 10^5
    2. 1 <= nums[i] <= 10^9
    3. 0 <= limit <= 10^9
*/
int min(int x, int y){
    return x < y ? x : y;
}
int max(int x, int y){
    return x > y ? x : y;
}
int cal_subarray_len(int* nums, int numsSize, int limit){
    int down = nums[0] - limit, up = nums[0] + limit;
    int ans = 1;
    for(int i=1; i<numsSize; ++i){
        if(nums[i] < down || nums[i] > up){
            break;
        }
        down = max(down, nums[i] - limit);
        up = min(up, nums[i] + limit);
        ++ ans;
    }
    return ans;
}
// === 36ms && 10.8MB === //
int longestSubarray(int* nums, int numsSize, int limit){
    if(numsSize <= 1){
        return numsSize;
    }
    int ans = 1;
    for(int i=0; i<numsSize-ans; ++i){
        int tmp = cal_subarray_len(&nums[i], numsSize-i, limit);
        ans = ans > tmp ? ans : tmp;
        // printf("%d : %d\n", i, ans);
    }
    return ans;
}