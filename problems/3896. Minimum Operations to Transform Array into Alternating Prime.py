'''
=== 3896. Minimum Operations to Transform Array into Alternating Prime ===

You are given an integer array nums.
An array is considered alternating prime if:
    - Elements at even indices (0-based) are prime numbers.
    - Elements at odd indices are non-prime numbers.
In one operation, you may increment any element by 1.
Return the minimum number of operations required to transform nums into an alternating prime array.
A prime number is a natural number greater than 1 with only two factors, 1 and itself.

Example 1:
    Input: nums = [1,2,3,4]
    Output: 3
    Explanation:
    The element at index 0 must be prime. Increment nums[0] = 1 to 2, using 1 operation.
    The element at index 1 must be non-prime. Increment nums[1] = 2 to 4, using 2 operations.
    The element at index 2 is already prime.
    The element at index 3 is already non-prime.
    Total operations = 1 + 2 = 3.
Example 2:
    Input: nums = [5,6,7,8]
    Output: 0
    Explanation:
    The elements at indices 0 and 2 are already prime.
    The elements at indices 1 and 3 are already non-prime.
    No operations are needed.
Example 3:
    Input: nums = [4,4]
    Output: 1
    Explanation:
    The element at index 0 must be prime. Increment nums[0] = 4 to 5, using 1 operation.
    The element at index 1 is already non-prime.
    Total operations = 1.

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 105
'''
def get_primes(n):
    primes = []
    status = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        if status[i] == 1:
            continue
        primes.append(i)
        for j in range(i, n+1, i):
            status[j] = 1
    return primes

PRIMES = get_primes(200000)
# === 232ms && 34.84MB === #
class Solution:
    def minOperations(self, nums: list[int]) -> int:
         
        def diff_to_prime(num):
            idx = bisect.bisect_left(PRIMES, num)
            if PRIMES[idx] == num:
                return 0
            return PRIMES[idx]-num
        
        ans = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                ans += diff_to_prime(num)
            else:
                if 1 < num <= 3:
                    ans += (4-num)
                elif diff_to_prime(num) == 0:
                    ans += 1
        return ans
             