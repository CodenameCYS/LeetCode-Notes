/*
=== 15. 3Sum ===

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
    - The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
] ===
*/
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
void QuickSort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int tmp = nums[st];
    int i=st, j=ed;
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
    QuickSort(nums, st, i-1);
    QuickSort(nums, i+1, ed);
}
// === 120ms(95.07%) && 37.4MB(25%) === // 
int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    QuickSort(nums, 0, numsSize-1);
    
    int** ans = (int**)malloc(20000*sizeof(int*));
    returnColumnSizes[0] = (int*)malloc(20000*sizeof(int));
    *returnSize = 0;
    int i=0;
    while(i<numsSize-2 && nums[i] <= 0){
        int j = i+1, k = numsSize-1;
        int a = nums[i];
        while(j<k){
            int b = nums[j], c = nums[k];
            if(a + b + c == 0){
                ans[*returnSize] = (int*)malloc(3*sizeof(int));
                ans[*returnSize][0] = a;
                ans[*returnSize][1] = b;
                ans[*returnSize][2] = c;
                returnColumnSizes[0][*returnSize] = 3;
                ++ *returnSize;
                while(j<k && nums[j] == b){
                    ++ j;
                }
                while(j<k && nums[k] == c){
                    -- k;
                }
                // printf("%d\t%d\t%d\n", a, b, c);
            }
            else if(a + b + c < 0){
                while(j<k && nums[j] == b){
                    ++ j;
                }
            }
            else{
                while(j<k && nums[k] == c){
                    -- k;
                }
            }
        }
        while(i<numsSize-2 && nums[i] == a){
                ++ i;
        }
    }
    return ans;
}

