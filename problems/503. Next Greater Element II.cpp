/*
=== 503. Next Greater Element II ===

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
    Input: [1,2,1]
    Output: [2,-1,2]
    Explanation: The first 1's next greater number is 2; 
    The number 2 can't find next greater number; 
    The second 1's next greater number needs to search circularly, which is also 2.

Note: The length of given array won't exceed 10000.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
// === 84ms(77.27%) && 17.7MB(100%) === //
int* nextGreaterElements(int* nums, int numsSize, int* returnSize){
    int* ans = (int*)malloc(numsSize*sizeof(int));
    *returnSize = numsSize;
    if(numsSize == 0){
        return ans;
    }
    int stack[numsSize];
    int size = 0;
    for(int i=numsSize-1; i>=0; --i){
        while(size != 0 && stack[size-1] <= nums[i]){
            -- size;
        }
        if(size == 0){
            ans[i] = INT_MIN;
        }
        else{
            ans[i] = stack[size-1];
        }
        stack[size] = nums[i];
        ++ size;
    }
    int j=numsSize-1, i=0;
    size = 0;
    while(i<j){
        while(i<j && nums[i] <= nums[j]){
            ++ i;
        }
        if(i<j){
            ans[j] = nums[i];
            -- j;
        }
        while(i<j && ans[j] != INT_MIN){
            -- j;
        }
    }
    for(int i=0; i<numsSize; ++i){
        if(ans[i] == INT_MIN){
            ans[i] = -1;
        }
    }
    return ans;
}

