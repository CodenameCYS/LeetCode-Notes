'''
=== 1461. Check If a String Contains All Binary Codes of Size K ===

Given a binary string s and an integer k.
Return True if all binary codes of length k is a substring of s. Otherwise, return False.

Example 1:
    Input: s = "00110110", k = 2
    Output: true
    Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
Example 2:
    Input: s = "00110", k = 2
    Output: true
Example 3:
    Input: s = "0110", k = 1
    Output: true
    Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
Example 4:
    Input: s = "0110", k = 2
    Output: false
    Explanation: The binary code "00" is of length 2 and doesn't exist in the array.
Example 5:
    Input: s = "0000000001011100", k = 4
    Output: false
 
Constraints:
    1. 1 <= s.length <= 5 * 10^5
    2. s consists of 0's and 1's only.
    3. 1 <= k <= 20
'''
# === 312ms && 18.6MB === #
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if k >= n:
            return False
        elif n < 2**k:
            return False
        cache = set()
        for i in range(n-k+1):
            cache.add(s[i:i+k])
        # print(cache)
        return len(cache) == 2**k