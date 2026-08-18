'''
=== 3266. Final Array State After K Multiplication Operations II ===

You are given an integer array nums, an integer k, and an integer multiplier.
You need to perform k operations on nums. In each operation:
    - Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
    - Replace the selected minimum value x with x * multiplier.
After the k operations, apply modulo 109 + 7 to every value in nums.
Return an integer array denoting the final state of nums after performing all k operations and then applying the modulo.

Example 1:
    Input: nums = [2,1,3,5,6], k = 5, multiplier = 2
    Output: [8,4,6,5,6]
    Explanation:
    Operation	Result
    After operation 1	[2, 2, 3, 5, 6]
    After operation 2	[4, 2, 3, 5, 6]
    After operation 3	[4, 4, 3, 5, 6]
    After operation 4	[4, 4, 6, 5, 6]
    After operation 5	[8, 4, 6, 5, 6]
    After applying modulo	[8, 4, 6, 5, 6]
Example 2:
    Input: nums = [100000,2000], k = 2, multiplier = 1000000
    Output: [999999307,999999993]
    Explanation:
    Operation	Result
    After operation 1	[100000, 2000000000]
    After operation 2	[100000000000, 2000000000]
    After applying modulo	[999999307, 999999993]
 
Constraints:
    1. 1 <= nums.length <= 104
    2. 1 <= nums[i] <= 109
    3. 1 <= k <= 109
    4. 1 <= multiplier <= 106
'''
MOD = 10**9+7

@lru_cache(None)
def pow_fn(x, r):
    if r == 0:
        return 1
    elif r == 1:
        return x
    else:
        return (pow_fn(x, r//2) * pow_fn(x, r-r//2)) % MOD

# === 508ms && 20.9MB === #
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums
        n = len(nums)
        q = [(-math.inf, x, i) for i, x in enumerate(nums)]
        _max = max(q)
        heapq.heapify(q)
        while k > 0:
            mod, x, i = heapq.heappop(q)
            y = x * multiplier
            if mod == -math.inf:
                a, b = y // MOD, y % MOD
                if a > 0:
                    nx = (math.log(a), b, i)
                else:
                    nx = (-math.inf, b, i)
            else:
                a, b = y // MOD, y % MOD
                if a > 0:
                    nx = (mod + math.log(a), b, i)
                else:
                    nx = (mod, b, i)
            heapq.heappush(q, nx)
            k -= 1
            if nx >= _max:
                break
        # print(q, k)
        m, r = k // n, k % n
        q = sorted(q)
        # print(q, k, m, r)
        ans = deepcopy(nums)
        for i, (_, x, idx) in enumerate(q):
            if i < r:
                ans[idx] = (x * pow_fn(multiplier, m+1)) % MOD
            else:
                ans[idx] = (x * pow_fn(multiplier, m)) % MOD
        return ans

# === 444ms && 20.4MB === #
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums
        n = len(nums)
        q = [(x, i) for i, x in enumerate(nums)]
        _max = max(nums)
        heapq.heapify(q)
        while k > 0:
            x, i = heapq.heappop(q)
            y = x * multiplier
            heapq.heappush(q, (y, i))
            k -= 1
            if y > _max:
                break

        m, r = k // n, k % n
        q = sorted(q)
        ans = deepcopy(nums)
        for i, (x, idx) in enumerate(q):
            if i < r:
                ans[idx] = (x * pow_fn(multiplier, m+1)) % MOD
            else:
                ans[idx] = (x * pow_fn(multiplier, m)) % MOD
        return ans

# === 501ms && 19.4MB === #
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums
        n = len(nums)
        q = [(x, i) for i, x in enumerate(nums)]
        _max = max(nums)
        heapq.heapify(q)
        while k > 0:
            x, i = heapq.heappop(q)
            y = x * multiplier
            heapq.heappush(q, (y, i))
            k -= 1
            if y > _max:
                break

        m, r = k // n, k % n
        q = sorted(q)
        ans = deepcopy(nums)
        for i, (x, idx) in enumerate(q):
            if i < r:
                ans[idx] = (x * pow(multiplier, m+1, MOD)) % MOD
            else:
                ans[idx] = (x * pow(multiplier, m, MOD)) % MOD
        return ans