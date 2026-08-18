/*
=== 350. Intersection of Two Arrays II ===

Given two arrays, write a function to compute their intersection.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]
Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]

Note:
    1. Each element in the result should appear as many times as it shows in both arrays.
    2. The result can be in any order.

Follow up:
    1. What if the given array is already sorted? How would you optimize your algorithm?
    2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
    3. What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
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
        if(i < j){
            nums[j] = nums[i];
            -- j;
        }
    }
    nums[i] = tmp;
    quick_sort(nums, st, i-1);
    quick_sort(nums, i+1, ed);
}
// === 8ms(73.11%) && 7.5MB(100%) === //
int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){
    quick_sort(nums1, 0, nums1Size-1);
    quick_sort(nums2, 0, nums2Size-1);
    int n = nums1Size < nums2Size ? nums1Size : nums2Size;
    *returnSize=0;
    int* ans = (int*)malloc(n*sizeof(int));
    int i=0, j=0;
    while(i<nums1Size && j<nums2Size){
        if(nums1[i] == nums2[j]){
            ans[*returnSize] = nums1[i];
            ++ i;
            ++ j;
            ++ *returnSize;
        }
        else if(nums1[i] < nums2[j]){
            ++ i;
        }
        else{
            ++ j;
        }
    }
    return ans;
}

