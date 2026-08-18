/*
=== 238. Product of Array Except Self ===

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
    Input:  [1,2,3,4]
    Output: [24,12,8,6]
    - Note: Please solve it without division and in O(n).

Follow up:
    - Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
// === 48ms(89.51%) && 15.1MB(74.29%) === //
int* productExceptSelf(int* nums, int numsSize, int* returnSize){
    long mul = 1;
    int zerosnum = 0;
    int zeroloc = -1;
    for(int i=0; i<numsSize; ++i){
        if(nums[i] == 0){
            ++ zerosnum;
            zeroloc = i;
        }
        else{
            mul *= nums[i];
        }
    }
    *returnSize = numsSize;
    int* ans = (int*)malloc(numsSize*sizeof(int));
    
    if(zerosnum >= 2){
        for(int i=0; i<numsSize; ++i){
            ans[i] = 0;
        }
        return ans;
    }
    else if(zerosnum == 1){
        for(int i=0; i<numsSize; ++i){
            ans[i] = 0;
        }
        ans[zeroloc] = mul;
        return ans;
    }
    else{
        for(int i=0; i<numsSize; ++i){
            ans[i] = mul/nums[i];
        }
        return ans;
    }
}
// === 48ms(89.51%) && 15.4MB(31.43%) === //
int* productExceptSelf(int* nums, int numsSize, int* returnSize){
    int* ans = (int*)malloc(numsSize*sizeof(int));
    *returnSize = numsSize;
    
    ans[0] = 1;
    for(int i=1; i<numsSize; ++i){
        ans[i] = ans[i-1] * nums[i-1];
    }
    int negprod = 1;
    for(int i=numsSize-1; i>=0; --i){
        ans[i] = ans[i]*negprod;
        negprod *= nums[i];
    }
    return ans;
}