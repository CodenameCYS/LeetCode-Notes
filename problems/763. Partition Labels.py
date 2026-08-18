'''
=== 763. Partition Labels ===

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
    Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:
    1. S will have length in range [1, 500].
    2. S will consist of lowercase letters ('a' to 'z') only.
'''
# === 36ms(73.51%) && 12.7MB(100%) === #
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        loc = {}
        for i,c in enumerate(S):
            if c not in loc.keys():
                loc[c] = [i,i]
            else:
                loc[c][1] = i
        loc = sorted(loc.values())
        st = 0; ed = 0
        ans = []
        for interval in loc:
            if interval[0] > ed:
                ans.append(ed-st+1)
                st, ed = interval
            else:
                ed = max(ed, interval[1])
        ans.append(ed-st+1)
        return ans