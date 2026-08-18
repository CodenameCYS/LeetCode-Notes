/*
=== 1218. Longest Arithmetic Subsequence of Given Difference ===

Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.
 
Example 1:
    Input: arr = [1,2,3,4], difference = 1
    Output: 4
    - Explanation: The longest arithmetic subsequence is [1,2,3,4].
Example 2:
    Input: arr = [1,3,5,7], difference = 1
    Output: 1
    - Explanation: The longest arithmetic subsequence is any single element.
Example 3:
    Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
    Output: 4
    - Explanation: The longest arithmetic subsequence is [7,5,3,1].
 
Constraints:
    1. 1 <= arr.length <= 10^5
    2. -10^4 <= arr[i], difference <= 10^4
*/
// === 72ms & 13MB === //
int longestSubsequence(int* arr, int arrSize, int difference){
    int tmp[20001];
    for(int i=0; i<20001; ++i){
        tmp[i] = 0;
    }
    for(int i=0; i<arrSize; ++i){
        if(arr[i]-difference >= -10000 && arr[i]-difference <= 10000){
            tmp[arr[i]+10000] = tmp[arr[i]-difference+10000] + 1;
        }
        else{
            tmp[arr[i]+10000] = 1;
        }
    }
    int max = 1;
    for(int i=0; i<20001; ++i){
        max = max > tmp[i] ? max : tmp[i];
    }
    return max;
}

