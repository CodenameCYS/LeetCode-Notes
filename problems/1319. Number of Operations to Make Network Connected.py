'''
=== 1319. Number of Operations to Make Network Connected ===

There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.
Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1. 

Example 1:
    Input: n = 4, connections = [[0,1],[0,2],[1,2]]
    Output: 1
    - Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:
    Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
    Output: 2
Example 3:
    Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
    Output: -1
    - Explanation: There are not enough cables.
Example 4:
    Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
    Output: 0
 
Constraints:
    1. 1 <= n <= 10^5
    2. 1 <= connections.length <= min(n*(n-1)/2, 10^5)
    3. connections[i].length == 2
    4. 0 <= connections[i][0], connections[i][1] < n
    5. connections[i][0] != connections[i][1]
    6. There are no repeated connections.
    7. No two computers are connected by more than one cable.
'''
# === Time Limit Exceeded === #
class Solution:
    def add_into_clusters(self, clusters, connection):
        clusters_in = []
        for i, cluster in enumerate(clusters):
            if connection[0] in cluster or connection[1] in cluster:
                cluster.update(connection)
                clusters_in.append(i)
        if len(clusters_in) > 1:
            i0 = clusters_in[0]
            [clusters[i0].update(clusters[i]) for i in clusters_in[1:]]
            clusters = [clusters[i0]] + [clusters[i] for i,c in enumerate(clusters) if i not in clusters_in]
        # print(clusters)
        return clusters
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        clusters = [set([i]) for i in range(n)]
        for connection in connections:
            clusters = self.add_into_clusters(clusters, connection)
        print(clusters)
        return len(clusters) - 1

# === 716ms & 33MB === #
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        state = [0] * n
        cmatrix = [[] for i in range(n)]
        # print(cmatrix)
        for c in connections:
            cmatrix[c[0]].append(c[1])
            cmatrix[c[1]].append(c[0])
            # print(cmatrix)
        clusters = 0
        for i in range(n):
            stack = []
            if state[i] == 0:
                stack = [i]
                clusters += 1
                while stack != []:
                    tmp = stack.pop()
                    state[tmp] = 1
                    for j in cmatrix[tmp]:
                        if state[j] == 0:
                            stack.append(j)
        return clusters - 1
