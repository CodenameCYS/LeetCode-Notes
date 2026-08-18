/*
=== 713. Subarray Product Less Than K ===

Your are given an array of positive integers nums.
Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
    Input: nums = [10, 5, 2, 6], k = 100
    Output: 8
    Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
    Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:
    1. 0 < nums.length <= 50000.
    2. 0 < nums[i] < 1000.
    3. 0 <= k < 10^6.
*/
// === 112ms(100%) && 11.3MB(100%) === //
int numSubarrayProductLessThanK(int* nums, int numsSize, int k){
    int product = 1;
    int i=0,j=0;
    int ans = 0;
    for(;j<numsSize; ++j){
        product *= nums[j];
        while(i<j && product >= k){
            product /= nums[i];
            ++ i;
        }
        if(product < k){
            ans += (j-i+1);
        }
        // printf("st: %d, ed: %d, prodcut: %d, count=%d\n", i, j, product, ans);
    }
    return ans;
}

