'''
=== 3562. Maximum Profit from Trading Stocks with Discounts ===

You are given an integer n, representing the number of employees in a company. Each employee is assigned a unique ID from 1 to n, and employee 1 is the CEO. You are given two 1-based integer arrays, present and future, each of length n, where:
    - present[i] represents the current price at which the ith employee can buy a stock today.
    - future[i] represents the expected price at which the ith employee can sell the stock tomorrow.
The company's hierarchy is represented by a 2D integer array hierarchy, where hierarchy[i] = [ui, vi] means that employee ui is the direct boss of employee vi.
Additionally, you have an integer budget representing the total funds available for investment.
However, the company has a discount policy: if an employee's direct boss purchases their own stock, then the employee can buy their stock at half the original price (floor(present[v] / 2)).
Return the maximum profit that can be achieved without exceeding the given budget.
Note:
    - You may buy each stock at most once.
    - You cannot use any profit earned from future stock prices to fund additional investments and must buy only from budget.

Example 1:
    Input: n = 2, present = [1,2], future = [4,3], hierarchy = [[1,2]], budget = 3
    Output: 5
    Explanation:
    Employee 1 buys the stock at price 1 and earns a profit of 4 - 1 = 3.
    Since Employee 1 is the direct boss of Employee 2, Employee 2 gets a discounted price of floor(2 / 2) = 1.
    Employee 2 buys the stock at price 1 and earns a profit of 3 - 1 = 2.
    The total buying cost is 1 + 1 = 2 <= budget. Thus, the maximum total profit achieved is 3 + 2 = 5.
Example 2:
    Input: n = 2, present = [3,4], future = [5,8], hierarchy = [[1,2]], budget = 4
    Output: 4
    Explanation:
    Employee 2 buys the stock at price 4 and earns a profit of 8 - 4 = 4.
    Since both employees cannot buy together, the maximum profit is 4.
Example 3:
    Input: n = 3, present = [4,6,8], future = [7,9,11], hierarchy = [[1,2],[1,3]], budget = 10
    Output: 10
    Explanation:
    Employee 1 buys the stock at price 4 and earns a profit of 7 - 4 = 3.
    Employee 3 would get a discounted price of floor(8 / 2) = 4 and earns a profit of 11 - 4 = 7.
    Employee 1 and Employee 3 buy their stocks at a total cost of 4 + 4 = 8 <= budget. Thus, the maximum total profit achieved is 3 + 7 = 10.
Example 4:
    Input: n = 3, present = [5,2,3], future = [8,5,6], hierarchy = [[1,2],[2,3]], budget = 7
    Output: 12
    Explanation:
    Employee 1 buys the stock at price 5 and earns a profit of 8 - 5 = 3.
    Employee 2 would get a discounted price of floor(2 / 2) = 1 and earns a profit of 5 - 1 = 4.
    Employee 3 would get a discounted price of floor(3 / 2) = 1 and earns a profit of 6 - 1 = 5.
    The total cost becomes 5 + 1 + 1 = 7 <= budget. Thus, the maximum total profit achieved is 3 + 4 + 5 = 12.

Constraints:
    1. 1 <= n <= 160
    2. present.length, future.length == n
    3. 1 <= present[i], future[i] <= 50
    4. hierarchy.length == n - 1
    5. hierarchy[i] == [ui, vi]
    6. 1 <= ui, vi <= n
    7. ui != vi
    8. 1 <= budget <= 160
    9. There are no duplicate edges.
    10. Employee 1 is the direct or indirect boss of every employee.
    11. The input graph hierarchy is guaranteed to have no cycles.
'''
# === 2362ms && 22.8MB === #
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        tree = defaultdict(list)
        for u, v in hierarchy:
            tree[u - 1].append(v - 1)

        @lru_cache(None)
        def dp(u):
            '''
            input: u : int -> 0-based user id
            output: 
              - dp0: [int] * (budget+1) -> max profit for each budget if parent node was not bought
              - dp1: [int] * (budget+1) -> max profit for each budget if parent node was bought
            '''
            child_dp = [dp(v) for v in tree[u]]
            dp0 = [0] + [-math.inf] * (budget) # parent not buy
            dp1 = [0] + [-math.inf] * (budget) # parent buy
            for parent_bought, max_profits in [(0, dp0), (1, dp1)]:
                cost = present[u] if parent_bought == 0 else present[u] // 2
                profit = future[u] - cost
                
                dpA = [0] + [-math.inf] * (budget) # u not buy
                dpB = [-math.inf] * (budget+1) # u buy
                if cost <= budget:
                    dpB[cost] = profit
                for case0, case1 in child_dp:
                    new_dpA = [-math.inf] * (budget+1) # u not buy
                    for bgt in range(budget+1):
                        if dpA[bgt] == -math.inf:
                            continue
                        for k in range(budget-bgt+1):
                            if case0[k] == -math.inf:
                                continue
                            new_dpA[bgt+k] = max(new_dpA[bgt+k], dpA[bgt] + case0[k])
                    dpA = new_dpA
                    
                    new_dpB = [-math.inf] * (budget+1) # u buy
                    for bgt in range(budget+1):
                        if dpB[bgt] == -math.inf:
                            continue
                        for k in range(budget-bgt+1):
                            if case1[k] == -math.inf:
                                continue
                            new_dpB[bgt+k] = max(new_dpB[bgt+k], dpB[bgt] + case1[k])
                    dpB = new_dpB
                    
                for bgt in range(budget+1):
                    max_profits[bgt] = max(dpA[bgt], dpB[bgt])
                    
            return dp0, dp1
                    
                
        
        max_profits, _ = dp(0)
        return max(max_profits)
        
                