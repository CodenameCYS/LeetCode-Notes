'''
=== 1617. Count Subtrees With Max Distance Between Cities ===

There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.
A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.
For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.
Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.
Notice that the distance between the two cities is the number of edges in the path between them.

Example 1:
    Input: n = 4, edges = [[1,2],[2,3],[2,4]]
    Output: [3,4,0]
    Explanation:
    The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
    The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
    No subtree has two nodes where the max distance between them is 3.
Example 2:
    Input: n = 2, edges = [[1,2]]
    Output: [1]
Example 3:
    Input: n = 3, edges = [[1,2],[2,3]]
    Output: [2,1]
 
Constraints:
    1. 2 <= n <= 15
    2. edges.length == n-1
    3. edges[i].length == 2
    4. 1 <= ui, vi <= n
    5. All pairs (ui, vi) are distinct.
'''
# === 1964ms && 14MB === #
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        edge_list = defaultdict(list)
        for u, v in edges:
            edge_list[u-1].append(v-1)
            edge_list[v-1].append(u-1)
        # print(edge_list)
            
        distance = [[0 for _ in range(n)] for _ in range(n)]    
        def bfs(u):
            nonlocal distance
            stack = [u]
            have_visited = {u}
            depth = 0
            while stack != []:
                n = len(stack)
                for _ in range(n):
                    v = stack.pop(0)
                    distance[u][v] = depth
                    for node in edge_list[v]:
                        if node not in have_visited:
                            have_visited.add(node)
                            stack.append(node)
                depth += 1
                # print(distance[u])
            return
        for i in range(n):
            bfs(i)
        # print(distance)
        
        def is_connected(nodes):
            queue = nodes[:1]
            status = [0 if x in nodes else -1 for x in range(n)]
            status[nodes[0]] = 1
            while queue != []:
                m = len(queue)
                for _ in range(m):
                    u = queue.pop(0)
                    for v in edge_list[u]:
                        if status[v] == 0:
                            queue.append(v)
                            status[v] = 1
            return all(x != 0 for x in status)
        
        def cal_max_distance(nodes):
            n = len(nodes)
            max_dis = 0
            for i in range(n-1):
                u = nodes[i]
                for j in range(i+1, n):
                    v = nodes[j]
                    max_dis = max(max_dis, distance[u][v])
            return max_dis
        
        ans = [0 for i in range(n)]
        for i in range(1, 2**n):
            nodes = []
            for k in range(n):
                if i % 2 == 1:
                    nodes.append(k)
                i = i // 2
                if i == 0:
                    break
            if is_connected(nodes):
                ans[cal_max_distance(nodes)] += 1
        # print("=" * 20)
        return ans[1:]
            
# ======================================================================================= #
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.children={}
# === 36ms && 14.3MB === #
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        edgedic=collections.defaultdict(set)
        for a,b in edges:
            edgedic[a].add(b)
            edgedic[b].add(a)
            
        subsize={}
        def constructTree(root,nodes,edgedic):
            if len(nodes)==1:
                return TreeNode(root)
            children=collections.defaultdict(set)
            def dfs(key,node):
                children[key].add(node)
                for nnd in edgedic[node]:
                    if nnd!=root and nnd in nodes and nnd not in children[key]:
                        dfs(key,nnd)
            for nd in edgedic[root]:
                if nd in nodes:
                    dfs(nd,nd)
            ans=TreeNode(root)
            for k in children:
                subsize[k]=len(children[k])
                ans.children[k]=constructTree(k,children[k],edgedic)
            return ans
        root=constructTree(1,set(range(1,n+1)),edgedic)
        
        def helper(root,num):
            # root: tree root
            # num: number of nodes in the tree
            # ret: [{(h,d): #num of subtrees stem from root and has diameter d and height h}, the required n-1 length vector]
            if num==2:
                return [{(1,1):1},[1]]
            ans1=collections.defaultdict(int)
            ans2=[0]*(num-1)
            tmpans1=[]
            for nv in root.children:
                tmp1, tmp2=helper(root.children[nv],subsize[nv])
                tmp=collections.defaultdict(int)
                for i in range(len(tmp2)):
                    ans2[i]+=tmp2[i]
                for h,d in tmp1:
                    tmp[h+1,max(d,h+1)]+=tmp1[h,d]
                tmp[1,1]+=1
                tmpans1.append(tmp)
            # construct ans1
            for tmp in tmpans1:
                new=copy.copy(ans1)
                for h,d in tmp:
                    new[h,d]+=tmp[h,d]
                    for h1,d1 in ans1:
                        new[max(h1,h),max([h+h1,d,d1])]+=ans1[h1,d1]*tmp[h,d]
                ans1=new
            for h,d in ans1:
                ans2[d-1]+=ans1[h,d]
            return [ans1,ans2]
        return helper(root,n)[1]