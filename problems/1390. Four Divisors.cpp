/*
=== 1390. Four Divisors ===

Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.
If there is no such integer in the array, return 0.

Example 1:
    Input: nums = [21,4,7]
    Output: 32
    Explanation:
    21 has 4 divisors: 1, 3, 7, 21
    4 has 3 divisors: 1, 2, 4
    7 has 2 divisors: 1, 7
    The answer is the sum of divisors of 21 only.
 
Constraints:
    1. 1 <= nums.length <= 10^4
    2. 1 <= nums[i] <= 10^5
*/
int sum_of_four_divisors(int num){
    int n = (int)sqrt(num);
    if(num == n*n){
        return -1;
    }
    int ans = 1 + num;
    bool has_find_divisor = false;
    for(int i=2; i<=n; ++i){
        if(num % i == 0){
            if(has_find_divisor){
                return -1;
            }
            else{
                ans += (i + num/i);
                has_find_divisor = true;
            }
        }
    }
    return has_find_divisor ? ans : -1;
}
// === 20ms && 5.9MB === //
int sumFourDivisors(int* nums, int numsSize){
    int ans = 0;
    for(int i=0; i<numsSize; ++i){
        int s = sum_of_four_divisors(nums[i]);
        // printf("%d -> %d\n", nums[i], s);
        if(s != -1){
            ans += s;
        }
    }
    return ans;
}

