'''
=== 3569. Maximize Count of Distinct Primes After Split ===

You are given an integer array nums having length n and a 2D integer array queries where queries[i] = [idx, val].
For each query:
    - Update nums[idx] = val.
    - Choose an integer k with 1 <= k < n to split the array into the non-empty prefix nums[0..k-1] and suffix nums[k..n-1] such that the sum of the counts of distinct prime values in each part is maximum.
Note: The changes made to the array in one query persist into the next query.
Return an array containing the result for each query, in the order they are given.

Example 1:
    Input: nums = [2,1,3,1,2], queries = [[1,2],[3,3]]
    Output: [3,4]
    Explanation:
    Initially nums = [2, 1, 3, 1, 2].
    After 1st query, nums = [2, 2, 3, 1, 2]. Split nums into [2] and [2, 3, 1, 2]. [2] consists of 1 distinct prime and [2, 3, 1, 2] consists of 2 distinct primes. Hence, the answer for this query is 1 + 2 = 3.
    After 2nd query, nums = [2, 2, 3, 3, 2]. Split nums into [2, 2, 3] and [3, 2] with an answer of 2 + 2 = 4.
    The output is [3, 4].
Example 2:
    Input: nums = [2,1,4], queries = [[0,1]]
    Output: [0]
    Explanation:
    Initially nums = [2, 1, 4].
    After 1st query, nums = [1, 1, 4]. There are no prime numbers in nums, hence the answer for this query is 0.
    The output is [0].
 
Constraints:
    1. 2 <= n == nums.length <= 5 * 104
    2. 1 <= queries.length <= 5 * 104
    3. 1 <= nums[i] <= 105
    4. 0 <= queries[i][0] < nums.length
    5. 1 <= queries[i][1] <= 105
'''
# === 7026ms && 46.94MB === #
def get_primes(n):
    status = [0 for _ in range(n+1)]
    primes = set()
    for i in range(2, n+1):
        if status[i] != 0:
            continue
        primes.add(i)
        for j in range(i, n+1, i):
            status[j] = 1
    return primes

PRIMES = get_primes(10**5)

class LazySegmentTree:
    def __init__(self, arr):
        """
        根据数组 arr 构建惰性线段树
        :param arr: 输入数组
        """
        self.n = len(arr)
        self.arr = arr
        # 初始化线段树和惰性标记数组（4倍原始数组大小）
        self.size = 4 * self.n
        self.tree = [-float('inf')] * self.size  # 存储区间最大值
        self.lazy = [0] * self.size             # 存储惰性标记
        self._build(0, 0, self.n - 1)           # 从根节点开始建树

    def _build(self, node, start, end):
        """
        递归构建线段树
        :param node: 当前节点索引
        :param start: 当前节点表示的区间起始索引
        :param end: 当前节点表示的区间结束索引
        """
        if start == end:
            # 叶子节点，直接存储数组值
            self.tree[node] = self.arr[start]
            return
        
        mid = (start + end) // 2
        left_node = 2 * node + 1  # 左子节点索引
        right_node = 2 * node + 2  # 右子节点索引
        
        # 递归构建左右子树
        self._build(left_node, start, mid)
        self._build(right_node, mid + 1, end)
        
        # 当前节点值为左右子树的最大值
        self.tree[node] = max(self.tree[left_node], self.tree[right_node])

    def _push_down(self, node, start, end):
        """
        下推惰性标记到子节点
        :param node: 当前节点索引
        :param start: 当前节点表示的区间起始索引
        :param end: 当前节点表示的区间结束索引
        """
        if self.lazy[node] != 0:
            # 更新当前节点的值
            self.tree[node] += self.lazy[node]
            
            if start != end:  # 非叶子节点，标记下推
                left_node = 2 * node + 1
                right_node = 2 * node + 2
                # 将惰性标记添加到子节点
                self.lazy[left_node] += self.lazy[node]
                self.lazy[right_node] += self.lazy[node]
            
            # 清除当前节点的惰性标记
            self.lazy[node] = 0

    def update(self, l, r, val):
        """
        将闭区间 [l, r] 内的所有元素增加 val
        :param l: 区间左边界
        :param r: 区间右边界
        :param val: 要增加的值
        """
        self._update(0, 0, self.n - 1, l, r, val)

    def _update(self, node, start, end, l, r, val):
        """
        递归执行区间更新
        :param node: 当前节点索引
        :param start: 当前节点表示的区间起始索引
        :param end: 当前节点表示的区间结束索引
        :param l: 更新区间左边界
        :param r: 更新区间右边界
        :param val: 要增加的值
        """
        # 先下推当前节点的惰性标记
        self._push_down(node, start, end)
        
        # 当前节点区间与更新区间无交集
        if start > r or end < l:
            return
        
        # 当前节点区间完全包含在更新区间内
        if l <= start and end <= r:
            # 更新当前节点值
            self.tree[node] += val
            if start != end:  # 非叶子节点，更新子节点惰性标记
                left_node = 2 * node + 1
                right_node = 2 * node + 2
                self.lazy[left_node] += val
                self.lazy[right_node] += val
            return
        
        # 部分重叠，递归更新子区间
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        
        self._update(left_node, start, mid, l, r, val)
        self._update(right_node, mid + 1, end, l, r, val)
        
        # 更新当前节点值为左右子树的最大值
        self.tree[node] = max(self.tree[left_node], self.tree[right_node])

    def query(self, l, r):
        """
        查询闭区间 [l, r] 内的最大元素值
        :param l: 查询区间左边界
        :param r: 查询区间右边界
        :return: 区间内的最大值
        """
        return self._query(0, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        """
        递归执行区间查询
        :param node: 当前节点索引
        :param start: 当前节点表示的区间起始索引
        :param end: 当前节点表示的区间结束索引
        :param l: 查询区间左边界
        :param r: 查询区间右边界
        :return: 区间内的最大值
        """
        # 先下推当前节点的惰性标记
        self._push_down(node, start, end)
        
        # 当前节点区间与查询区间无交集
        if start > r or end < l:
            return -float('inf')
        
        # 当前节点区间完全包含在查询区间内
        if l <= start and end <= r:
            return self.tree[node]
        
        # 部分重叠，递归查询子区间
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        
        left_max = self._query(left_node, start, mid, l, r)
        right_max = self._query(right_node, mid + 1, end, l, r)
        
        return max(left_max, right_max)


class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        primes_locs = defaultdict(list)
        for i, x in enumerate(nums):
            if x in PRIMES:
                primes_locs[x].append(i)

        n = len(nums)
        segment_tree = LazySegmentTree([0 for _ in range(n)])
        for p, locs in primes_locs.items():
            if len(locs) > 1:
                segment_tree.update(locs[0], locs[-1], 1)

        def query(idx, val):
            nonlocal primes_locs, segment_tree, nums
            # print("=" * 5)
            # print(primes_locs, segment_tree.query(0, n-1))
            old_val = nums[idx]
            nums[idx] = val
            if old_val == val:
                return len(primes_locs) + segment_tree.query(0, n-1)
            if old_val in PRIMES:
                l, r = primes_locs[old_val][0], primes_locs[old_val][-1]
                primes_locs[old_val].pop(bisect.bisect_left(primes_locs[old_val], idx))
                if l == r:
                    primes_locs.pop(old_val)
                    pass
                elif len(primes_locs[old_val]) == 1:
                    segment_tree.update(l, r, -1)
                elif l == idx:
                    new_l = primes_locs[old_val][0]
                    segment_tree.update(idx, new_l-1, -1)
                elif r == idx:
                    new_r = primes_locs[old_val][-1]
                    segment_tree.update(new_r+1, idx, -1)
            if val in PRIMES:
                if val not in primes_locs:
                    primes_locs[val] = [idx]
                else:
                    l, r = primes_locs[val][0], primes_locs[val][-1]
                    bisect.insort(primes_locs[val], idx)
                    if len(primes_locs[val]) == 2:
                        l, r = primes_locs[val][0], primes_locs[val][-1]
                        segment_tree.update(l, r, 1)
                    elif idx < l:
                        segment_tree.update(idx, l-1, 1)
                    elif idx > r:
                        segment_tree.update(r+1, idx, 1)
            # print(primes_locs, segment_tree.query(0, n-1))
            return len(primes_locs) + segment_tree.query(0, n-1)

        return [query(idx, val) for idx, val in queries]




