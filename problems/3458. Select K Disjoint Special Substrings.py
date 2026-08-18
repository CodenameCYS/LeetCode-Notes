'''
=== 3458. Select K Disjoint Special Substrings ===

Given a string s of length n and an integer k, determine whether it is possible to select k disjoint special substrings.
A special substring is a substring where:
    - Any character present inside the substring should not appear outside it in the string.
    - The substring is not the entire string s.
Note that all k substrings must be disjoint, meaning they cannot overlap.
Return true if it is possible to select k such disjoint special substrings; otherwise, return false.
A substring is a contiguous non-empty sequence of characters within a string.
 
Example 1:
    Input: s = "abcdbaefab", k = 2
    Output: true
    Explanation:
    We can select two disjoint special substrings: "cd" and "ef".
    "cd" contains the characters 'c' and 'd', which do not appear elsewhere in s.
    "ef" contains the characters 'e' and 'f', which do not appear elsewhere in s.
Example 2:
    Input: s = "cdefdc", k = 3
    Output: false
    Explanation:
    There can be at most 2 disjoint special substrings: "e" and "f". Since k = 3, the output is false.
Example 3:
    Input: s = "abeabe", k = 0
    Output: true

Constraints:
    1. 2 <= n == s.length <= 5 * 104
    2. 0 <= k <= 26
    3. s consists only of lowercase English letters.
'''
# === 70ms && 27.6MB === #
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        locs = defaultdict(list)
        for i, ch in enumerate(s):
            locs[ch].append(i)
            
        starts = sorted([(indexes[0], ch) for ch, indexes in locs.items()])
        n = len(starts)
        
        @lru_cache(None)
        def dp(idx):
            if idx >= n:
                return 0
            
            st, ch = starts[idx]
            seen = {ch}
            ed, nxt = locs[ch][-1], idx
            for _st, ch in starts[idx:]:
                if _st > ed:
                    break
                ed = max(ed, locs[ch][-1])
                seen.add(ch)
                nxt += 1
                
            is_allowed = not (st == 0 and ed == len(s)-1)
            for ch, indexes in locs.items():
                if ch in seen:
                    continue
                i = bisect.bisect_left(indexes, st)
                if i < len(indexes) and indexes[i] < ed:
                    is_allowed = False
                    break
            
            # print(f"idx={idx}, nxt={nxt}, is_allowed={is_allowed}, st={st}, ed={ed}, seen={seen}")
            if is_allowed:
                return max(dp(idx+1), 1 + dp(nxt))
            else:
                return dp(idx+1)
        
        return dp(0) >= k
            