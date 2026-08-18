/*
=== 287. Find the Duplicate Number ===
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
*/
# include <stdio.h>
# include <stdlib.h>

int findDuplicate(int* nums, int numsSize);

int main(){

    int nums[5] = {1,2,2,2,4};
    int numsSize = 5;
    int ans = findDuplicate(nums,numsSize);
    printf("ans = %d\n", ans);

    system("pause");
    return 1;
}

int findDuplicate(int* nums, int numsSize) {
    int count[numsSize];
    for(int i=1; i<numsSize; ++i){
        count[i] = 0;
    }
    for(int i=0; i<numsSize; ++i){
        count[nums[i]] += 1;
        if(count[nums[i]] > 1){
            return nums[i];
        }
    }
    return 0;
}