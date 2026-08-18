'''
=== 3479. Fruits Into Baskets III ===

You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.
From left to right, place the fruits according to these rules:
    - Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
    - Each basket can hold only one type of fruit.
    - If a fruit type cannot be placed in any basket, it remains unplaced.
Return the number of fruit types that remain unplaced after all possible allocations are made.

Example 1:
    Input: fruits = [4,2,5], baskets = [3,5,4]
    Output: 1
    Explanation:
    fruits[0] = 4 is placed in baskets[1] = 5.
    fruits[1] = 2 is placed in baskets[0] = 3.
    fruits[2] = 5 cannot be placed in baskets[2] = 4.
    Since one fruit type remains unplaced, we return 1.
Example 2:
    Input: fruits = [3,6,1], baskets = [6,4,7]
    Output: 0
    Explanation:
    fruits[0] = 3 is placed in baskets[0] = 6.
    fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
    fruits[2] = 1 is placed in baskets[1] = 4.
    Since all fruits are successfully placed, we return 0.

Constraints:
    1. n == fruits.length == baskets.length
    2. 1 <= n <= 105
    3. 1 <= fruits[i], baskets[i] <= 109
'''
class SegmentTree:
    def __init__(self, arr):
        self.length = len(arr)
        self.tree = self.build(arr)

    def feature_func(self, *args):
        return min(args)

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

# === 2398ms && 43.9MB === #
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        ordered_baskets = sorted([(cap, idx) for idx, cap in enumerate(baskets)])
        ordered_baskets_capacity = [x[0] for x in ordered_baskets]
        ordered_baskets_index = [x[1] for x in ordered_baskets]
        segment_tree = SegmentTree(ordered_baskets_index)
        
        ans = 0
        for fruit in fruits:
            idx = bisect.bisect_left(ordered_baskets_capacity, fruit)
            if idx >= n:
                ans += 1
                continue
            
            left_most_avaliable = segment_tree.query(idx, n-1)
            if left_most_avaliable >= n:
                ans += 1
                continue
            
            basket = (baskets[left_most_avaliable], left_most_avaliable)
            idx = bisect.bisect_left(ordered_baskets, basket)
            segment_tree.update(idx, n)
        return ans
            