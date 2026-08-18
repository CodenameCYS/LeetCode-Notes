'''
=== 3343. Count Number of Balanced Permutations ===

You are given a string num. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of the digits at odd indices.
Return the number of distinct permutations of num that are balanced.
Since the answer may be very large, return it modulo 109 + 7.
A permutation is a rearrangement of all the characters of a string.

Example 1:
    Input: num = "123"
    Output: 2
    Explanation:
    The distinct permutations of num are "123", "132", "213", "231", "312" and "321".
    Among them, "132" and "231" are balanced. Thus, the answer is 2.
Example 2:
    Input: num = "112"
    Output: 1
    Explanation:
    The distinct permutations of num are "112", "121", and "211".
    Only "121" is balanced. Thus, the answer is 1.
Example 3:
    Input: num = "12345"
    Output: 0
    Explanation:
    None of the permutations of num are balanced, so the answer is 0.
 
Constraints:
    1. 2 <= num.length <= 80
    2. num consists of digits '0' to '9' only.
'''
MOD = 10**9+7

factorials = [1 for i in range(41)]
for i in range(2, 41):
    factorials[i] = (i * factorials[i-1]) % MOD
    
revs = [1 for i in range(41)]
for i in range(2, 41):
    revs[i] = pow(factorials[i], -1, mod=MOD)
    
@lru_cache(None)
def C(n, i):
    return (factorials[n] * revs[i] * revs[n-i]) % MOD
# === 2195ms && 113.7MB === #
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        
        cnt = Counter(num)
        odd, even = len(num) - len(num)//2, len(num)//2
        
        @lru_cache(None)
        def dp(idx, delta, odd, even):
            if idx == 10:
                return 1 if delta == 0 else 0
            # n, m = (odd-1, even) if idx == 0 else (odd, even)
            n, m = odd, even
            k = cnt[str(idx)]
            ans = 0
            for i in range(k+1):
                if i > n or k-i > m:
                    continue
                ans = (ans + C(n, i) * C(m, k-i) * dp(idx+1, delta + idx * (i*2-k), odd-i, even-k+i)) % MOD
            return ans
        
        return dp(0, 0, odd, even)