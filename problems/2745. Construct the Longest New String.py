'''
=== 2745. Construct the Longest New String ===

You are given three integers x, y, and z.
You have x strings equal to "AA", y strings equal to "BB", and z strings equal to "AB". You want to choose some (possibly all or none) of these strings and concactenate them in some order to form a new string. This new string must not contain "AAA" or "BBB" as a substring.
Return the maximum possible length of the new string.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
    Input: x = 2, y = 5, z = 1
    Output: 12
    Explanation: We can concactenate the strings "BB", "AA", "BB", "AA", "BB", and "AB" in that order. Then, our new string is "BBAABBAABBAB". 
    That string has length 12, and we can show that it is impossible to construct a string of longer length.
Example 2:
    Input: x = 3, y = 2, z = 2
    Output: 14
    Explanation: We can concactenate the strings "AB", "AB", "AA", "BB", "AA", "BB", and "AA" in that order. Then, our new string is "ABABAABBAABBAA". 
    That string has length 14, and we can show that it is impossible to construct a string of longer length.
 
Constraints:
    1. 1 <= x, y, z <= 50
'''
# === 3134ms && 166.6MB === #
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        
        @lru_cache(None)
        def dfs(x, y, z, pre):
            res = 0
            if pre == "AA":
                if y > 0:
                    res = max(res, 2 + dfs(x, y-1, z, "BB"))
            elif pre == "BB" or pre == "AB":
                if x > 0:
                    res = max(res, 2 + dfs(x-1, y, z, "AA"))
                if z > 0:
                    res = max(res, 2 + dfs(x, y, z-1, "AB"))
            else:
                if x > 0:
                    res = max(res, 2 + dfs(x-1, y, z, "AA"))
                if y > 0:
                    res = max(res, 2 + dfs(x, y-1, z, "BB"))
                if z > 0:
                    res = max(res, 2 + dfs(x, y, z-1, "AB"))
            return res
        
        return dfs(x, y, z, "")
    
# === 56ms === #
class Solution:
    def longestBeautifulString(self, x: int, y: int, z: int) -> int:
        return (z + min(x, y+1) + min(x+1, y)) * 2