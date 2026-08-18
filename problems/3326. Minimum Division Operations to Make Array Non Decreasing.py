'''
=== 3326. Minimum Division Operations to Make Array Non Decreasing ===

You are given an integer array nums.
Any positive divisor of a natural number x that is strictly less than x is called a proper divisor of x. For example, 2 is a proper divisor of 4, while 6 is not a proper divisor of 6.
You are allowed to perform an operation any number of times on nums, where in each operation you select any one element from nums and divide it by its greatest proper divisor.
Return the minimum number of operations required to make the array non-decreasing.
If it is not possible to make the array non-decreasing using any number of operations, return -1.

Example 1:
    Input: nums = [25,7]
    Output: 1
    Explanation:
    Using a single operation, 25 gets divided by 5 and nums becomes [5, 7].
Example 2:
    Input: nums = [7,7,6]
    Output: -1
Example 3:
    Input: nums = [1,1,1,1]
    Output: 0

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 106
'''
def get_primes(n):
    status = [0 for _ in range(n+1)]
    primes = []
    for i in range(2, n+1):
        if status[i] == 1:
            continue
        primes.append(i)
        for j in range(i, n+1, i):
            status[j] = 1
    return primes

PRIMES = get_primes(10**5+1)
# === 794ms && 30.6MB === #
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        def fn(num, _max):
            for i in PRIMES:
                if i > _max:
                    break
                if num % i == 0:
                    return i
            return -1
        
        _max = nums[-1]
        ans = 0
        for num in nums[::-1]:
            if num <= _max:
                _max = num
                continue
            else:
                num = fn(num, _max)
                if num == -1:
                    return -1
                else:
                    _max = num
                    ans += 1
        return ans
            
        