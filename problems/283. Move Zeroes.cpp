/*
=== 283. Move Zeroes ===

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

Note:
    - You must do this in-place without making a copy of the array.
    - Minimize the total number of operations.

*/
// === 24ms(11.08%) & 8.9MB(57.43%) === //
void moveToEnd(int* nums, int numsSize){
    if(numsSize <= 0){
        return;
    }
    int temp = nums[0];
    for(int i=1; i<numsSize; ++i){
        nums[i-1] = nums[i];
    }
    nums[numsSize-1] = temp;
}
void moveZeroes(int* nums, int numsSize) {
    int zeronum = 0;
    for(int i=0; i<numsSize-zeronum; ++i){
        if(nums[i] == 0){
            moveToEnd(&nums[i], numsSize-zeronum-i);
            --i;
            ++zeronum;
        }
    }
}
// === 12ms(43.70%) & 8.9MB(60.13%) === //
void moveZeroes(int* nums, int numsSize) {
    int* ans = nums;
    int loc = 0;
    for(int i=0; i<numsSize; ++i){
        if(nums[i] != 0){
            ans[loc] = nums[i];
            ++loc;
        }
    }
    for(; loc<numsSize; ++loc){
        ans[loc] = 0;
    }
}