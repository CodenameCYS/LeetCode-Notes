'''
=== 886. Possible Bipartition ===

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
Each person may dislike some other people, and they should not go into the same group. 
Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
Return true if and only if it is possible to split everyone into two groups in this way.

Example 1:
    Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
    Output: true
    Explanation: group1 [1,4], group2 [2,3]
Example 2:
    Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
    Output: false
Example 3:
    Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    Output: false
 
Constraints:
    1. 1 <= N <= 2000
    2. 0 <= dislikes.length <= 10000
    3. dislikes[i].length == 2
    4. 1 <= dislikes[i][j] <= N
    5. dislikes[i][0] < dislikes[i][1]
    6. There does not exist i != j for which dislikes[i] == dislikes[j].
'''
# === 1172ms(14.67%) && 18.4MB(98.31%) === #
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        cache = {}
        for a, b in dislikes:
            cache[a] = cache.get(a, []) + [b]
            cache[b] = cache.get(b, []) + [a]
        if len(cache) == 0:
            return True
        groups = [set(), set()]
        have_seen = set()
        while len(have_seen) != N:
            for i in range(1, N+1):
                if i not in have_seen:
                    q = [set([i]), set()]
            while len(q[0]) != 0:
                our_group, their_group = groups
                queue, next_queue = q
                for p in queue:
                    if p in their_group:
                        return False
                    our_group.add(p)
                    have_seen.add(p)
                    for np in cache.get(p, []):
                        if np not in their_group:
                            next_queue.add(np)
                q = [next_queue, set()]
                groups = [their_group, our_group]
                # print(q)
                # print(groups)
        return True