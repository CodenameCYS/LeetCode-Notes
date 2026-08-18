'''
=== 3777. Minimum Deletions to Make Alternating Substring ===

You are given a string s of length n consisting only of the characters 'A' and 'B'.
You are also given a 2D integer array queries of length q, where each queries[i] is one of the following:
    - [1, j]: Flip the character at index j of s i.e. 'A' changes to 'B' (and vice versa). This operation mutates s and affects subsequent queries.
    - [2, l, r]: Compute the minimum number of character deletions required to make the substring s[l..r] alternating. This operation does not modify s; the length of s remains n.
A substring is alternating if no two adjacent characters are equal. A substring of length 1 is always alternating.
Return an integer array answer, where answer[i] is the result of the ith query of type [2, l, r].

Example 1:
    Input: s = "ABA", queries = [[2,1,2],[1,1],[2,0,2]]
    Output: [0,2]
    Explanation:
    i	queries[i]	j	l	r	s before query	s[l..r]	Result	Answer
    0	[2, 1, 2]	-	1	2	"ABA"	"BA"	Already alternating	0
    1	[1, 1]	1	-	-	"ABA"	-	Flip s[1] from 'B' to 'A'	-
    2	[2, 0, 2]	-	0	2	"AAA"	"AAA"	Delete any two 'A's to get "A"	2
    Thus, the answer is [0, 2].
Example 2:
    Input: s = "ABB", queries = [[2,0,2],[1,2],[2,0,2]]
    Output: [1,0]
    Explanation:
    i	queries[i]	j	l	r	s before query	s[l..r]	Result	Answer
    0	[2, 0, 2]	-	0	2	"ABB"	"ABB"	Delete one 'B' to get "AB"	1
    1	[1, 2]	2	-	-	"ABB"	-	Flip s[2] from 'B' to 'A'	-
    2	[2, 0, 2]	-	0	2	"ABA"	"ABA"	Already alternating	0
    Thus, the answer is [1, 0].
Example 3:
    Input: s = "BABA", queries = [[2,0,3],[1,1],[2,1,3]]
    Output: [0,1]
    Explanation:
    i	queries[i]	j	l	r	s before query	s[l..r]	Result	Answer
    0	[2, 0, 3]	-	0	3	"BABA"	"BABA"	Already alternating	0
    1	[1, 1]	1	-	-	"BABA"	-	Flip s[1] from 'A' to 'B'	-
    2	[2, 1, 3]	-	1	3	"BBBA"	"BBA"	Delete one 'B' to get "BA"	1
    Thus, the answer is [0, 1].

Constraints:
    1. 1 <= n == s.length <= 105
    2. s[i] is either 'A' or 'B'.
    3. 1 <= q == queries.length <= 105
    4. queries[i].length == 2 or 3
    5. queries[i] == [1, j] or,
    6. queries[i] == [2, l, r]
    7. 0 <= j <= n - 1
    8. 0 <= l <= r <= n - 1
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
# === 3291ms && 62.84MB === #
class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        arr = [0 if ch == "A" else 1 for ch in s]
        status = [0 for _ in arr]
        for i in range(1, n):
            if s[i] == s[i-1]:
                status[i] = 1
        segment_tree = SegmentTree(status)

        def update(idx):
            arr[idx] = 1-arr[idx]
            if idx-1 >= 0:
                segment_tree.update(idx, 1 if arr[idx] == arr[idx-1] else 0)
            if idx+1 < n:
                segment_tree.update(idx+1, 1 if arr[idx] == arr[idx+1] else 0)
            return
        
        def query(l, r):
            return segment_tree.query(l+1, r)
        
        ans = []
        for q in queries:
            if q[0] == 1:
                update(q[1])
            else:
                ans.append(query(q[1], q[2]))
        return ans
        