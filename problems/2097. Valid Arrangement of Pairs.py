'''
=== 2097. Valid Arrangement of Pairs ===

You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. An arrangement of pairs is valid if for every index i where 1 <= i < pairs.length, we have endi-1 == starti.
Return any valid arrangement of pairs.
Note: The inputs will be generated such that there exists a valid arrangement of pairs.

Example 1:
    Input: pairs = [[5,1],[4,5],[11,9],[9,4]]
    Output: [[11,9],[9,4],[4,5],[5,1]]
    Explanation:
    This is a valid arrangement since endi-1 always equals starti.
    end0 = 9 == 9 = start1 
    end1 = 4 == 4 = start2
    end2 = 5 == 5 = start3
Example 2:
    Input: pairs = [[1,3],[3,2],[2,1]]
    Output: [[1,3],[3,2],[2,1]]
    Explanation:
    This is a valid arrangement since endi-1 always equals starti.
    end0 = 3 == 3 = start1
    end1 = 2 == 2 = start2
    The arrangements [[2,1],[1,3],[3,2]] and [[3,2],[2,1],[1,3]] are also valid.
Example 3:
    Input: pairs = [[1,2],[1,3],[2,1]]
    Output: [[1,2],[2,1],[1,3]]
    Explanation:
    This is a valid arrangement since endi-1 always equals starti.
    end0 = 2 == 2 = start1
    end1 = 1 == 1 = start2
 
Constraints:
    1. 1 <= pairs.length <= 105
    2. pairs[i].length == 2
    3. 0 <= starti, endi <= 109
    4. starti != endi
    5. No two pairs are exactly the same.
    6. There exists a valid arrangement of pairs.
'''
# === 3080ms && 179.3MB === #
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        deg = defaultdict(int)
        out = defaultdict(list)
        for u, v in pairs:
            deg[u] += 1
            deg[v] -= 1
            out[u].append(v)
            
        _, src = max((d, u) for u, d in deg.items())
        res = []
        
        def dfs(u):
            nonlocal res, out
            while out[u]:
                v = out[u].pop(0)
                dfs(v)
            res.append(u)
            
        dfs(src)
        n = len(res)
        res = res[::-1]
        return [[res[i], res[i+1]] for i in range(n-1)]
            