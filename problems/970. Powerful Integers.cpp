/*
=== 970. Powerful Integers ===

Given two non-negative integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.
Return a list of all powerful integers that have value less than or equal to bound.
You may return the answer in any order.  In your answer, each value should occur at most once.

Example 1:
    Input: x = 2, y = 3, bound = 10
    Output: [2,3,4,5,7,9,10]
Explanation: 
    2 = 2^0 + 3^0
    3 = 2^1 + 3^0
    4 = 2^0 + 3^1
    5 = 2^1 + 3^1
    7 = 2^2 + 3^1
    9 = 2^3 + 3^0
    10 = 2^0 + 3^2
Example 2:
    Input: x = 3, y = 5, bound = 15
    Output: [2,4,6,8,10,14]

Note:
    1. 1 <= x <= 100
    2. 1 <= y <= 100
    3. 0 <= bound <= 10^6
*/
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
// === 0ms === //
void QuickSort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int i = st, j = ed, temp = nums[st];
    while(i < j){
        while(i < j && nums[j] >= temp){
            --j;
        }
        if(i < j){
            nums[i] = nums[j];
            ++i;
        }
        while(i < j && nums[i] <= temp){
            ++i;
        }
        if(i < j){
            nums[j] = nums[i];
            --j;
        }
    }
    nums[i] = temp;
    QuickSort(nums, st, i-1);
    QuickSort(nums, i+1, ed);
}
void removeDuplicated(int* nums, int* returnSize){
    int original_size = *returnSize;
    int loc = 0;
    for(int i = 1; i<original_size; ++i){
        if(nums[loc] == nums[i]){
            *returnSize -= 1;
            continue;
        }
        nums[loc+1] = nums[i];
        ++ loc;
    }
    // printf("%d\t%d\n", original_size, *returnSize);
}
int* powerfulIntegers(int x, int y, int bound, int* returnSize) {
    if(bound <= 1){
        *returnSize == 0;
        return NULL;
    }
    int maxsize;
    int* ans;
    if(x == 1 && y == 1){
        *returnSize = 1;
        ans = (int*)malloc(sizeof(int));
        *ans = 2;
        return ans;
    }
    else if(x == 1){
        maxsize = 2 + log(bound)/log(y);
        ans = (int*)malloc(maxsize * sizeof(int));
        *returnSize = 0;
        for(int temp = 1; temp < bound; temp *= y){
            ans[*returnSize] = 1 + temp;
            ++ *returnSize;
        }
        return ans;
    }
    else if(y == 1){
        *returnSize = 2 + log(bound)/log(x);
        ans = (int*)malloc(maxsize * sizeof(int));
        *returnSize = 0;
        for(int temp = 1; temp < bound; temp *= x){
            ans[*returnSize] = 1 + temp;
            ++ *returnSize;
        }
        return ans;
    }
    else{
        maxsize = (int)(log(bound)/log(x) + 1) * (int)(log(bound)/log(y) + 1);
        ans = (int*)malloc(maxsize * sizeof(int));
        *returnSize = 0;
        for(int i = 1; i < bound; i *= x){
            int loc = 0;
            for(int j = 1; i + j <= bound; j *= y){
                ans[*returnSize] = i + j;
                ++ *returnSize;
            }
        }
    }
    QuickSort(ans, 0, *returnSize-1);
    // printf("%d\n", *returnSize);
    removeDuplicated(ans, returnSize);
    // printf("%d\n", *returnSize);
    return ans;
}