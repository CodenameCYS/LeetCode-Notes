/*
=== 739. Daily Temperatures ===

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 // === 140ms(100%) && 22.3MB(100%) === //
int* dailyTemperatures(int* T, int TSize, int* returnSize){
    int temp_stack[TSize], day_stack[TSize], size=0;
    int* ans = (int*)malloc(TSize * sizeof(int));
    *returnSize = TSize;
    for(int i=0; i<TSize; ++i){
        while(size > 0 && T[i] > temp_stack[size-1]){
            ans[day_stack[size-1]] = i - day_stack[size-1];
            -- size;
        }
        temp_stack[size] = T[i];
        day_stack[size] = i;
        ++ size;
    }
    for(int i=0; i<size; ++i){
        ans[day_stack[i]] = 0;
    }
    return ans;
}

