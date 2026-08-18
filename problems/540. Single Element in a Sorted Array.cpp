/*
=== 540. Single Element in a Sorted Array ===

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Example 1:
    Input: [1,1,2,3,3,4,4,8,8]
    Output: 2
Example 2:
    Input: [3,3,7,7,10,11,11]
    Output: 10
 
Note: Your solution should run in O(log n) time and O(1) space.
*/
int find(int* nums, int st, int ed){
    if(ed - st == 0){
        return nums[st];
    }
    int mid = (st + ed) / 2;
    // printf("%d, %d, %d\n", st, mid, ed);
    if(nums[mid-1] == nums[mid]){
        if((mid-st+1) % 2 == 0){
            return find(nums, mid+1, ed);
        }
        else{
            return find(nums, st, mid-2);
        }
    }
    else if(nums[mid] == nums[mid+1]){
        if((ed-mid+1) % 2 == 0){
            return find(nums, st, mid-1);
        }
        else{
            return find(nums, mid+2, ed);
        }
    }
    else{
        return nums[mid];
    }
}
// === 4ms(100%) && 7.9MB(33.33%) === //
int singleNonDuplicate(int* nums, int numsSize){
    if(numsSize == 0){
        return 0;
    }
    return find(nums, 0, numsSize-1);
}

