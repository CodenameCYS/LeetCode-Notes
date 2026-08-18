/*
=== 260. Single Number III ===

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:
    Input:  [1,2,1,3,2,5]
    Output: [3,5]

Note:
- The order of the result is not important. So in the above example, [5, 3] is also correct.
- Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
*/
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
void QuickSort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed, temp=nums[i];
    while(i<j){
        while(i<j && nums[j] >= temp){
            --j;
        }
        if(i<j){
            nums[i] = nums[j];
            ++i;
        }
        while(i<j && nums[i] <= temp){
            ++i;
        }
        if(i<j){
            nums[j] = nums[i];
            --j;
        }
    }
    nums[i] = temp;
    QuickSort(nums, st, i-1);
    QuickSort(nums, i+1, ed);
}
// === 8ms(41.43%) & 8MB(33.33%) === //
int* singleNumber(int* nums, int numsSize, int* returnSize) {
    if(numsSize == 0){
        *returnSize = 0;
        return NULL;
    }
    
    QuickSort(nums, 0, numsSize-1);
    int* ans = (int*)malloc(numsSize * sizeof(int));
    *returnSize = 0;
    for(int i=0; i<numsSize; ++i){
        if(*returnSize == 0 || nums[i] != ans[*returnSize-1]){
            ans[*returnSize] = nums[i];
            ++ *returnSize;
        }
        else{
            -- *returnSize;
        }
    }
    return ans;
}