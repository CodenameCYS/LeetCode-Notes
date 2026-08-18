'''
=== 2280. Minimum Lines to Represent a Line Chart ===

You are given a 2D integer array stockPrices where stockPrices[i] = [dayi, pricei] indicates the price of the stock on day dayi is pricei. A line chart is created from the array by plotting the points on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting adjacent points. One such example is shown below:
Return the minimum number of lines needed to represent the line chart.

Example 1:
    Input: stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
    Output: 3
    Explanation:
    The diagram above represents the input, with the X-axis representing the day and Y-axis representing the price.
    The following 3 lines can be drawn to represent the line chart:
    - Line 1 (in red) from (1,7) to (4,4) passing through (1,7), (2,6), (3,5), and (4,4).
    - Line 2 (in blue) from (4,4) to (5,4).
    - Line 3 (in green) from (5,4) to (8,1) passing through (5,4), (6,3), (7,2), and (8,1).
    It can be shown that it is not possible to represent the line chart using less than 3 lines.
Example 2:
    Input: stockPrices = [[3,4],[1,2],[7,8],[2,3]]
    Output: 1
    Explanation:
    As shown in the diagram above, the line chart can be represented with a single line.
    
Constraints:
    1. 1 <= stockPrices.length <= 105
    2. stockPrices[i].length == 2
    3. 1 <= dayi, pricei <= 109
    4. All dayi are distinct.
'''
# === 2245ms && 59.6MB === #
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        def cal_line(p1, p2):
            k = (p2[1] - p1[1]) / (p2[0] - p1[0])
            b = p1[1] - k * p1[0]
            return k, b
        
        stockPrices = sorted(stockPrices)
        n = len(stockPrices)
        if n == 1:
            return 0
        res = 1
        k, b = cal_line(stockPrices[0], stockPrices[1])
        # print(k, b)
        for i in range(1, n-1):
            k1, b1 = cal_line(stockPrices[i], stockPrices[i+1])
            if k1 != k or b1 != b:
                res += 1
            k, b = k1, b1
            # print(k, b)
        return res