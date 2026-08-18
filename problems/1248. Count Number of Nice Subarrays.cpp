/*
=== 1248. Count Number of Nice Subarrays ===

Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.

Example 1:
    Input: nums = [1,1,2,1,1], k = 3
    Output: 2
    - Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:
    Input: nums = [2,4,6], k = 1
    Output: 0
    - Explanation: There is no odd numbers in the array.
Example 3:
    Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
    Output: 16
 
Constraints:
    1. 1 <= nums.length <= 50000
    2. 1 <= nums[i] <= 10^5
    3. 1 <= k <= nums.length
*/
// === 108ms && 12MB === //
int numberOfSubarrays(int* nums, int numsSize, int k){
    int even_num[numsSize + 1];
    int odd_num = 0;
    int count = 0;
    for(int i=0; i<numsSize; ++i){
        if(nums[i] % 2 == 0){
            ++ count;
        }
        else{
            even_num[odd_num] = count + 1;
            ++ odd_num;
            count = 0;
        }
    }
    even_num[odd_num] = count + 1;
    
    int ans = 0;
    for(int i=0; i<=odd_num-k; ++i){
        ans += even_num[i] * even_num[i+k];
    }
    return ans;
}

