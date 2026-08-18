'''
=== 3589. Count Prime-Gap Balanced Subarrays ===

You are given an integer array nums and an integer k.
A subarray is called prime-gap balanced if:
    - It contains at least two prime numbers, and
    - The difference between the maximum and minimum prime numbers in that subarray is less than or equal to k.
Return the count of prime-gap balanced subarrays in nums.
Note:
    - A subarray is a contiguous non-empty sequence of elements within an array.
    - A prime number is a natural number greater than 1 with only two factors, 1 and itself.
 
Example 1:
    Input: nums = [1,2,3], k = 1
    Output: 2
    Explanation:
    Prime-gap balanced subarrays are:
    [2,3]: contains two primes (2 and 3), max - min = 3 - 2 = 1 <= k.
    [1,2,3]: contains two primes (2 and 3), max - min = 3 - 2 = 1 <= k.
    Thus, the answer is 2.
Example 2:
    Input: nums = [2,3,5,7], k = 3
    Output: 4
    Explanation:
    Prime-gap balanced subarrays are:
    [2,3]: contains two primes (2 and 3), max - min = 3 - 2 = 1 <= k.
    [2,3,5]: contains three primes (2, 3, and 5), max - min = 5 - 2 = 3 <= k.
    [3,5]: contains two primes (3 and 5), max - min = 5 - 3 = 2 <= k.
    [5,7]: contains two primes (5 and 7), max - min = 7 - 5 = 2 <= k.
    Thus, the answer is 4.

Constraints:
    1. 1 <= nums.length <= 5 * 104
    2. 1 <= nums[i] <= 5 * 104
    3. 0 <= k <= 5 * 104
'''
def get_primes(n):
    status = [0 for _ in range(n+1)]
    primes = set()
    for i in range(2, n+1):
        if status[i] == 1:
            continue
        primes.add(i)
        for j in range(i, n+1, i):
            status[j] = 1
    return primes

PRIMES = get_primes(50000)
# === 731ms && 21.38MB === #
class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        primes = []
        for i, num in enumerate(nums):
            if num in PRIMES:
                primes.append((i, num))
        n = len(nums)
        i, j, m = 0, 0, len(primes)
        # print(primes)
        _primes = []
        ans = 0
        while j < m:
            bisect.insort(_primes, primes[j][1])
            while i < j and _primes[-1] - _primes[0] > k:
                _primes.pop(bisect.bisect_left(_primes, primes[i][1]))
                i += 1
            if len(_primes) > 1:
                l = primes[j-1][0]+1 if j-1 == 0 or i == 0 else primes[j-1][0] - primes[i-1][0]
                r = n-primes[j][0] if j == m-1 else primes[j+1][0] - primes[j][0]
                ans += l*r
                # print(ans, _primes, i,j,l, r)
            j += 1
        return ans