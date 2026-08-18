'''
=== 2584. Split the Array to Make Coprime Products ===

You are given a 0-indexed integer array nums of length n.
A split at an index i where 0 <= i <= n - 2 is called valid if the product of the first i + 1 elements and the product of the remaining elements are coprime.
    - For example, if nums = [2, 3, 3], then a split at the index i = 0 is valid because 2 and 9 are coprime, while a split at the index i = 1 is not valid because 6 and 3 are not coprime. A split at the index i = 2 is not valid because i == n - 1.
Return the smallest index i at which the array can be split validly or -1 if there is no such split.
Two values val1 and val2 are coprime if gcd(val1, val2) == 1 where gcd(val1, val2) is the greatest common divisor of val1 and val2.

Example 1:
    Input: nums = [4,7,8,15,3,5]
    Output: 2
    Explanation: The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i.
    The only valid split is at index 2.
Example 2:
    Input: nums = [4,7,15,8,3,5]
    Output: -1
    Explanation: The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i.
    There is no valid split.
 
Constraints:
    1. n == nums.length
    2. 1 <= n <= 104
    3. 1 <= nums[i] <= 106
'''
@lru_cache(None)
def get_primes():
    primes = []
    status = [0 for _ in range(10**6)]
    for i in range(2, 10**6):
        if status[i] == 1:
            continue
        primes.append(i)
        for j in range(i, 10**6, i):
            status[j] = 1
    return primes
# === 747ms && 24.9MB === #
class Solution:
    
    primes = get_primes()
    primes_set = set(primes)
    
    def findValidSplit(self, nums: List[int]) -> int:
        # print(primes)
        cnt = defaultdict(int)
        for x in nums:
            for p in self.primes:
                if x in self.primes_set:
                    cnt[x] += 1
                    break
                if p > x:
                    break
                while x % p == 0:
                    cnt[p] += 1
                    x = x // p
        # print(cnt)
        
        s = defaultdict(int)
        for i, x in enumerate(nums[:-1]):
            for p in self.primes:
                if x in self.primes_set:
                    s[x] += 1
                    break
                if p > x:
                    break
                while x % p == 0:
                    s[p] += 1
                    x = x // p
            if all(s[k] == cnt[k] for k in s):
                return i
        return -1