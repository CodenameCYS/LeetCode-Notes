'''
=== 3129. Find All Possible Stable Binary Arrays I ===

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
    1. 1 <= zero, one, limit <= 200
'''
MOD = 10**9+7
FACTORIALS = [1 for _ in range(401)]
for i in range(1, 401):
    FACTORIALS[i] = i * FACTORIALS[i-1] % MOD
    
def rev(x):
    return pow(x, -1, MOD)

def C(n, m):
    if m < 0:
        return 0
    return FACTORIALS[n] * rev(FACTORIALS[m]) * rev(FACTORIALS[n-m]) % MOD

# === 3157ms && 684.4MB === #
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        
        @lru_cache(None)
        def dp(n,m,k):
            if n + k > limit * (m+1) or m > limit * (n+1):
                return 0
            elif n + k <= limit and m <= limit:
                ans = C(n+m, n)
            elif n + k <= limit and m > limit and m <= 2 * limit:
                ans = C(n+m, n) - C(n+m-limit-1, n) * (n+1)
            else:
                ans = dp(m-1, n, 1)
                if k+1 <= limit:
                    ans = (ans + dp(n-1, m, k+1)) % MOD
            return ans % MOD
        
        ans = dp(zero, one, 0)
        # print("=" * 10)
        return ans

# === 3727ms && 756.5MB === #
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        
        @lru_cache(None)
        def dp(n,m,k,p):
            # n -> zero, m -> one, k -> pre count, p -> pre element
            if n + (1-p) * k > limit * (m+1) or m + p * k > limit * (n+1):
                return 0
            elif n + (1-p) * k <= limit and m + p * k <= limit:
                ans = C(n+m, n)
            elif p == 0 and n + k <= limit and m > limit and m <= 2 * limit:
                ans = C(n+m, n) - C(n+m-limit-1, n) * (n+1)
            elif p == 1 and n > limit and m + k <= limit and n <= 2 * limit:
                ans = C(n+m, n) - C(n+m-limit-1, m) * (m+1)
            else:
                ans = 0
                if k*(1-p)+1 <= limit:
                    ans = (ans + dp(n-1, m, k*(1-p)+1, 0)) % MOD
                if k*p+1 <= limit:
                    ans = (ans + dp(m-1, n, k*p+1, 0)) % MOD
            return ans % MOD
        
        ans = dp(zero, one, 0, 0)
        # print("=" * 10)
        return ans

# === 707ms && 32.1MB === #            
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        
        @lru_cache(None)
        def dp(n,m):
            if n == 0:
                return 0
            elif m == 0:
                return 1 if n <= limit else 0
            elif n > limit * (m+1) or m > limit * n:
                return 0
            elif n <= limit and m <= limit:
                ans = C(n+m-1, m)
            elif n <= limit and m > limit and m <= 2 * limit:
                ans = C(n+m-1, m) - C(n+m-limit-2, n-1) * n
            else:
                ans = 0
                for i in range(1, min(limit, n) + 1):
                    ans = (ans + dp(m, n-i))
            return ans % MOD
        
        ans = (dp(zero, one) + dp(one, zero)) % MOD
        # print("=" * 10)
        return ans
            