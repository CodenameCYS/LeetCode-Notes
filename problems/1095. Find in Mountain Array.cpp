/*
=== 1095. Find in Mountain Array ===

(This problem is an interactive problem.)
You may recall that an array A is a mountain array if and only if:
    - A.length >= 3
    - There exists some i with 0 < i < A.length - 1 such that:
    - A[0] < A[1] < ... A[i-1] < A[i]
    - A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:
    - MountainArray.get(k) returns the element of the array at index k (0-indexed).
    - MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.
 
Example 1:
    Input: array = [1,2,3,4,5,3,1], target = 3
    Output: 2
    - Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:
    Input: array = [0,1,2,4,2,1], target = 3
    Output: -1
    - Explanation: 3 does not exist in the array, so we return -1.
 
Constraints:
    1. 3 <= mountain_arr.length() <= 10000
    2. 0 <= target <= 10^9
    3. 0 <= mountain_arr.get(index) <= 10^9
*/
/**
 * *********************************************************************
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * *********************************************************************
 *
 * int get(MountainArray *, int index);
 * int length(MountainArray *);
 */
int findMaxloc(MountainArray* mountainArr, int len, int* maxloc){
    int l = 0, lnum = get(mountainArr, 0);
    int r = len-1, rnum = get(mountainArr, len-1);
    while(r-l > 1){
        int tmp = get(mountainArr, (r + l) / 2);
        int ltmp = get(mountainArr, (l + r) / 2 - 1);
        if(ltmp > tmp){
            r = (l + r) / 2 - 1;
            rnum = ltmp;
            continue;
        }
        int rtmp = get(mountainArr, (l + r) / 2 + 1);
        if(rtmp < tmp){
            *maxloc = (l + r) / 2;
            return tmp;
        }
        else{
            l = (l + r) / 2 + 1;
            lnum = rtmp;
        }
    }
    if(lnum > rnum){
        *maxloc = l;
        return lnum;
    }
    else{
        *maxloc = r;
        return rnum;
    }
}
int findTarget(int target, MountainArray* mountainArr, int st, int ed, bool ascending){
    if(st == ed){
        if(get(mountainArr, st) == target){
            return st;
        }
        else{
            return -1;
        }
    }
    
    int lnum = get(mountainArr, st);
    if(lnum == target){
        return st;
    }
    else if(ascending && lnum > target){
        return -1;
    }
    else if(!ascending && lnum < target){
        return -1;
    }
    int rnum = get(mountainArr, ed);
    if(rnum == target){
        return ed;
    }
    else if(ascending && rnum < target){
        return -1;
    }
    else if(!ascending && rnum > target){
        return -1;
    }
    
    while(ed - st > 1){
        int tmp = get(mountainArr, (st + ed) / 2);
        if(tmp == target){
            return (st + ed) / 2;
        }
        else if(tmp < target){
            if(ascending){
                st = (st + ed) / 2;
            }
            else{
                ed = (st + ed) / 2;
            }
        }
        else{
            if(ascending){
                ed = (st + ed) / 2;
            }
            else{
                st = (st + ed) / 2;
            }
        }
    }
    return -1;
}
// === 4ms && 7.7MB === //
int findInMountainArray(int target, MountainArray* mountainArr){
	int len = length(mountainArr);
    // printf("array length : %d\n", len);
    // printf("st : %d\ted : %d\n", get(mountainArr, 0), get(mountainArr, len-1));
    int maxloc = 0;
    int maxnum = findMaxloc(mountainArr, len, &maxloc);
    // printf("max number : %d -> %d\n", maxloc, maxnum);
    if(maxnum < target){
        return -1;
    }
    else if(maxnum == target){
        return maxloc;
    }
    int ans = findTarget(target, mountainArr, 0, maxloc-1, true);
    if(ans != -1){
        return ans;
    }
    ans = findTarget(target, mountainArr, maxloc+1, len-1, false);
    return ans;
}