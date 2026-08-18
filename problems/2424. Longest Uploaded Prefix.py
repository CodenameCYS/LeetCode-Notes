'''
=== 2424. Longest Uploaded Prefix ===

You are given a stream of n videos, each represented by a distinct number from 1 to n that you need to "upload" to a server. You need to implement a data structure that calculates the length of the longest uploaded prefix at various points in the upload process.
We consider i to be an uploaded prefix if all videos in the range 1 to i (inclusive) have been uploaded to the server. The longest uploaded prefix is the maximum value of i that satisfies this definition.
Implement the LUPrefix class:
    - LUPrefix(int n) Initializes the object for a stream of n videos.
    - void upload(int video) Uploads video to the server.
    - int longest() Returns the length of the longest uploaded prefix defined above.

Example 1:
    Input
    ["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"]
    [[4], [3], [], [1], [], [2], []]
    Output
    [null, null, 0, null, 1, null, 3]
    Explanation
    LUPrefix server = new LUPrefix(4);   // Initialize a stream of 4 videos.
    server.upload(3);                    // Upload video 3.
    server.longest();                    // Since video 1 has not been uploaded yet, there is no prefix.
                                         // So, we return 0.
    server.upload(1);                    // Upload video 1.
    server.longest();                    // The prefix [1] is the longest uploaded prefix, so we return 1.
    server.upload(2);                    // Upload video 2.
    server.longest();                    // The prefix [1,2,3] is the longest uploaded prefix, so we return 3.
 
Constraints:
    1. 1 <= n <= 105
    2. 1 <= video <= 105
    3. All values of video are distinct.
    4. At most 2 * 105 calls in total will be made to upload and longest.
    5. At least one call will be made to longest.
'''
class DSU:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        
    def find(self, k):
        if self.root[k] != k:
            self.root[k] = self.find(self.root[k])
        return self.root[k]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.root[x] = y
        return
# === 1880ms && 72.5MB === # 
class LUPrefix:

    def __init__(self, n: int):
        self.n = n
        self.status = [0 for _ in range(n)]
        self.dsu = DSU(n)

    def upload(self, video: int) -> None:
        idx = video-1
        self.status[idx] = 1
        if idx - 1 >= 0 and self.status[idx-1] == 1:
            self.dsu.union(idx-1, idx)
        if idx + 1 < self.n and self.status[idx+1] == 1:
            self.dsu.union(idx, idx+1)
        return

    def longest(self) -> int:
        if self.status[0] == 0:
            return 0
        return self.dsu.find(0) + 1


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()