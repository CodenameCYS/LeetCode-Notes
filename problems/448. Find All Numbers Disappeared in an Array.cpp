/*
=== 448. Find All Numbers Disappeared in an Array ===

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]

*/

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
# include <stdio.h>
# include <stdlib.h>

//=== ver1.0 beat 96.0% ===//
int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc(numsSize*sizeof(int));
    *returnSize = 0;
    
    int i = 0;
    while(i < numsSize){
        /*
        printf("%d\t%d:\t", i, nums[i]);
        for(int j=0; j<numsSize; ++j){
            printf("%d\t", nums[j]);
        }
        printf("\n");
        */
        if(nums[i] > 0 && nums[i] <= numsSize && nums[nums[i]-1] != nums[i]){
            int temp = nums[i];
            nums[i] = nums[temp -1];
            nums[temp - 1] = temp;
        }
        else{
            ++i;
        }
    }
    
    for(int i=0; i<numsSize; ++i){
        if(nums[i] != i+1){
            ans[*returnSize] = i+1;
            *returnSize += 1;
        }
    }
    
    return ans;
}

// === ver2.0 === //
