'''
=== 1585. Check If String Is Transformable With Substring Sort Operations ===

Given two strings s and t, you want to transform string s into string t using the following operation any number of times:
    - Choose a non-empty substring in s and sort it in-place so the characters are in ascending order.
For example, applying the operation on the underlined substring in "14234" results in "12344".
Return true if it is possible to transform string s into string t. Otherwise, return false.
A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "84532", t = "34852"
    Output: true
    Explanation: You can transform s into t using the following sort operations:
    "84532" (from index 2 to 3) -> "84352"
    "84352" (from index 0 to 2) -> "34852"
Example 2:
    Input: s = "34521", t = "23415"
    Output: true
    Explanation: You can transform s into t using the following sort operations:
    "34521" -> "23451"
    "23451" -> "23415"
Example 3:
    Input: s = "12345", t = "12435"
    Output: false
    Example 4:
    Input: s = "1", t = "2"
    Output: false
 
Constraints:
    1. s.length == t.length
    2. 1 <= s.length <= 105
    3. s and t only contain digits from '0' to '9'.
'''
# === 3332ms && 104.1MB === #
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        n = len(t)
        scounter = [{c: 0 for c in "0123456789"} for _ in range(n+1)]
        tcounter = [{c: 0 for c in "0123456789"} for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for c in "0123456789":
                scounter[i][c] = scounter[i+1][c]
                tcounter[i][c] = tcounter[i+1][c]
            scounter[i][s[i]] += 1
            tcounter[i][t[i]] += 1
        
        if not all(scounter[0][c] == tcounter[0][c] for c in "0123456789"):
            return False
        
        scounter_v2 = {c: [] for c in "0123456789"}
        for i in range(n):
            scounter_v2[s[i]].append(i+1)
        tcounter_v2 = {c: [] for c in "0123456789"}
        for i in range(n):
            tcounter_v2[t[i]].append(i+1)
            
        for c in "123456789":
            for idx1, idx2 in zip(scounter_v2[c], tcounter_v2[c]):
                if not all(scounter[idx1][str(k)] >= tcounter[idx2][str(k)] for k in range(int(c))):
                    return False
        return True
                
            
        