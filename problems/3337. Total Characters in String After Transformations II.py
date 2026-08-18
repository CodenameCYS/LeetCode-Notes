'''
=== 3337. Total Characters in String After Transformations II ===

You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:
    - Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
    - The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
Return the length of the resulting string after exactly t transformations.
Since the answer may be very large, return it modulo 109 + 7.

Example 1:
    Input: s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
    Output: 7
    Explanation:
    First Transformation (t = 1):
        'a' becomes 'b' as nums[0] == 1
        'b' becomes 'c' as nums[1] == 1
        'c' becomes 'd' as nums[2] == 1
        'y' becomes 'z' as nums[24] == 1
        'y' becomes 'z' as nums[24] == 1
        String after the first transformation: "bcdzz"
    Second Transformation (t = 2):
        'b' becomes 'c' as nums[1] == 1
        'c' becomes 'd' as nums[2] == 1
        'd' becomes 'e' as nums[3] == 1
        'z' becomes 'ab' as nums[25] == 2
        'z' becomes 'ab' as nums[25] == 2
        String after the second transformation: "cdeabab"
    Final Length of the string: The string is "cdeabab", which has 7 characters.
Example 2:
    Input: s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    Output: 8
    Explanation:
    First Transformation (t = 1):
        'a' becomes 'bc' as nums[0] == 2
        'z' becomes 'ab' as nums[25] == 2
        'b' becomes 'cd' as nums[1] == 2
        'k' becomes 'lm' as nums[10] == 2
        String after the first transformation: "bcabcdlm"
    Final Length of the string: The string is "bcabcdlm", which has 8 characters.

Constraints:
    1. 1 <= s.length <= 105
    2. s consists only of lowercase English letters.
    3. 1 <= t <= 109
    4. nums.length == 26
    5. 1 <= nums[i] <= 25
'''
MOD = 10**9+7
# === 3719ms && 25.3MB === #
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        
        def mat_mul(A, B):
            assert(len(A[0]) == len(B))
            n, m, l = len(A), len(A[0]), len(B[0])
            out = [[0 for _ in range(l)] for _ in range(n)]
            for i in range(n):
                for j in range(l):
                    for k in range(m):
                        out[i][j] = (out[i][j] + A[i][k] * B[k][j]) % MOD
            return out
        
        # @lru_cache(None)
        # def mat_pow(A, n):
        #     assert(len(A) == len(A[0]))
        #     if n == 1:
        #         return A
        #     return mat_mul(mat_pow(A, n//2), mat_pow(A, n-n//2))
        
        
        # transformation matrics
        mat = [[0 for _ in range(26)] for _ in range(26)]
        for i, j in enumerate(nums):
            for k in range(1, j+1):
                mat[i][(i+k) % 26] = 1
                
        @lru_cache(None)
        def mat_pow(n):
            if n == 1:
                return mat
            return mat_mul(mat_pow(n//2), mat_pow(n-n//2))
                
        mat = mat_pow(t)
        
        # count array
        cnt = [0 for _ in range(26)]
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
            
        out = [0 for _ in range(26)]
        for j in range(26):
            for i in range(26):
                out[j] = (out[j] + cnt[i] * mat[i][j]) % MOD
        return sum(out) % MOD
        
        
        
        