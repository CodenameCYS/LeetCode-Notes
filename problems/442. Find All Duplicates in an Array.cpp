/*
=== 442. Find All Duplicates in an Array ===


Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

*/
# include <stdio.h>
# include <stdlib.h>

// === ver1.0 === //
// beat 17.99% //
void QuickSort(int* nums, int start, int end){
    if(start >= end){
        return;
    }
    
    int i = start, j = end;
    int temp = nums[start];
    while(i < j){
        while(i < j && nums[j] >= temp){
            --j;
        }
        if(i < j){
            nums[i] = nums[j];
            ++i;
        }
        while(i < j && nums[i] <= temp){
            ++i;
        }
        if(i < j){
            nums[j] = nums[i];
            --j;
        }
    }
    nums[i] = temp;
    QuickSort(nums, start, i-1);
    QuickSort(nums, i+1, end);
    return;
}

int* findDuplicates(int* nums, int numsSize, int* returnSize) {
    QuickSort(nums, 0, numsSize-1);
    
    int* ans = (int*)malloc((numsSize+1)/2*sizeof(int));
    *returnSize = 0;
    int i = 1;
    while(i < numsSize){
        if(nums[i] == nums[i-1]){
            ans[*returnSize] = nums[i];
            *returnSize += 1;
            i += 2;
        }        
        else{
            ++i;
        }
    }
    return ans;
}

// === ver2.0 === //
// beat 91.37% //
int* findDuplicates(int* nums, int numsSize, int* returnSize) {    
    int* ans = (int*)malloc((numsSize+1)/2*sizeof(int));
    *returnSize = 0;
    
    int i = 0;
    while(i < numsSize){
        if(nums[nums[i]-1] != nums[i]){
            int temp = nums[i];
            nums[i] = nums[temp - 1];
            nums[temp - 1] = temp;
        }
        else{
            ++i;
        }
    }
    
    i = 0;
    while(i < numsSize){
        if(nums[i] != i + 1){
            ans[*returnSize] = nums[i];
            *returnSize += 1;
        }
        ++i;
    }
    
    return ans;
}