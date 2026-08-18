'''
=== 3629. Minimum Jumps to Reach End via Prime Teleportation ===

You are given an integer array nums of length n.
You start at index 0, and your goal is to reach index n - 1.
From any index i, you may perform one of the following operations:
    - Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
    - Prime Teleportation: If nums[i] is a prime number p, you may instantly jump to any index j != i such that nums[j] % p == 0.
Return the minimum number of jumps required to reach index n - 1.
A prime number is a natural number greater than 1 with only two factors, 1 and itself.

Example 1:
    Input: nums = [1,2,4,6]
    Output: 2
    Explanation:
    One optimal sequence of jumps is:
    Start at index i = 0. Take an adjacent step to index 1.
    At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.
    Thus, the answer is 2.
Example 2:
    Input: nums = [2,3,4,7,9]
    Output: 2
    Explanation:
    One optimal sequence of jumps is:
    Start at index i = 0. Take an adjacent step to index i = 1.
    At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.
    Thus, the answer is 2.
Example 3:
    Input: nums = [4,6,5,8]
    Output: 3
    Explanation:
    Since no teleportation is possible, we move through 0 → 1 → 2 → 3. Thus, the answer is 3.

Constraints:
    1. 1 <= n == nums.length <= 105
    2. 1 <= nums[i] <= 106
'''
def get_primes(n):
    status = [0 for _ in range(n+1)]
    primes = set()
    for i in range(2, n+1):
        if status[i] != 0:
            continue
        primes.add(i)
        for j in range(i, n+1, i):
            status[j] = 1
    return primes

PRIMES = get_primes(10**6)
PRIME_LIST = list(sorted(PRIMES))
# === 3037ms && 64.27MB === #
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        # print(n)

        @lru_cache(None)
        def get_prime_factors(num):
            if num in PRIMES:
                return [num]
            idx = bisect.bisect_right(PRIME_LIST, sqrt(num)+1)-1
            for i in range(idx, -1, -1):
                if num % PRIME_LIST[i] == 0:
                    while num % PRIME_LIST[i] == 0:
                        num = num // PRIME_LIST[i]
                    return [PRIME_LIST[i]] + get_prime_factors(num)
            return []
        
        primes = {num for num in nums if num in PRIMES}
        jump = defaultdict(list)
        for i, num in enumerate(nums):
            for p in get_prime_factors(num):
                if p in primes:
                    jump[p].append(i)     
        
        seen = {0}
        q = [(0, 0)]
        while q:
            step, idx = heapq.heappop(q)
            idx = -idx
            # if idx in {191, 134, 454}:
            #     print(f"idx = {idx}, num = {nums[idx]}, step = {step}")
            # seen.add(idx)
            if idx == n-1:
                return step
            if idx-1 >= 0 and idx-1 not in seen:
                heapq.heappush(q, (step+1, -idx+1))
                seen.add(idx-1)
            if idx+1 < n and idx+1 not in seen:
                if idx+1 == n-1:
                    return step+1
                heapq.heappush(q, (step+1, -idx-1))
                seen.add(idx+1)
            if nums[idx] in PRIMES:
                for nxt in jump[nums[idx]]:
                    if nxt == n-1:
                        return step+1
                    if nxt not in seen:
                        heapq.heappush(q, (step+1, -nxt))
                        seen.add(nxt)
        return -1

