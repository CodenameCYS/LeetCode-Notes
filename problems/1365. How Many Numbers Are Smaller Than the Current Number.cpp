/*
=== 1365. How Many Numbers Are Smaller Than the Current Number ===

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.

Example 1:
    Input: nums = [8,1,2,2,3]
    Output: [4,0,1,1,3]
    Explanation: 
    For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
    For nums[1]=1 does not exist any smaller number than it.
    For nums[2]=2 there exist one smaller number than it (1). 
    For nums[3]=2 there exist one smaller number than it (1). 
    For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:
    Input: nums = [6,5,4,8]
    Output: [2,1,0,3]
Example 3:
    Input: nums = [7,7,7,7]
    Output: [0,0,0,0]
 
Constraints:
    1. 2 <= nums.length <= 500
    2. 0 <= nums[i] <= 100
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void quick_sort(int* nums, int* idx, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed, k=idx[st], tmp=nums[st];
    while(i<j){
        while(i<j && nums[j] >= tmp){
            -- j;
        }
        if(i<j){
            nums[i] = nums[j];
            idx[i] = idx[j];
            ++ i;
        }
        while(i<j && nums[i] <= tmp){
            ++ i;
        }
        if(i<j){
            nums[j] = nums[i];
            idx[j] = idx[i];
            -- j;
        }
    }
    nums[i] = tmp, idx[i] = k;
    quick_sort(nums, idx, st, i-1);
    quick_sort(nums, idx, i+1, ed);
}
// === 8ms && 6.6MB === //
int* smallerNumbersThanCurrent(int* nums, int numsSize, int* returnSize){
    int* ans = (int*)malloc(numsSize*sizeof(int));
    *returnSize = numsSize;
    if(numsSize == 0){
        return ans;
    }
    
    int idx[numsSize];
    for(int i=0; i<numsSize; ++i){
        idx[i] = i;
    }
    quick_sort(nums, idx, 0, numsSize-1);
        
    for(int i=0; i<numsSize;){
        int count = i;
        ans[idx[i]] = count;
        ++ i;
        while(i<numsSize && nums[i] == nums[count]){
            ans[idx[i]] = count;
            ++ i;
        }
    }
    return ans;
}

