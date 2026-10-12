'''
=== 4077. Minimize Inversions in a Prefix Tree ===

You are given an array words of n unique strings containing only lowercase English letters from 'a' to 'j'. You are also given an integer array target containing each index from 0 to n - 1 exactly once.
Build a prefix tree from words:
    - The root represents the empty string "".
    - Each other node represents a different non-empty prefix of a word. The parent of a node is the prefix obtained by removing its last character.
    - The node representing the complete word words[i] is marked with index i. A marked node may also have children.
You may choose the order of the children of each node independently. You cannot change which node is a child's parent.
Traverse the tree starting at the root. When visiting a node, first record its index if it is marked. Then visit its children in the chosen order, completing the traversal of each child before moving to the next. This is a pre-order traversal.
The recorded indices form an array traversal of length n. Let pos[i] be the position of index i in target.
An inversion is a pair of positions (a, b) such that 0 <= a < b < n and pos[traversal[a]] > pos[traversal[b]].
Return the minimum possible number of inversions over all choices of child orderings.

Example 1:
    Input: words = ["bad","bag","fig","fed"], target = [3,1,0,2]
    Output: 2
    Explanation:
    Visit the root's "f" child before its "b" child. Within the "f" branch, visit "fed" before "fig". Within the "b" branch, visit "bag" before "bad".
    This produces traversal = [3,2,1,0]:
    Traversal position	Word index	Word	Position in target
    0	3	"fed"	0
    1	2	"fig"	3
    2	1	"bag"	1
    3	0	"bad"	2
    The positions in target are [0,3,1,2]. The inversions are the pairs of traversal positions (1,2) and (1,3), since 3 > 1 and 3 > 2.
    No child ordering produces fewer than 2 inversions.
Example 2:
    Input: words = ["ab","ac","ba","bc"], target = [0,3,1,2]
    Output: 1
    Explanation:
    Visit the root's "a" child before its "b" child. Within these branches, visit "ab" before "ac", and "bc" before "ba".
    This produces traversal = [0,1,3,2]:
    Traversal position	Word index	Word	Position in target
    0	0	"ab"	0
    1	1	"ac"	2
    2	3	"bc"	1
    3	2	"ba"	3
    The positions in target are [0,2,1,3]. The only inversion is the pair of traversal positions (1,2), since 2 > 1.
    No child ordering produces zero inversions.

Constraints:
    1. 1 <= n == words.length <= 104
    2. 1 <= words[i].length <= 20
    3. words[i] contains only lowercase English letters from 'a' to 'j'​​​​​​​
    4. All words[i] are unique
    5. 0 <= target[i] <= n - 1
    6. target is a permutation of integers from 0 to n - 1
'''
# === 13896ms && 55.93MB === #
class Node:
    def __init__(self):
        self.son = {}
        self.pos = -1

# 计算 a 在 b 左侧时，a 和 b 之间的逆序对个数
# a 和 b 已经升序排序
def calc_inversions(a: list[int], b: list[int]) -> int:
    n, m = len(a), len(b)
    i = j = inv = 0
    while i < n and j < m:
        if a[i] > b[j]:
            # a 的子数组 [i, n-1] 中的数都大于 b[j]
            inv += n - i
            j += 1
        else:
            i += 1
    return inv

class Solution:
    def minInversions(self, words: list[str], target: list[int]) -> int:
        n = len(target)
        pos = [0] * n
        for i, x in enumerate(target):
            pos[x] = i

        # 创建前缀树（字典树）
        root = Node()
        for i, word in enumerate(words):
            cur = root
            for ch in word:
                if ch not in cur.son:
                    cur.son[ch] = Node()
                cur = cur.son[ch]
            cur.pos = pos[i]

        # 返回 node 子树的 pos 列表（已从小到大排序）
        def dfs(node: Node) -> list[int]:
            nonlocal ans
            a = [dfs(son) for son in node.son.values()]

            # 预处理逆序对个数
            inv = [[calc_inversions(p, q) for q in a] for p in a]

            m = len(a)
            u = 1 << m
            f = [inf] * u
            f[0] = 0
            for s, fs in enumerate(f):  # 之前选的下标集合是 s
                # 在 s 的右边添加 j
                for j in range(m):
                    if s >> j & 1:
                        continue
                    sum_inv = fs
                    # 枚举 s 中的下标 i，计算新产生的逆序对个数
                    for i in range(m):
                        if s >> i & 1:
                            sum_inv += inv[i][j]
                    f[s | 1 << j] = min(f[s | 1 << j], sum_inv)
            ans += f[-1]

            res = []
            cur_pos = node.pos
            if cur_pos >= 0:
                res.append(cur_pos)
            for sub in a:
                if cur_pos >= 0:
                    # cur_pos 与子树之间的逆序对个数
                    ans += bisect_left(sub, cur_pos)
                res += sub

            res.sort()
            return res

        ans = 0
        dfs(root)
        return ans