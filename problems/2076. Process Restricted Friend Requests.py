'''
=== 2076. Process Restricted Friend Requests ===

You are given an integer n indicating the number of people in a network. Each person is labeled from 0 to n - 1.
You are also given a 0-indexed 2D integer array restrictions, where restrictions[i] = [xi, yi] means that person xi and person yi cannot become friends, either directly or indirectly through other people.
Initially, no one is friends with each other. You are given a list of friend requests as a 0-indexed 2D integer array requests, where requests[j] = [uj, vj] is a friend request between person uj and person vj.
A friend request is successful if uj and vj can be friends. Each friend request is processed in the given order (i.e., requests[j] occurs before requests[j + 1]), and upon a successful request, uj and vj become direct friends for all future friend requests.
Return a boolean array result, where each result[j] is true if the jth friend request is successful or false if it is not.
Note: If uj and vj are already direct friends, the request is still successful.

Example 1:
    Input: n = 3, restrictions = [[0,1]], requests = [[0,2],[2,1]]
    Output: [true,false]
    Explanation:
    Request 0: Person 0 and person 2 can be friends, so they become direct friends. 
    Request 1: Person 2 and person 1 cannot be friends since person 0 and person 1 would be indirect friends (1--2--0).
Example 2:
    Input: n = 3, restrictions = [[0,1]], requests = [[1,2],[0,2]]
    Output: [true,false]
    Explanation:
    Request 0: Person 1 and person 2 can be friends, so they become direct friends.
    Request 1: Person 0 and person 2 cannot be friends since person 0 and person 1 would be indirect friends (0--2--1).
Example 3:
    Input: n = 5, restrictions = [[0,1],[1,2],[2,3]], requests = [[0,4],[1,2],[3,1],[3,4]]
    Output: [true,false,true,false]
    Explanation:
    Request 0: Person 0 and person 4 can be friends, so they become direct friends.
    Request 1: Person 1 and person 2 cannot be friends since they are directly restricted.
    Request 2: Person 3 and person 1 can be friends, so they become direct friends.
    Request 3: Person 3 and person 4 cannot be friends since person 0 and person 1 would be indirect friends (0--4--3--1).
 
Constraints:
    1. 2 <= n <= 1000
    2. 0 <= restrictions.length <= 1000
    3. restrictions[i].length == 2
    4. 0 <= xi, yi <= n - 1
    5. xi != yi
    6. 1 <= requests.length <= 1000
    7. requests[j].length == 2
    8. 0 <= uj, vj <= n - 1
    9. uj != vj
'''
# === 7412ms && 15.4MB === #
class DSU:
    def __init__(self, n):
        self.dsu = [i for i in range(n)]
        
    def find(self, x, update=False):
        if self.dsu[x] == x:
            return x
        if not update:
            return self.find(self.dsu[x], False)
        else:
            self.dsu[x] = self.find(self.dsu[x], True)
            return self.dsu[x]

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        res = []
        for u, v in requests:
            uk = dsu.find(u, True)
            vk = dsu.find(v, True)
            dsu.dsu[uk] = vk
            if any(dsu.find(x, False) == dsu.find(y, False) for x, y in restrictions):
                res.append(False)
                dsu.dsu[uk] = uk
            else:
                for i in range(n):
                    dsu.find(i, True)
                res.append(True)
        return res