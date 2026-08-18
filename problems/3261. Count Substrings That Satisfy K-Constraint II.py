'''
=== 3261. Count Substrings That Satisfy K-Constraint II ===

You are given a binary string s and an integer k.
You are also given a 2D integer array queries, where queries[i] = [li, ri].
A binary string satisfies the k-constraint if either of the following conditions holds:
    - The number of 0's in the string is at most k.
    - The number of 1's in the string is at most k.
Return an integer array answer, where answer[i] is the number of substrings of s[li..ri] that satisfy the k-constraint.

Example 1:
    Input: s = "0001111", k = 2, queries = [[0,6]]
    Output: [26]
    Explanation:
    For the query [0, 6], all substrings of s[0..6] = "0001111" satisfy the k-constraint except for the substrings s[0..5] = "000111" and s[0..6] = "0001111".
Example 2:
    Input: s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]]
    Output: [15,9,3]
    Explanation:
    The substrings of s with a length greater than 3 do not satisfy the k-constraint.

Constraints:
    1. 1 <= s.length <= 105
    2. s[i] is either '0' or '1'.
    3. 1 <= k <= s.length
    4. 1 <= queries.length <= 105
    5. queries[i] == [li, ri]
    6. 0 <= li <= ri < s.length
    7. All queries are distinct.
'''
# === 2078ms && 73.4MB === #
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        i, j = 0, 0
        cnt = defaultdict(int)
        boundaries = [0 for _ in range(n)]
        while i < n:
            while j < n:
                if cnt["0"] > k and cnt["1"] > k:
                    break
                cnt[s[j]] += 1
                j += 1
            if cnt["0"] > k and cnt["1"] > k:
                boundaries[i] = j-1
            else:
                boundaries[i] = j
            cnt[s[i]] -= 1
            i += 1
            
        cnt = [b-i for i, b in enumerate(boundaries)]
        cs = list(accumulate(cnt, initial=0))
        # print(boundaries, cnt, cs)
        qs = [(i, l, r) for i, (l, r) in enumerate(queries)]
        qs = sorted(qs, key=lambda x: (x[2], x[1]), reverse=True)
        ans = [0 for _ in qs]
        for idx, l, r in qs:
            i = max(bisect.bisect_right(boundaries, r), l)
            _cnt = cs[i] - cs[l]
            for j in range(i, r+1):
                _cnt += min(boundaries[j], r+1) - j
            ans[idx] = _cnt
        return ans
        
        # def query(l, r):
        #     ans = 0
        #     for i in range(l, r+1):
        #         ans += (min(boundaries[i], r+1) - i)
        #     return ans
        
        # return [query(l, r) for l, r in queries]

# === 1864ms && 72.9MB === #
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        i, j = 0, 0
        cnt = defaultdict(int)
        boundaries = [0 for _ in range(n)]
        while i < n:
            while j < n:
                if cnt["0"] > k and cnt["1"] > k:
                    break
                cnt[s[j]] += 1
                j += 1
            if cnt["0"] > k and cnt["1"] > k:
                boundaries[i] = j-1
            else:
                boundaries[i] = j
            cnt[s[i]] -= 1
            i += 1
            
        cnt = [b-i for i, b in enumerate(boundaries)]
        cs = list(accumulate(cnt, initial=0))
        
        def query(l, r):
            i = max(bisect.bisect_right(boundaries, r), l)
            ans = cs[i] - cs[l]
            for j in range(i, r+1):
                ans += min(boundaries[j], r+1) - j
            return ans
        
        return [query(l, r) for l, r in queries]
# === 1470ms && 72.9MB === #
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        i, j = 0, 0
        cnt = defaultdict(int)
        boundaries = [0 for _ in range(n)]
        while i < n:
            while j < n:
                if cnt["0"] > k and cnt["1"] > k:
                    break
                cnt[s[j]] += 1
                j += 1
            if cnt["0"] > k and cnt["1"] > k:
                boundaries[i] = j-1
            else:
                boundaries[i] = j
            cnt[s[i]] -= 1
            i += 1
            
        cnt = [b-i for i, b in enumerate(boundaries)]
        cs = list(accumulate(cnt, initial=0))
        
        def query(l, r):
            i = max(bisect.bisect_right(boundaries, r), l)
            ans = cs[i] - cs[l] + (r+1) * (r+1-i) - (r+i) * (r+1-i) // 2
            return ans
        
        return [query(l, r) for l, r in queries]