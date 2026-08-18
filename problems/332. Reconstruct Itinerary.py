'''
=== 332. Reconstruct Itinerary ===

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
    1. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    2. All airports are represented by three capital letters (IATA code).
    3. You may assume all tickets form at least one valid itinerary.
    4. One must use all the tickets once and only once.

Example 1:
    Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:
    Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
                But it is larger in lexical order.
'''
# === 80ms(78.66%) && 14.5MB(13.93%) === #
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        cache = {}
        for idx, (x, y) in enumerate(tickets):
            cache[x] = cache.get(x, []) + [y]
        
        for k in cache:
            cache[k] = sorted(cache[k])
        # print(cache)

        ans = []
        def dfs(node):
            nonlocal ans, cache
            while cache.get(node, []) != []:
                dfs(cache[node].pop(0))
            ans.insert(0, node)
        dfs("JFK")

        return ans