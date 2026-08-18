/*
=== 215. Kth Largest Element in an Array ===

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
    Input: [3,2,1,5,6,4] and k = 2
    Output: 5

Example 2:
    Input: [3,2,3,1,2,4,5,5,6] and k = 4
    Output: 4

Note: 
    You may assume k is always valid, 1 ≤ k ≤ array's length.
*/
void QuickSort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int temp = nums[st];
    int i=st, j=ed;
    while(i<j){
        while(i<j && nums[j]<=temp){
            --j;
        }
        if(i<j){
            nums[i] = nums[j];
            ++i;
        }
        while(i<j && nums[i]>=temp){
            ++i;
        }
        if(i<j){
            nums[j] = nums[i];
            --j;
        }
    }
    nums[i] = temp;
    QuickSort(nums, st, i-1);
    QuickSort(nums, i+1, ed);
}

int findKthLargest(int* nums, int numsSize, int k) {
    QuickSort(nums, 0, numsSize-1);
    return nums[k-1];
}