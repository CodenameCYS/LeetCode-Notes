/*
=== 1296. Divide Array in Sets of K Consecutive Numbers ===

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

Example 1:
    Input: nums = [1,2,3,3,4,4,5,6], k = 4
    Output: true
    - Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:
    Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
    Output: true
    - Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:
    Input: nums = [3,3,2,2,1,1], k = 3
    Output: true
Example 4:
    Input: nums = [1,2,3,4], k = 3
    Output: false
    - Explanation: Each array should be divided in subarrays of size 3.
 
Constraints:
    1. 1 <= nums.length <= 10^5
    2. 1 <= nums[i] <= 10^9
    3. 1 <= k <= nums.length
*/
void QuickSort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed, tmp = nums[st];
    while(i<j){
        while(i<j && nums[j]>tmp){
            --j;
        }
        if(i<j){
            nums[i] = nums[j];
            ++i;
        }
        while(i<j && nums[i]<tmp){
            ++i;
        }
        if(i<j){
            nums[j] = nums[i];
            --j;
        }
    }
    nums[i] = tmp;
    QuickSort(nums, st, i-1);
    QuickSort(nums, i+1, ed);
}
int InfillOneSet(int* nums, int* state, int numsSize, int flag, int k){
    int next_flag = flag;
    // printf("%d ", nums[flag]);
    int tmp = nums[flag];
    int count = 0;
    while(flag < numsSize && count < k){
        if(state[flag] == 0){
            if(nums[flag] == tmp){
                state[flag] = 1;
                ++ tmp;
                ++ count;
            }
            else if(nums[flag] > tmp){
                return -1;
            }
        }
        ++ flag;
    }
    while(next_flag<numsSize && state[next_flag] == 1){
        ++ next_flag;
    }
    return next_flag;
}
// === 1504ms & 12.4MB === //
bool isPossibleDivide(int* nums, int numsSize, int k){
    if(numsSize % k != 0){
        return false;
    }
    else if(k == 1){
        return true;
    }
    int state[numsSize];
    for(int i=0; i<numsSize; ++i){
        state[i] = 0;
    }
    QuickSort(nums, 0, numsSize-1);
    // printf("quick sort finished!\n");
    int flag = 0;
    while(flag < numsSize){
        flag = InfillOneSet(nums, state, numsSize, flag, k);
        if(flag == -1){
            return false;
        }
    }
    return true;
}