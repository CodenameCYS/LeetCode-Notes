'''
# === 3130. Find All Possible Stable Binary Arrays II === #

You are given 3 positive integers zero, one, and limit.
A binary array arr is called stable if:
    - The number of occurrences of 0 in arr is exactly zero.
    - The number of occurrences of 1 in arr is exactly one.
    - Each subarray of arr with a size greater than limit must contain both 0 and 1.
Return the total number of stable binary arrays.
Since the answer may be very large, return it modulo 109 + 7.

Example 1:
    Input: zero = 1, one = 1, limit = 2
    Output: 2
    Explanation:
    The two possible stable binary arrays are [1,0] and [0,1], as both arrays have a single 0 and a single 1, and no subarray has a length greater than 2.
Example 2:
    Input: zero = 1, one = 2, limit = 1
    Output: 1
    Explanation:
    The only possible stable binary array is [1,0,1].
    Note that the binary arrays [1,1,0] and [0,1,1] have subarrays of length 2 with identical elements, hence, they are not stable.
Example 3:
    Input: zero = 3, one = 3, limit = 2
    Output: 14
    Explanation:
    All the possible stable binary arrays are [0,0,1,0,1,1], [0,0,1,1,0,1], [0,1,0,0,1,1], [0,1,0,1,0,1], [0,1,0,1,1,0], [0,1,1,0,0,1], [0,1,1,0,1,0], [1,0,0,1,0,1], [1,0,0,1,1,0], [1,0,1,0,0,1], [1,0,1,0,1,0], [1,0,1,1,0,0], [1,1,0,0,1,0], and [1,1,0,1,0,0].

Constraints:
    1. 1 <= zero, one, limit <= 1000
'''
MOD = 10**9+7
FACTORIALS = [1 for _ in range(1001)]
for i in range(1, 1001):
    FACTORIALS[i] = i * FACTORIALS[i-1] % MOD
    
Inv_FACTORIALS = [pow(x, -1, MOD) for x in FACTORIALS]

def C(n: int, m: int):
    if m < 0:
        return 0
    return (FACTORIALS[n] * Inv_FACTORIALS[m] * Inv_FACTORIALS[n-m]) % MOD

# === 213ms && 16.8MB === #
class Solution:
    
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        ans = 0
        N = zero + one
        min_zero_group = (zero - 1) // limit + 1
        min_one_group = (one - 1) // limit + 1
        
        def count(n, g, k):
            ans = C(n+g-1, g-1)
            r, flag = 1, -1
            while n - r * (k+1) >= 0:
                ans = (ans + flag * C(n - r*(k+1) + g-1, g-1) * C(g, r)) % MOD
                r += 1
                flag *= -1
            return ans
        
        for n in range(min_zero_group, zero+1):
            for m in range(n-1, n+1+1):
                if m < min_one_group or m > one:
                    continue
                flag = 1 if n != m else 2
                ans = (ans + flag * count(zero-n, n, limit - 1) * count(one-m, m, limit - 1)) % MOD
        return ans % MOD
    
# === 72ms && 17.1MB === #
class Solution:
    
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        ans = 0
        N = zero + one
        min_zero_group = (zero - 1) // limit + 1
        min_one_group = (one - 1) // limit + 1
        
        @lru_cache(None)
        def count(n, g, k):
            ans = C(n+g-1, g-1)
            r, flag = 1, -1
            while n - r * (k+1) >= 0:
                ans = (ans + flag * C(n - r*(k+1) + g-1, g-1) * C(g, r)) % MOD
                r += 1
                flag *= -1
            return ans
        
        for n in range(min_zero_group, zero+1):
            for m in range(n-1, n+1+1):
                if m < min_one_group or m > one:
                    continue
                flag = 1 if n != m else 2
                ans = (ans + flag * count(zero-n, n, limit - 1) * count(one-m, m, limit - 1)) % MOD
        return ans % MOD

# === 94ms && 16.7MB === #
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        if zero > one:
            zero, one = one, zero
        m = zero + 1
        f = [0] * (m + 1)
        for i in range((zero - 1) // limit + 1, zero + 1):
            f[i] = C(zero - 1, i - 1)
            for j in range(1, min(i, (zero - i) // limit) + 1):
                f[i] = (f[i] + (1 - j % 2 * 2) * C(i, j) * C(zero - j * limit - 1, i - 1)) % MOD

        ans = 0
        for i in range((one - 1) // limit + 1, min(one, m) + 1):
            s = C(one - 1, i - 1)
            for j in range(1, min(i, (one - i) // limit) + 1):
                s = (s + (1 - j % 2 * 2) * C(i, j) * C(one - j * limit - 1, i - 1)) % MOD
            ans = (ans + s * (f[i - 1] + (f[i] * 2 if i <= zero else 0) + (f[i + 1] if i < zero else 0))) % MOD
        return ans