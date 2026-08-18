'''
=== 1233. Remove Sub-Folders from the Filesystem ===

Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.
If a folder[i] is located within another folder[j], it is called a sub-folder of it.
The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

Example 1:
    Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    Output: ["/a","/c/d","/c/f"]
    - Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
Example 2:
    Input: folder = ["/a","/a/b/c","/a/b/d"]
    Output: ["/a"]
    - Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are subfolders of "/a".
Example 3:
    Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
    Output: ["/a/b/c","/a/b/ca","/a/b/d"]
 
Constraints:
    1. 1 <= folder.length <= 4 * 10^4
    2. 2 <= folder[i].length <= 100
    3. folder[i] contains only lowercase letters and '/'
    4. folder[i] always starts with character '/'
    5. Each folder name is unique.
'''
# === 1280ms & 29.6MB === #
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        folder = sorted(folder, key= lambda x: len(x))
        for it in folder:
            need_add = True
            for tmp in ans:
                if it.find(tmp) == 0 and it[len(tmp)] == '/':
                    need_add = False
                    break
            if need_add:
                ans.append(it)
        return ans

# === 148ms === #
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = [tuple(i.split('/')) for i in folder]
        folder.sort(key=len)
        res = set()
        for i in folder:
            
            for j in range(1, len(i) + 1):
                if i[:j] in res:
                    break
            else:
                res.add(i)
        return list('/'.join(i) for i in res)