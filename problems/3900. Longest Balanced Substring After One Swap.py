'''
=== 3900. Longest Balanced Substring After One Swap ===

You are given a binary string s consisting only of characters '0' and '1'.
A string is balanced if it contains an equal number of '0's and '1's.
You can perform at most one swap between any two characters in s. Then, you select a balanced substring from s.
Return an integer representing the maximum length of the balanced substring you can select.

Example 1:
    Input: s = "100001"
    Output: 4
    Explanation:
    Swap "100001". The string becomes "101000".
    Select the substring "101000", which is balanced because it has two '0's and two '1's.
Example 2:
    Input: s = "111"
    Output: 0
    Explanation:
    Choose not to perform any swaps.
    Select the empty substring, which is balanced because it has zero '0's and zero '1's.

Constraints:
    1. 1 <= s.length <= 105
    2. s consists only of the characters '0' and '1'.
'''
# === 1766ms && 46.12MB === # 
class Solution:
    def longestBalanced(self, s: str) -> int:
        cnt = Counter(s)
        if cnt['0'] == 0 or cnt['1'] == 0:
            return 0
        
        n = len(s)
        locs = defaultdict(list)
        locs[0].append(0)
        delta = [0 for _ in range(n+1)]
        for i, ch in enumerate(s):
            if ch == '1':
                delta[i+1] = delta[i] + 1
            else:
                delta[i+1] = delta[i] - 1
            locs[delta[i+1]].append(i+1)

        ans = 0
        for i in range(n):
            if n-i <= ans:
                break
            candi = []
            candi.append(locs[delta[i]][-1] - i)
            if len(locs[delta[i]+2]) > 0 and (locs[delta[i]+2][-1] - i) // 2 - 1 < cnt['0']:
                candi.append(locs[delta[i]+2][-1] - i)
            elif len(locs[delta[i]+2]) > 1 and (locs[delta[i]+2][-2] - i) // 2 - 1 < cnt['0']:
                candi.append(locs[delta[i]+2][-2] - i)
            if len(locs[delta[i]-2]) > 0 and (locs[delta[i]-2][-1] - i) // 2 - 1 < cnt['1']:
                candi.append(locs[delta[i]-2][-1] - i)
            elif len(locs[delta[i]-2]) > 1 and (locs[delta[i]-2][-2] - i) // 2 - 1 < cnt['1']:
                candi.append(locs[delta[i]-2][-2] - i)
            ans = max(ans, max(candi))
        return ans