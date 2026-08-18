/*
=== 769. Max Chunks To Make Sorted ===

Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.
What is the most number of chunks we could have made?

Example 1:
    Input: arr = [4,3,2,1,0]
    Output: 1
    Explanation:
    Splitting into two or more chunks will not return the required result.
    For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:
    Input: arr = [1,0,2,3,4]
    Output: 4
    Explanation:
    We can split into two chunks, such as [1, 0], [2, 3, 4].
    However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

Note:
    1. arr will have length in range [1, 10].
    2. arr[i] will be a permutation of [0, 1, ..., arr.length - 1].
*/
// === 0ms(100%) && 5.4MB(100%) === //
int maxChunksToSorted(int* arr, int arrSize){
    int max[arrSize], min[arrSize];
    max[0] = arr[0];
    int ans = arr[0] == 0 ? 1 : 0;
    for(int i=1; i<arrSize; ++i){
        max[i] = arr[i] > max[i-1] ? arr[i] : max[i-1];
        if(max[i] == i){
            ++ ans;
        }
    }
    return ans;
}

