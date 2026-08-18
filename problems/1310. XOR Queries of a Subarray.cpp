/*
=== 1310. XOR Queries of a Subarray ===

Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ). Return an array containing the result for the given queries.
 
Example 1:
    Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
    Output: [2,7,14,8] 
    - Explanation: 
    The binary representation of the elements in the array are:
    1 = 0001 
    3 = 0011 
    4 = 0100 
    8 = 1000 
    The XOR values for queries are:
    [0,1] = 1 xor 3 = 2 
    [1,2] = 3 xor 4 = 7 
    [0,3] = 1 xor 3 xor 4 xor 8 = 14 
    [3,3] = 8
Example 2:
    Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
    Output: [8,0,4,4]
 
Constraints:
    1. 1 <= arr.length <= 3 * 10^4
    2. 1 <= arr[i] <= 10^9
    3. 1 <= queries.length <= 3 * 10^4
    4. queries[i].length == 2
    5. 0 <= queries[i][0] <= queries[i][1] < arr.length
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int xor(int x, int y){
    int ans = 0;
    int base = 1;
    while(x != 0 || y != 0){
        ans = ans + base * ((x + y) % 2);
        base *= 2;
        x /= 2;
        y /= 2;
    }
    return ans;
}
// === 128ms & 21.9MB === //
int* xorQueries(int* arr, int arrSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize){
    int* ans = (int*)malloc(queriesSize*sizeof(int));
    *returnSize = queriesSize;
    
    int xor_arr[arrSize + 1];
    xor_arr[0] = 0;
    for(int i=0; i<arrSize; ++i){
        xor_arr[i+1] = xor(xor_arr[i], arr[i]);
    }
    
    for(int i=0; i<queriesSize; ++i){
        ans[i] = xor(xor_arr[queries[i][0]], xor_arr[queries[i][1]+1]);
    }
    return ans;
}