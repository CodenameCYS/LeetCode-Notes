/*
=== 611. Valid Triangle Number ===

Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
    Input: [2,2,3,4]
    Output: 3
    Explanation:
    Valid combinations are: 
    2,3,4 (using the first 2)
    2,3,4 (using the second 2)
    2,2,3

Note:
    1. The length of the given array won't exceed 1000.
    2. The integers in the given array are in the range of [0, 1000].
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
// === 384ms(26.67%) && 7MB(100%) === //
int triangleNumber(int* nums, int numsSize){
    quick_sort(nums, 0, numsSize-1);
    int ans = 0;
    for(int i=0; i<numsSize-2; ++i){
        for(int j=i+1; j<numsSize-1; ++j){
            for(int k=j+1; k<numsSize && nums[i] + nums[j] > nums[k]; ++k){
                ++ ans;
            }
        }
    }
    return ans;
}

