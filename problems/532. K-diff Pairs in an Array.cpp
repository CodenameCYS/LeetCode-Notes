/*
=== 532. K-diff Pairs in an Array ===

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
    Input: [3, 1, 4, 1, 5], k = 2
    Output: 2
    Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
    Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
    Input:[1, 2, 3, 4, 5], k = 1
    Output: 4
    Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
    Input: [1, 3, 1, 5, 4], k = 0
    Output: 1
    Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
    1. The pairs (i, j) and (j, i) count as the same pair.
    2. The length of the array won't exceed 10,000.
    3. All the integers in the given input belong to the range: [-1e7, 1e7].
*/
void quick_sort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed, tmp=nums[st];
    while(i<j){
        while(i<j && nums[j] >= tmp){
            -- j;
        }
        if(i<j){
            nums[i] = nums[j];
            ++ i;
        }
        while(i<j && nums[i] <= tmp){
            ++ i;
        }
        if(i<j){
            nums[j] = nums[i];
            -- j;
        }
    }
    nums[i] = tmp;
    quick_sort(nums, st, i-1);
    quick_sort(nums, i+1, ed);
}
// === 100ms(15.38%) && 7.8MB(100%) === //
int findPairs(int* nums, int numsSize, int k){
    quick_sort(nums, 0, numsSize-1);
    if(k < 0){
        return 0;
    }
    int i=0, j=0, tmp=INT_MIN;
    int ans = 0;
    while(j<numsSize){
        while(j<numsSize && (i>=j || nums[j] < nums[i] + k)){
            ++ j;
        }
        if(j<numsSize  && nums[i] != tmp && nums[i] + k == nums[j]){
            ++ ans;
            tmp = nums[i];
        }
        ++ i;
    }
    return ans;
}

