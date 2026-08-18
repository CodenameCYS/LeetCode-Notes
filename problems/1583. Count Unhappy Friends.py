'''
=== 1583. Count Unhappy Friends ===

You are given a list of preferences for n friends, where n is always even.
For each person i, preferences[i] contains a list of friends sorted in the order of preference. In other words, a friend earlier in the list is more preferred than a friend later in the list. Friends in each list are denoted by integers from 0 to n-1.
All the friends are divided into pairs. The pairings are given in a list pairs, where pairs[i] = [xi, yi] denotes xi is paired with yi and yi is paired with xi.
However, this pairing may cause some of the friends to be unhappy. A friend x is unhappy if x is paired with y and there exists a friend u who is paired with v but:
    - x prefers u over y, and
    - u prefers x over v.
Return the number of unhappy friends.

Example 1:
    Input: n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]
    Output: 2
    Explanation:
    Friend 1 is unhappy because:
    - 1 is paired with 0 but prefers 3 over 0, and
    - 3 prefers 1 over 2.
    Friend 3 is unhappy because:
    - 3 is paired with 2 but prefers 1 over 2, and
    - 1 prefers 3 over 0.
    Friends 0 and 2 are happy.
Example 2:
    Input: n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
    Output: 0
    Explanation: Both friends 0 and 1 are happy.
Example 3:
    Input: n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
    Output: 4
 
Constraints:
    1. 2 <= n <= 500
    2. n is even.
    3. preferences.length == n
    4. preferences[i].length == n - 1
    5. 0 <= preferences[i][j] <= n - 1
    6. preferences[i] does not contain i.
    7. All values in preferences[i] are unique.
    8. pairs.length == n/2
    9. pairs[i].length == 2
    10. xi != yi
    11. 0 <= xi, yi <= n - 1
    12. Each person is contained in exactly one pair.
'''
# === 472ms && 27.1MB === #
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        n = len(pairs)
        ans = 0
        for i in range(n):
            x, y = pairs[i]
            xh = True
            yh = True
            for j in range(n):
                if i == j:
                    continue
                u, v = pairs[j]
                if preferences[x].index(u) < preferences[x].index(y) and preferences[u].index(x) < preferences[u].index(v):
                    xh = False
                    break
                if preferences[x].index(v) < preferences[x].index(y) and preferences[v].index(x) < preferences[v].index(u):
                    xh = False
                    break
            for j in range(n):
                if i == j:
                    continue
                u, v = pairs[j]
                if preferences[y].index(u) < preferences[y].index(x) and preferences[u].index(y) < preferences[u].index(v):
                    yh = False
                    break
                if preferences[y].index(v) < preferences[y].index(x) and preferences[v].index(y) < preferences[v].index(u):
                    yh = False
                    break
            if not xh: 
                ans += 1
            if not yh: 
                ans += 1
        return ans