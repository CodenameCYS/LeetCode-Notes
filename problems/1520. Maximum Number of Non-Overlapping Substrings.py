'''
=== 1520. Maximum Number of Non-Overlapping Substrings ===

Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:
    - The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
    - A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.
Notice that you can return the substrings in any order.

Example 1:
    Input: s = "adefaddaccc"
    Output: ["e","f","ccc"]
    Explanation: The following are all the possible substrings that meet the conditions:
    [
    "adefaddaccc"
    "adefadda",
    "ef",
    "e",
    "f",
    "ccc",
    ]
    If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
Example 2:
    Input: s = "abbaccd"
    Output: ["d","bb","cc"]
    Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.
 
Constraints:
    1. 1 <= s.length <= 105
    2. s contains only lowercase English letters.
'''
# === 464ms && 33.58MB === #
class SegmentTree:
    def __init__(self, arr):
        self.length = len(arr)
        self.tree = self.build(arr)

    def feature_func(self, *args):
        ans = 0
        for arg in args:
            ans = ans | arg
        return ans

    def build(self, arr):
        n = len(arr)
        tree = [0 for _ in range(2*n)]
        for i in range(n):
            tree[i+n] = arr[i]
        for i in range(n-1, 0, -1):
            tree[i] = self.feature_func(tree[2*i], tree[2*i+1])
        return tree

    def update(self, idx, val):
        idx = idx + self.length
        self.tree[idx] = val
        while idx > 1:
            self.tree[idx // 2] = self.feature_func(self.tree[idx], self.tree[idx ^ 1])
            idx = idx // 2
        return

    def query(self, lb, rb):
        lb += self.length 
        rb += self.length
        nodes = []
        while lb < rb:
            if lb % 2 == 1:
                nodes.append(self.tree[lb])
                lb += 1
            if rb % 2 == 0:
                nodes.append(self.tree[rb])
                rb -= 1
            lb = lb // 2
            rb = rb // 2
        if lb == rb:
            nodes.append(self.tree[rb])
        return self.feature_func(*nodes)

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        locs = {}
        for i, ch in enumerate(s):
            if ch in locs:
                locs[ch][1] = i
            else:
                locs[ch] = [i, i]
        
        arr = [1<<(ord(ch)-ord('a')) for ch in s]
        segment_tree = SegmentTree(arr)
        valid = []
        for ch in locs.keys():
            status = 1 << (ord(ch) - ord('a'))
            st, ed = locs[ch]
            covered = segment_tree.query(st, ed)
            while covered != status:
                for i in range(26):
                    if covered & (1<<i) == 0:
                        continue
                    _ch = chr(ord('a') + i)
                    st = min(st, locs[_ch][0])
                    ed = max(ed, locs[_ch][1])
                    status = status | (1<<i)
                covered = segment_tree.query(st, ed)
            valid.append((st, ed))
        valid = sorted(valid)
        
        n = len(valid)
        @cache
        def dp(idx):
            if idx >= n:
                return []
            st, ed = valid[idx]
            nxt = bisect.bisect_left(valid, (ed+1, ed+1))
            ans1 = dp(idx+1)
            ans2 = [s[st:ed+1]] + dp(nxt)
            if len(ans1) > len(ans2):
                return ans1
            elif len(ans1) < len(ans2):
                return ans2
            elif len(ans1) == 0:
                return []
            else:
                return ans1 if sum(len(x) for x in ans1) < sum(len(x) for x in ans2) else ans2

        return dp(0)