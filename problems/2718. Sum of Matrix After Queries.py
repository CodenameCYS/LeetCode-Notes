'''
=== 2718. Sum of Matrix After Queries ===

You are given an integer n and a 0-indexed 2D array queries where queries[i] = [typei, indexi, vali].
Initially, there is a 0-indexed n x n matrix filled with 0's. For each query, you must apply one of the following changes:
    - if typei == 0, set the values in the row with indexi to vali, overwriting any previous values.
    - if typei == 1, set the values in the column with indexi to vali, overwriting any previous values.
Return the sum of integers in the matrix after all queries are applied.

Example 1:
    Input: n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
    Output: 23
    Explanation: The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 23. 
Example 2:
    Input: n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
    Output: 17
    Explanation: The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 17.
 
Constraints:
    1. 1 <= n <= 104
    2. 1 <= queries.length <= 5 * 104
    3. queries[i].length == 3
    4. 0 <= typei <= 1
    5. 0 <= indexi < n
    6. 0 <= vali <= 105
'''
# === 1979ms && 39.4MB === #
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        cols, rows = n, n
        seen_cols, seen_rows = set(), set()
        res = 0
        for _type, idx, val in queries[::-1]:
            if _type == 0:
                if idx in seen_rows:
                    continue
                seen_rows.add(idx)
                res += val * cols
                rows -= 1
            else:
                if idx in seen_cols:
                    continue
                seen_cols.add(idx)
                res += val * rows
                cols -= 1
        return res