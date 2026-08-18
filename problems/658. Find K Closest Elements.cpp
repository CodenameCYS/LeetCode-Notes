/*
=== 658. Find K Closest Elements ===

Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
    Input: [1,2,3,4,5], k=4, x=3
    Output: [1,2,3,4]
Example 2:
    Input: [1,2,3,4,5], k=4, x=-1
    Output: [1,2,3,4]

Note:
    1. The value k is positive and will always be smaller than the length of the sorted array.
    2. Length of the given array is positive and will not exceed 104
    3. Absolute value of elements in the array and x will not exceed 104
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int find_closest(int* arr, int arrSize, int x){
    int dis = abs(x-arr[0]);
    int loc = 0;
    for(int i=1; i<arrSize && abs(x-arr[i])<=dis; ++i){
        dis = abs(x-arr[i]);
        loc = i;
    }
    return loc;
}
// === 72ms(100%) && 14.5MB(100%) === //
int* findClosestElements(int* arr, int arrSize, int k, int x, int* returnSize){
    int st = find_closest(arr, arrSize, x), ed = st;
    while(ed - st < k-1){
        int i=st-1, j=ed+1;
        if(i < 0){
            ++ ed;
        }
        else if(j >= arrSize){
            -- st;
        }
        else{
            if(abs(arr[i]-x) <= abs(arr[j]-x)){
                -- st;
            }
            else{
                ++ ed;
            }
        }
    }
    *returnSize = k;
    return &(arr[st]);
}

