/*
=== 961. N-Repeated Element in Size 2N Array ===

In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
Return the element repeated N times.

Example 1:
    Input: [1,2,3,3]
    Output: 3

Example 2:
    Input: [2,1,2,5,3,2]
    Output: 2

Example 3:
    Input: [5,1,5,2,5,3,5,4]
    Output: 5
 
Note:
    1. 4 <= A.length <= 10000
    2. 0 <= A[i] < 10000
    3. A.length is even
*/
// === 12ms === //
int SortOnce(int* nums, int st, int ed){
    int temp = nums[st];
    int i = st, j = ed;
    while(i<j){
        while(i<j && nums[j] > temp){
            --j;
        }
        if(i<j){
            if(nums[j]==temp){
                return temp;
            }
            else{
                nums[i] = nums[j];
                ++i;
            }
        }
        while(i<j && nums[i] < temp){
            ++i;
        }
        if(i<j){
            if(nums[i]==temp){
                return temp;
            }
            else{
                nums[j] = nums[i];
                --j;
            }
        }
    }
    nums[i] = temp;
    return -(i+1);
}
int repeatedNTimes(int* A, int ASize) {
    int loc = SortOnce(A, 0, ASize-1);
    if(loc == -1){
        loc = SortOnce(A, 1, ASize-1);
    }
    else if(loc == -ASize){
        loc = SortOnce(A, 0, ASize-2);
    }
    if(loc >= 0){
        return loc;
    }
    int temp = A[0];
    for(int i=1; i<ASize; ++i){
        if(A[i] == temp){
            return temp;
        }
        temp = A[i];
    }
    return temp;
}
/* ================================================================================================== */
// === 8ms === //
int repeatedNTimes(int* A, int ASize) {
    int ans = A[0];
    for(int i=1; i<ASize; ++i){
        if(A[i] == ans){
            return ans;
        }
    }
    ans = A[1];
    for(int i=2; i<ASize; ++i){
        if(A[i] == ans){
            return ans;
        }
    }
    ans = A[2];
    for(int i=3; i<ASize; ++i){
        if(A[i] == ans){
            return ans;
        }
        ans = A[i];
    }
    return ans;
}