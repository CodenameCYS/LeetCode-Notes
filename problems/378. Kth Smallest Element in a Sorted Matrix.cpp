/*
=== 378. Kth Smallest Element in a Sorted Matrix ===

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
- Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:
    matrix = [
        [ 1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ],
    k = 8,
    return 13.

Note:
- You may assume k is always valid, 1 ≤ k ≤ n2.
*/
void quick_sort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed, tmp=nums[st];
    while(i<j){
        while(i<j && nums[j]>=tmp){
            --j;
        }
        if(i<j){
            nums[i] = nums[j];
            ++i;
        }
        while(i<j && nums[i]<=tmp){
            ++i;
        }
        if(i<j){
            nums[j] = nums[i];
            --j;
        }
    }
    nums[i] = tmp;
    quick_sort(nums, st, i-1);
    quick_sort(nums, i+1, ed);
}
// === 76ms(58.83%) && 9.5MB(100%) === //
int kthSmallest(int** matrix, int matrixSize, int* matrixColSize, int k){
    int m=matrixSize, n=matrixColSize[0];
    int nums[m*n];
    int numsSize = 0;
    for(int i=0; i<m; ++i){
        for(int j=0; j<n; ++j){
            nums[numsSize] = matrix[i][j];
            ++ numsSize;
        }
    }
    quick_sort(nums, 0, numsSize-1);
    return nums[k-1];
}

