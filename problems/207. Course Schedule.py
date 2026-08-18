'''
=== 207. Course Schedule ===

There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
    Input: 2, [[1,0]] 
    Output: true
    Explanation: There are a total of 2 courses to take. 
                 To take course 1 you should have finished course 0. So it is possible.
Example 2:
    Input: 2, [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
                 To take course 1 you should have finished course 0, and to take course 0 you should
                 also have finished course 1. So it is impossible.

Note:
    1. The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    2. You may assume that there are no duplicate edges in the input prerequisites.
'''
# === 1684ms(5.04%) && 279.3(6.12%) === #
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requirements = {i:set() for i in range(numCourses)}
        for a,b in prerequisites:
            # print(a,b)
            requirements[a].add(b)
            requirements[a].update(requirements[b])
            for c in requirements[b]:
                requirements[a].update(requirements[c])
            for k,v in requirements.items():
                if a in v:
                    v.update(requirements[a])
            # print(requirements)
            if a in requirements[a]:
                return False
        print(requirements)
        return True
        