/*
=== 167. Two Sum II - Input array is sorted ===

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:
    1. Your returned answers (both index1 and index2) are not zero-based.
    2. You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    - Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int find_target(int* numbers, int target, int st, int ed){
    if(numbers[st] == target){
        return st;
    }
    else if(numbers[ed] == target){
        return ed;
    }
    while(ed - st > 1){
        int tmp = (st+ed)/2;
        if(numbers[tmp] == target){
            return tmp;
        }
        else if(numbers[tmp] < target){
            st = tmp;
        }
        else{
            ed = tmp;
        }
    }
    return -1;
}
// === 12ms(38.39%) && 8MB(42.86%) === //
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int* ans = (int*)malloc(2*sizeof(int));
    *returnSize = 2;
    for(int i=0; i<numbersSize-1; ++i){
        // printf("%d ::\n", i);
        int tmp = find_target(numbers, target - numbers[i], i+1, numbersSize-1);
        if(tmp != -1){
            ans[0] = i + 1;
            ans[1] = tmp + 1;
            // printf("%d\t%d\n", i, tmp);
            return ans;
        }
    }
    return ans;
}
// === 4ms(96.68%) && 7.9MB(100%) === //
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int* ans = (int*)malloc(2*sizeof(int));
    *returnSize = 2;
    int l=0, r=numbersSize-1;
    while(l<r){
        int sum = numbers[l] + numbers[r];
        if(sum == target){
            ans[0] = l+1;
            ans[1] = r+1;
            return ans;
        }
        else if(sum < target){
            ++ l;
        }
        else{
            -- r;
        }
    }
    return ans;
}