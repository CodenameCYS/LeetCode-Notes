'''
=== 1578. Minimum Deletion Cost to Avoid Repeating Letters ===

Given a string s and an array of integers cost where cost[i] is the cost of deleting the character i in s.
Return the minimum cost of deletions such that there are no two identical letters next to each other.
Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

Example 1:
    Input: s = "abaac", cost = [1,2,3,4,5]
    Output: 3
    Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
Example 2:
    Input: s = "abc", cost = [1,2,3]
    Output: 0
    Explanation: You don't need to delete any character because there are no identical letters next to each other.
Example 3:
    Input: s = "aabaa", cost = [1,2,3,4,1]
    Output: 2
    Explanation: Delete the first and the last character, getting the string ("aba").
 
Constraints:
    1. s.length == cost.length
    2. 1 <= s.length, cost.length <= 10^5
    3. 1 <= cost[i] <= 10^4
    4. s contains only lowercase English letters.
'''
# === 1184ms && 24.2MB === #
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = sum(cost)
        n = len(cost)
        
        last = ''
        ans = 0
        idx = 0
        while idx < n:
            ch = s[idx]
            co = cost[idx]
            if ch != last:
                last = ch
                idx += 1
            else:
                st = idx-1
                while idx < n and s[idx] == last:
                    idx += 1
                ans += sum(cost[st:idx]) - max(cost[st:idx])
        return ans