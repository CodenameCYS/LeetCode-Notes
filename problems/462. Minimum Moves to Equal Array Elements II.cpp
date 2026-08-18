/*
=== 462. Minimum Moves to Equal Array Elements II ===

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.
You may assume the array's length is at most 10,000.

Example:
    Input:
    [1,2,3]
    Output:
    2
    Explanation:
    Only two moves are needed (remember each move increments or decrements one element):
    [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
*/
long cal_moves(int* nums, int numsSize, int base){
    long ans = 0;
    for(int i=0; i<numsSize; ++i){
        ans += abs(nums[i] - base);
    }
    return ans;
}
// === 868ms(11.11%) && 7.6MB(100%) === //
int minMoves2(int* nums, int numsSize){
    if(numsSize <= 1){
        return 0;
    }
    long ans = cal_moves(nums, numsSize, nums[0]);
    for(int i=1; i<numsSize; ++i){
        long tmp = cal_moves(nums, numsSize, nums[i]);
        ans = ans < tmp ? ans : tmp;
    }
    return ans;
}
// ==================================================================================== //
void quick_sort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed, tmp=nums[st];
    while(i<j){
        while(i<j && nums[j] >= tmp){
            --j;
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
    quick_sort(nums, st, i-1);
    quick_sort(nums, i+1, ed);
}
// === 184ms(11.11%) && 8MB(100%) === //
int minMoves2(int* nums, int numsSize){
    if(numsSize <= 1){
        return 0;
    }
    quick_sort(nums, 0, numsSize-1);
    int base = nums[numsSize/2];
    int ans = 0;
    for(int i=0; i<numsSize; ++i){
        ans += abs(nums[i] - base);
    }
    return ans;
}


