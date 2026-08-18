/*
=== 303. Range Sum Query - Immutable ===

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
    Given nums = [-2, 0, 3, -5, 2, -1]
    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3

Note:
    1. You may assume that the array does not change.
    2. There are many calls to sumRange function.
*/

// === 40ms(43.90%) & 12.2MB(57.14%) === //
typedef struct {
    int numsSize;
    int* nums;
} NumArray;

NumArray* numArrayCreate(int* nums, int numsSize) {
    NumArray* ans = (NumArray*)malloc(sizeof(NumArray));
    ans -> numsSize = numsSize;
    if(numsSize == 0){
        ans->nums = NULL;
    }
    else{
        ans -> nums = (int*)malloc(numsSize*sizeof(int));
        (ans -> nums)[0] = nums[0];
        for(int i=1; i<numsSize; ++i){
            (ans -> nums)[i] = (ans -> nums)[i-1] + nums[i];
        }
    }
    return ans;
}

int numArraySumRange(NumArray* obj, int i, int j) {
    if(i == 0){
        return (obj->nums)[j];
    }
    else{
        return (obj->nums)[j] - (obj->nums)[i-1];
    }
}

void numArrayFree(NumArray* obj) {
    free(obj->nums);
    free(obj);
}

/**
 * Your NumArray struct will be instantiated and called as such:
 * struct NumArray* obj = numArrayCreate(nums, numsSize);
 * int param_1 = numArraySumRange(obj, i, j);
 * numArrayFree(obj);
 */