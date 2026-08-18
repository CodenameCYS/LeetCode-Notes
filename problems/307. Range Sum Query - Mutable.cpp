/*
=== 307. Range Sum Query - Mutable ===

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
The update(i, val) function modifies nums by updating the element at index i to val.

Example:
    Given nums = [1, 3, 5]
    sumRange(0, 2) -> 9
    update(1, 2)
    sumRange(0, 2) -> 8

Note:
    1. The array is only modifiable by the update function.
    2. You may assume the number of calls to update and sumRange function is distributed evenly.
*/
// === 168ms(15%) & 13.8MB(100%) === //
typedef struct {
    int* nums;
    int numsSize;
} NumArray;

NumArray* numArrayCreate(int* nums, int numsSize) {
    NumArray* obj = (NumArray*)malloc(sizeof(NumArray));
    obj->numsSize = numsSize;
    if(numsSize==0){
        obj->nums = NULL;
    }
    else{
        obj->nums = (int*)malloc(numsSize*sizeof(int));
        for(int i=0; i<numsSize; ++i){
            (obj->nums)[i] = nums[i];
        }
    }
    return obj;
}

void numArrayUpdate(NumArray* obj, int i, int val) {
    (obj->nums)[i] = val;
}

int numArraySumRange(NumArray* obj, int i, int j) {
    int ans = 0;
    while(i<=j){
        ans += (obj->nums)[i];
        ++i;
    }
    return ans;
}

void numArrayFree(NumArray* obj) {
    free(obj->nums);
    free(obj);
}

/**
 * Your NumArray struct will be instantiated and called as such:
 * struct NumArray* obj = numArrayCreate(nums, numsSize);
 * numArrayUpdate(obj, i, val);
 * int param_2 = numArraySumRange(obj, i, j);
 * numArrayFree(obj);
 */