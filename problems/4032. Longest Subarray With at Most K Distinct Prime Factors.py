'''
=== 4032. Longest Subarray With at Most K Distinct Prime Factors ===

You are given an integer array nums consisting of positive integers and an integer k.
The prime factor set of a subarray is the union of the distinct prime factors of all its elements.
Return the length of the longest subarray whose prime factor set contains at most k distinct prime factors. If no such subarray exists, return 0.

Example 1:
    Input: nums = [7,6,10,12,11], k = 3
    Output: 3
    Explanation:
    Consider the subarray [6, 10, 12]:
    The distinct prime factors of 6 are {2, 3}.
    The distinct prime factors of 10 are {2, 5}.
    The distinct prime factors of 12 are {2, 3}.
    The union of these sets is {2, 3, 5}, which contains 3 distinct prime factors.
    No longer subarray satisfies the condition. Therefore, the answer is 3.
Example 2:
    Input: nums = [4,6,9,18], k = 4
    Output: 4
    Explanation:
    Consider the entire array [4, 6, 9, 18]:
    The distinct prime factors of 4 are {2}.
    The distinct prime factors of 6 are {2, 3}.
    The distinct prime factors of 9 are {3}.
    The distinct prime factors of 18 are {2, 3}.
    The union of these sets is {2, 3}, which contains 2 distinct prime factors.
    Since 2 <= 4, the entire array is valid. Therefore, the answer is 4.
Example 3:
    Input: nums = [6,10,15], k = 2
    Output: 1
    Explanation:
    Every subarray of length at least 2 has prime factor set {2, 3, 5}, which contains 3 distinct prime factors.
    Since 3 > 2, only subarrays of length 1 are valid. Therefore, the answer is 1.

Constraints:
    1. 1 <= nums.length <= 105
    2. 2 <= nums[i] <= 105
    3. 1 <= k <= 104
'''
# === 1282ms && 44.19MB === #
def get_primes(n):
    ans = []
    status = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        if status[i] != 0:
            continue
        ans.append(i)
        for j in range(i, n+1, i):
            status[j] = 1
    return ans

PRIMES = get_primes(10**5)
PRIME_SET = set(PRIMES)

@lru_cache(None)
def get_factors(n):
    ans = []
    for p in PRIMES:
        if n % p != 0:
            continue
        ans.append(p)
        while n % p == 0:
            n = n // p 
        if n in PRIME_SET:
            ans.append(n)
            break
        elif n == 1:
            break
    return ans

class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        cnt = defaultdict(int)
        i, j, n = 0, 0, len(nums)
        ans = 0
        while j < n:
            primes = get_factors(nums[j])
            for p in primes:
                cnt[p] += 1
            j += 1
            while i < j and len(cnt) > k:
                _primes = get_factors(nums[i])
                for p in _primes:
                    cnt[p] -= 1
                    if cnt[p] == 0:
                        cnt.pop(p)
                i += 1
            ans = max(ans, j-i)
        return ans