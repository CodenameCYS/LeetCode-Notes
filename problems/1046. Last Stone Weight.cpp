/*
=== 1046. Last Stone Weight ===

We have a collection of rocks, each rock has a positive integer weight.
Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:
    - If x == y, both stones are totally destroyed;
    - If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Example 1:
    Input: [2,7,4,1,8,1]
    Output: 1
    - Explanation: 
    We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
    we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
    we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
    we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 
Note:
    1. 1 <= stones.length <= 30
    2. 1 <= stones[i] <= 1000
*/
void QuickSort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int i = st, j = ed;
    int temp = nums[st];
    while(i<j){
        while(i<j && nums[j] >= temp){
            --j;
        }
        if(i<j){
            nums[i] = nums[j];
            ++i;
        }
        while(i<j && nums[i] <= temp){
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
// === 0ms && 6.9MB === //
int lastStoneWeight(int* stones, int stonesSize){
    QuickSort(stones, 0, stonesSize-1);
    
    for(int i=stonesSize-2; i>=0; --i){
        stones[i] = stones[i+1] - stones[i];
        if(stones[i] == 0){
            --i;
            continue;
        }
        for(int j=i; j>0; --j){
            if(stones[j] < stones[j-1]){
                int temp = stones[j];
                stones[j] = stones[j-1];
                stones[j-1] = temp;
            }
            else{
                break;
            }
        }
    }
    return stones[0];
}