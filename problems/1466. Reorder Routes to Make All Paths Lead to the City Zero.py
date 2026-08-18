'''
=== 1466. Reorder Routes to Make All Paths Lead to the City Zero ===

There are n cities numbered from 0 to n-1 and n-1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
Roads are represented by connections where connections[i] = [a, b] represents a road from city a to b.
This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
It's guaranteed that each city can reach the city 0 after reorder.

Example 1:
    Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    Output: 3
    Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 2:
    Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
    Output: 2
    Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 3:
    Input: n = 3, connections = [[1,0],[2,0]]
    Output: 0
 
Constraints:
    1. 2 <= n <= 5 * 10^4
    2. connections.length == n-1
    3. connections[i].length == 2
    4. 0 <= connections[i][0], connections[i][1] <= n-1
    5. connections[i][0] != connections[i][1]
'''
# === 1264ms && 44.5MB === #
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        src2tgt = {i: [] for i in range(n)}
        tgt2src = {i: [] for i in range(n)}
        for src, tgt in connections:
            tgt2src[tgt].append(src)
            src2tgt[src].append(tgt)
        # print("src -> tgt: ", src2tgt)
        # print("tgt -> src: ", tgt2src)
        ans = 0
        queue = [0]
        have_connect = set()
        have_seen = {0}
        while queue != []:
            tgt = queue.pop(0)
            if tgt in have_connect:
                continue
            have_connect.add(tgt)
            src2tgt[tgt] = [it for it in src2tgt[tgt] if it not in have_seen]
            tgt2src[tgt] = [it for it in tgt2src[tgt] if it not in have_seen]
            ans += len(src2tgt[tgt])
            queue.extend(src2tgt[tgt])
            queue.extend(tgt2src[tgt])
            have_seen.update(src2tgt[tgt] + tgt2src[tgt])
            # print(queue)
            # print(have_connect)
        return ans
                
        
        