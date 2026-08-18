'''
=== 1436. Destination City ===

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Example 1:
    Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    Output: "Sao Paulo" 
    Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:
    Input: paths = [["B","C"],["D","B"],["C","A"]]
    Output: "A"
    Explanation: All possible trips are: 
    "D" -> "B" -> "C" -> "A". 
    "B" -> "C" -> "A". 
    "C" -> "A". 
    "A". 
    Clearly the destination city is "A".
Example 3:
    Input: paths = [["A","Z"]]
    Output: "Z"
 
Constraints:
    1. 1 <= paths.length <= 100
    2. paths[i].length == 2
    3. 1 <= cityAi.length, cityBi.length <= 10
    4. cityAi != cityBi
    5. All strings consist of lowercase and uppercase English letters and the space character.
'''
# === 48ms && 13.7MB === #
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city = {}
        for a, b in paths:
            city[a] = 1 if a not in city.keys() else city[a] + 1
            city[b] = -1 if b not in city.keys() else city[b] - 1
        ans = [c for c,v in city.items() if v == -1][0]
        return ans