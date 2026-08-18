'''
=== 1494. Parallel Courses II ===

Given the integer n representing the number of courses at some university labeled from 1 to n, and the array dependencies where dependencies[i] = [xi, yi]  represents a prerequisite relationship, that is, the course xi must be taken before the course yi.  Also, you are given the integer k.
In one semester you can take at most k courses as long as you have taken all the prerequisites for the courses you are taking.
Return the minimum number of semesters to take all courses. It is guaranteed that you can take all courses in some way.

Example 1:
    Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
    Output: 3 
    Explanation: The figure above represents the given graph. In this case we can take courses 2 and 3 in the first semester, then take course 1 in the second semester and finally take course 4 in the third semester.
Example 2:
    Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
    Output: 4 
    Explanation: The figure above represents the given graph. In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester and take course 4 in the second semester, then take course 1 in the third semester and finally take course 5 in the fourth semester.
Example 3:
    Input: n = 11, dependencies = [], k = 2
    Output: 6
 
Constraints:
    1. 1 <= n <= 15
    2. 1 <= k <= n
    3. 0 <= dependencies.length <= n * (n-1) / 2
    4. dependencies[i].length == 2
    5. 1 <= xi, yi <= n
    6. xi != yi
    7. All prerequisite relationships are distinct, that is, dependencies[i] != dependencies[j].
    8. The given graph is a directed acyclic graph.
'''
# === 48ms(49.92%) && 13.8MB === #
class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        dep = {i: set() for i in range(1, n+1)}
        counter = [0 for i in range(n+1)]
        for x, y in dependencies:
            dep[y].add(x)
            counter[x] += 1
        stack = sorted([x for x in range(1, n+1) if len(dep[x]) == 0], key=lambda x: counter[x])
        have_taken = 0
        ans = 0
        while have_taken < n:
            # print(stack)
            unlock = []
            for i in range(k):
                course = stack.pop()
                for key, v in dep.items():
                    if course in v:
                        v.remove(course)
                        if len(v) == 0:
                            unlock.append(key)
                have_taken += 1
                if stack == []:
                    break
            for c in unlock:
                stack.append(c)
                dep.pop(c)
            stack = sorted(stack, key=lambda x: counter[x])
            ans += 1
            # print(have_taken)
        return ans
                