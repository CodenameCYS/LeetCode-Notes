'''
=== 2983. Palindrome Rearrangement Queries ===

You are given a 0-indexed string s having an even length n.
You are also given a 0-indexed 2D integer array, queries, where queries[i] = [ai, bi, ci, di].
For each query i, you are allowed to perform the following operations:
    - Rearrange the characters within the substring s[ai:bi], where 0 <= ai <= bi < n / 2.
    - Rearrange the characters within the substring s[ci:di], where n / 2 <= ci <= di < n.
For each query, your task is to determine whether it is possible to make s a palindrome by performing the operations.
Each query is answered independently of the others.
Return a 0-indexed array answer, where answer[i] == true if it is possible to make s a palindrome by performing operations specified by the ith query, and false otherwise.
    - A substring is a contiguous sequence of characters within a string.
    - s[x:y] represents the substring consisting of characters from the index x to index y in s, both inclusive.
 
Example 1:
    Input: s = "abcabc", queries = [[1,1,3,5],[0,2,5,5]]
    Output: [true,true]
    Explanation: In this example, there are two queries:
    In the first query:
    - a0 = 1, b0 = 1, c0 = 3, d0 = 5.
    - So, you are allowed to rearrange s[1:1] => abcabc and s[3:5] => abcabc.
    - To make s a palindrome, s[3:5] can be rearranged to become => abccba.
    - Now, s is a palindrome. So, answer[0] = true.
    In the second query:
    - a1 = 0, b1 = 2, c1 = 5, d1 = 5.
    - So, you are allowed to rearrange s[0:2] => abcabc and s[5:5] => abcabc.
    - To make s a palindrome, s[0:2] can be rearranged to become => cbaabc.
    - Now, s is a palindrome. So, answer[1] = true.
Example 2:
    Input: s = "abbcdecbba", queries = [[0,2,7,9]]
    Output: [false]
    Explanation: In this example, there is only one query.
    a0 = 0, b0 = 2, c0 = 7, d0 = 9.
    So, you are allowed to rearrange s[0:2] => abbcdecbba and s[7:9] => abbcdecbba.
    It is not possible to make s a palindrome by rearranging these substrings because s[3:6] is not a palindrome.
    So, answer[0] = false.
Example 3:
    Input: s = "acbcab", queries = [[1,2,4,5]]
    Output: [true]
    Explanation: In this example, there is only one query.
    a0 = 1, b0 = 2, c0 = 4, d0 = 5.
    So, you are allowed to rearrange s[1:2] => acbcab and s[4:5] => acbcab.
    To make s a palindrome s[1:2] can be rearranged to become abccab.
    Then, s[4:5] can be rearranged to become abccba.
    Now, s is a palindrome. So, answer[0] = true.
 
Constraints:
    1. 2 <= n == s.length <= 105
    2. 1 <= queries.length <= 105
    3. queries[i].length == 4
    4. ai == queries[i][0], bi == queries[i][1]
    5. ci == queries[i][2], di == queries[i][3]
    6. 0 <= ai <= bi < n / 2
    7. n / 2 <= ci <= di < n
    8. n is even.
    9. s consists of only lowercase English letters.
'''
class SegmentTree:
    def __init__(self, arr):
        self.length = len(arr)
        self.tree = self.build(arr)

    def feature_func(self, *args):
        return sum(args)

    def build(self, arr):
        n = len(arr)
        tree = [0 for _ in range(2*n)]
        for i in range(n):
            tree[i+n] = arr[i]
        for i in range(n-1, 0, -1):
            tree[i] = self.feature_func(tree[i<<1], tree[(i<<1) | 1])
        return tree

    def update(self, idx, val):
        idx = idx + self.length
        self.tree[idx] = val
        while idx > 1:
            self.tree[idx>>1] = self.feature_func(self.tree[idx], self.tree[idx ^ 1])
            idx = idx>>1
        return

    def query(self, lb, rb):
        lb += self.length 
        rb += self.length
        nodes = []
        while lb < rb:
            if lb & 1 == 1:
                nodes.append(self.tree[lb])
                lb += 1
            if rb & 1 == 0:
                nodes.append(self.tree[rb])
                rb -= 1
            lb = lb >> 1
            rb = rb >> 1
        if lb == rb:
            nodes.append(self.tree[rb])
        return self.feature_func(*nodes)
# === 3424ms && 76.1MB === #
class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        
        n, m = len(s), len(s) // 2
        # print(n, m)
        cnt = [[0 for _ in range(26)] for _ in range(n+1)]
        for i, ch in enumerate(s):
            for j in range(26):
                cnt[i+1][j] = cnt[i][j]
            cnt[i+1][ord(ch) - ord('a')] += 1
        # print(cnt[m], cnt[n])
            
        matched = [1 if s[i] == s[n-1-i] else 0 for i in range(m)]
        segment_tree = SegmentTree(matched)
        
        @lru_cache(None)
        def query_inner(a, b, c, d):
            lb = min(a, n-1-d)
            rb = max(b, n-1-c)
            cnt1 = [cnt[rb+1][i]-cnt[lb][i] for i in range(26)]
            cnt2 = [cnt[n-lb][i]-cnt[n-1-rb][i] for i in range(26)]
            ans = all(x == y for x, y in zip(cnt1, cnt2))
            # print(f"inner: [{a}, {b}], [{c}, {d}] -> real: [{lb}, {rb}] -> {ans}")
            return ans
        
        @lru_cache(None)
        def query_inclusive(a, b, c, d):
            cnt1 = [cnt[b+1][i]-cnt[a][i] for i in range(26)]
            cnt2 = [cnt[d+1][i]-cnt[c][i] for i in range(26)]
            ans = all([x >= y for x, y in zip(cnt1, cnt2)])
            # print(f"inclusive: [{a}, {b}] & [{c}, {d}], ==> {s[a:b+1]} & {s[c:d+1]} -> {ans}")
            return ans
        
        @lru_cache(None)
        def query_outer(a, b):
            if b < a:
                ans = True
            else:
                ans = (b-a+1 == segment_tree.query(a, b))
            # print(f"outer: [{a}, {b}] -> {ans}")
            return ans
        
        @lru_cache(None)
        def query(a, b, c, d):
            a1, b1, c1, d1 = n-1-b, n-1-a, n-1-d, n-1-c
            if b < c1:
                return query_inner(a, b, n-1-a, n-1-b) and query_inner(c1, d1, c, d) and query_outer(0, a-1) and query_outer(b+1, c1-1) and query_outer(d1+1, m-1)
            elif a > d1:
                return query_inner(a, b, n-1-a, n-1-b) and query_inner(c1, d1, c, d) and query_outer(0, c1-1) and query_outer(d1+1, a-1) and query_outer(b+1, m-1)
            elif a <= c1 <= d1 <= b or c1 <= a <= b <= d1:
                return query_inner(a, b, c, d) and query_outer(0, min(a, c1)-1) and query_outer(max(b, d1)+1, m-1)
            elif a <= c1 <= b <= d1:
                return query_inner(a, b, c, d) and query_outer(0, a-1) and query_outer(d1+1, m-1) and query_inclusive(a, b, d+1, b1) and query_inclusive(c, d, b+1, d1)
            else:
                return query_inner(a, b, c, d) and query_outer(0, c1-1) and query_outer(b+1, m-1) and query_inclusive(a, b, a1, c-1) and query_inclusive(c, d, c1, a-1)
        
        ans = [query(a, b, c, d) for a, b, c, d in queries]
        # print("=" * 10)
        return ans