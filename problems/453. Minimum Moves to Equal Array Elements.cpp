/*
=== 453. Minimum Moves to Equal Array Elements ===

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:
    Input:
    [1,2,3]
    Output:
    3
    Explanation:
    Only three moves are needed (remember each move increments two elements):
    [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
*/
// === 36ms(90.48%) && 8.5MB(100%) === //
int minMoves(int* nums, int numsSize){
    if(numsSize <= 1){
        return 0;
    }
    int min=nums[0];
    for(int i=1; i<numsSize; ++i){
        min = nums[i] < min ? nums[i] : min;
    }
    int ans = 0;
    for(int i=0; i<numsSize; ++i){
        ans += nums[i] - min;
    }
    return ans;
}

