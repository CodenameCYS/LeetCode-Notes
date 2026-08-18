'''
=== 3984. Divisible Game ===

You are given an integer array nums of length n.
Alice and Bob are playing a game. Alice chooses:
    - An integer k such that k > 1.
    - Two integers l and r such that 0 <= l <= r < n.
Initially, both Alice's and Bob's scores are 0.
For each index i in the range [l, r] (inclusive):
    - If nums[i] is divisible by k, Alice's score increases by nums[i].
    - Otherwise, Bob's score increases by nums[i].
The score difference is Alice's score minus Bob's score.
Alice wants to maximize the score difference. If there are multiple values of k that achieve the maximum score difference, she chooses the smallest such k.
Return the product of the maximum score difference and the chosen value of k. Since the result can be large, return it modulo 109 + 7.

Example 1:
    Input: nums = [1,4,6,8]
    Output: 36
    Explanation:
    Alice can choose k = 2, l = 1, and r = 3.
    All values in nums[1..3] are divisible by 2, so Alice's score is 4 + 6 + 8 = 18, while Bob's score is 0.
    The score difference is 18, which is the maximum possible. Among all values of k that achieve this score difference, the smallest is 2.
    Therefore, the answer is 18 * 2 = 36.
Example 2:
    Input: nums = [2,1,2]
    Output: 6
    Explanation:
    Alice can choose k = 2, l = 0, and r = 2.
    The values nums[0] and nums[2] are divisible by 2, so Alice's score is 2 + 2 = 4. The value nums[1] is not divisible by 2, so Bob's score is 1.
    The score difference is 4 - 1 = 3, which is the maximum possible. Among all values of k that achieve this score difference, the smallest is 2.
    Therefore, the answer is 3 * 2 = 6.
Example 3:
    Input: nums = [1]
    Output: 1000000005
    Explanation:
    Alice must choose some k > 1. The smallest possible choice is k = 2.
    Since nums[0] is not divisible by 2, Alice's score is 0, while Bob's score is 1.
    The score difference is -1, which is the maximum possible.
    Therefore, the answer is -1 * 2 = -2. Modulo 109 + 7, this equals 1000000005.
 
Constraints:
    - 1 <= nums.length <= 1000
    - 1 <= nums[i] <= 106
'''
MOD = 10**9+7

def get_primes(n):
    primes = []
    status = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        if status[i] != 0:
            continue
        primes.append(i)
        for j in range(i, n+1, i):
            status[j] = 1
    return primes

PRIMES = get_primes(10**6)
# === 14799ms && 29.98MB === #
class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        _max = max(nums)
        tot = sum(nums) - 2 * Counter(nums)[1]

        def get_score(nums, p):
            l, s = 0, 0
            score = -math.inf
            for num in nums:
                if num % p == 0:
                    s += num
                else:
                    s -= num
                score = max(score, s-l)
                l = min(s, l)
            return score

        elems = Counter([x for x in nums if x != 1])
        if len(elems) == 0:
            return -2 % MOD
        elif len(elems) == 1:
            num = list(elems.keys())[0]
            for p in PRIMES:
                if num % p == 0:
                    return (p * get_score(nums, p)) % MOD

        elems = list(elems.keys())
        primes = [p for p in PRIMES if p<=_max and any(x % p == 0 for x in elems)]

        score = -math.inf
        ans = 0
        for p in primes:
            if p > _max:
                return ans
            _score = get_score(nums, p)
            if _score > score:
                score = _score
                ans = (_score * p) % MOD
            if score == tot:
                return ans
        return ans
        