'''
=== 399. Evaluate Division ===

You are given equations in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating-point number). Given some queries, return the answers. If the answer does not exist, return -1.0.
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

Example 1:
    Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    Explanation: 
    Given: a / b = 2.0, b / c = 3.0
    queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
    return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:
    Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:
    Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    Output: [0.50000,2.00000,-1.00000,-1.00000]
 
Constraints:
    1. 1 <= equations.length <= 20
    2. equations[i].length == 2
    3. 1 <= equations[i][0], equations[i][1] <= 5
    4. values.length == equations.length
    5. 0.0 < values[i] <= 20.0
    6. 1 <= queries.length <= 20
    7. queries[i].length == 2
    8. 1 <= queries[i][0], queries[i][1] <= 5
    9. equations[i][0], equations[i][1], queries[i][0], queries[i][1] consist of lower case English letters and digits.
'''
class DSU:
    def __init__(self):
        self.dsu = {}
        
    def find(self, x):
        if x not in self.dsu:
            return None
        if x == self.dsu[x]:
            return x
        self.dsu[x] = self.find(self.dsu[x])
        return self.dsu[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.dsu[yr] = xr
        return
    
    def add(self, x):
        if x not in self.dsu:
            self.dsu[x] = x
        return
# === 32ms(57.19%) && 14.2MB(5.17%) === #
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        dsu = DSU()
        for i in range(n):
            x, y = equations[i]
            dsu.add(x)
            dsu.add(y)
            dsu.union(x, y)
            
        abs_values = {x:1 for x in dsu.dsu if dsu.find(x) == x}
        queue = list(abs_values.keys())
        while queue != []:
            x = queue.pop(0)
            for i in range(n):
                if equations[i][0] == x and equations[i][1] not in abs_values:
                    y = equations[i][1]
                    abs_values[y] = abs_values[x] / values[i]
                    queue.append(y)
                elif equations[i][1] == x and equations[i][0] not in abs_values:
                    y = equations[i][0]
                    abs_values[y] = abs_values[x] * values[i]
                    queue.append(y)
        
        ans = []
        for x, y in queries:
            if x not in abs_values or y not in abs_values or dsu.find(x) != dsu.find(y):
                ans.append(-1)
            else:
                ans.append(abs_values[x] / abs_values[y])
        return ans
        
            
        
        