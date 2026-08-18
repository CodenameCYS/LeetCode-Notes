from typing import List


"""
解题思路：线段树 + 区间信息合并

题目要求每次修改一个字符后，求整个字符串中最长的连续相同字符段。
如果每次修改后重新扫描字符串，单次查询需要 O(n)，最多 10^5 次查询会超时。

一次修改只会影响包含该位置的区间，因此可以用线段树维护答案。对于线段树的
每个节点（即一段连续区间），维护以下信息：

1. length：区间长度。
2. left_char / right_char：区间最左端和最右端的字符。
3. prefix：从区间左端开始的最长相同字符前缀长度。
4. suffix：到区间右端结束的最长相同字符后缀长度。
5. longest：区间内部最长的连续相同字符段长度。

如何合并左右子区间：

- 父区间的初始 longest 是两个子区间 longest 的较大值。
- 如果左区间的右端字符 != 右区间的左端字符，连续段无法跨过中点，合并结束。
- 如果两个边界字符相同，跨中点连续段的长度为：

            左区间 suffix + 右区间 prefix

    用它更新父区间的 longest。
- 只有当左区间整体是同一个字符，即 prefix[left] == length[left] 时，父区间的
    prefix 才能继续延伸到右区间。父区间的 suffix 同理。

每次修改只需要更新一个叶子节点，然后沿着它到根节点的路径重新合并。根节点
longest[1] 始终是整个字符串的答案。

复杂度：建树 O(n)，每次修改 O(log n)，总复杂度 O(n + k log n)，空间 O(n)。
"""


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        n = len(s)
        size = 1
        while size < n:
            size *= 2

        tree_size = size * 2
        length = [0] * tree_size
        prefix = [0] * tree_size
        suffix = [0] * tree_size
        longest = [0] * tree_size
        left_char = [""] * tree_size
        right_char = [""] * tree_size

        def pull(node: int) -> None:
            """使用两个子节点的信息，重新计算当前节点。"""
            left = node * 2
            right = left + 1

            # size 是不小于 n 的 2 的幂，因此末尾可能存在空的补位叶子。
            if length[left] == 0:
                length[node] = length[right]
                prefix[node] = prefix[right]
                suffix[node] = suffix[right]
                longest[node] = longest[right]
                left_char[node] = left_char[right]
                right_char[node] = right_char[right]
                return
            if length[right] == 0:
                length[node] = length[left]
                prefix[node] = prefix[left]
                suffix[node] = suffix[left]
                longest[node] = longest[left]
                left_char[node] = left_char[left]
                right_char[node] = right_char[left]
                return

            length[node] = length[left] + length[right]
            left_char[node] = left_char[left]
            right_char[node] = right_char[right]
            prefix[node] = prefix[left]
            suffix[node] = suffix[right]
            longest[node] = max(longest[left], longest[right])

            # 边界字符不同，不会产生跨越左右区间的新连续段。
            if right_char[left] != left_char[right]:
                return

            # 边界字符相同，左右两段可以在中点处连接。
            longest[node] = max(longest[node], suffix[left] + prefix[right])

            # 左区间整体同字符时，父区间前缀才能延伸进右区间。
            if prefix[left] == length[left]:
                prefix[node] += prefix[right]
            # 右区间整体同字符时，父区间后缀才能延伸进左区间。
            if suffix[right] == length[right]:
                suffix[node] += suffix[left]

        # 字符串中的每个字符对应一个有效叶子，节点信息均为 1。
        for index, char in enumerate(s):
            node = size + index
            length[node] = prefix[node] = suffix[node] = longest[node] = 1
            left_char[node] = right_char[node] = char

        # 自底向上合并，完成初始建树。
        for node in range(size - 1, 0, -1):
            pull(node)

        def update(index: int, char: str) -> int:
            """修改一个叶子，并沿父节点链更新到根节点。"""
            node = size + index
            left_char[node] = right_char[node] = char
            node //= 2
            while node:
                pull(node)
                node //= 2
            return longest[1]

        return [
            update(index, char)
            for index, char in zip(queryIndices, queryCharacters)
        ]