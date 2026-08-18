'''
=== 547. Friend Circles ===

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.
Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
    Input: 
    [[1,1,0],
    [1,1,0],
    [0,0,1]]
    Output: 2
    Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
    The 2nd student himself is in a friend circle. So return 2.
Example 2:
    Input: 
    [[1,1,0],
    [1,1,1],
    [0,1,1]]
    Output: 1
    Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
    so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

Note:
    1. N is in range [1,200].
    2. M[i][i] = 1 for all students.
    3. If M[i][j] = 1, then M[j][i] = 1.
'''
# === 268ms(24.35%) && 12.9MB(100%) === #
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        stack = []
        have_seen = set()
        ans = 0
        for i, friends in enumerate(M):
            if i in have_seen:
                continue
            ans += 1
            stack.append(i)
            while stack != []:
                person = stack.pop()
                have_seen.add(person)
                stack += [j for j,v in enumerate(M[person]) if j not in have_seen and v == 1]
        return ans
# ==================================================================================== #               
class DSU:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        self.depth = [1 for i in range(N)]
        
    def find(self, k):
        if self.root[k] == k:
            return k
        self.root[k] = self.find(self.root[k])
        return self.root[k]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.root[y] = x
        return
# === 208ms(55.86%) && 14.3MB(37.71%) === #
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        dsu = DSU(n)
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    dsu.union(i, j)
        # print(dsu.parent)
        group = set()
        for i in range(n):
            group.add(dsu.find(i))
        return len(group)