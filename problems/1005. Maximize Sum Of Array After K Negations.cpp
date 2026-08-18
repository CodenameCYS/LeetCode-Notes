/*
=== 1005. Maximize Sum Of Array After K Negations ===

Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)
Return the largest possible sum of the array after modifying it in this way.

Example 1:
    Input: A = [4,2,3], K = 1
    Output: 5
    Explanation: Choose indices (1,) and A becomes [4,-2,3].
Example 2:
    Input: A = [3,-1,0,2], K = 3
    Output: 6
    Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
Example 3:
    Input: A = [2,-3,-1,5,-4], K = 2
    Output: 13
    Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
 
Note:
    1. 1 <= A.length <= 10000
    2. 1 <= K <= 10000
    3. -100 <= A[i] <= 100
*/
void QuickSort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed, temp=nums[st];
    while(i<j){
        while(i<j && nums[j] >= temp){
            --j;
        }
        if(i<j){
            nums[i] = nums[j];
            ++i;
        }
        while(i<j && nums[i] <= temp){
            ++i;
        }
        if(i<j){
            nums[j] = nums[i];
            --j;
        }
    }
    nums[i] = temp;
    QuickSort(nums, st, i-1);
    QuickSort(nums, i+1, ed);
}
// === 4ms & 7MB === //
int largestSumAfterKNegations(int* A, int ASize, int K) {
    int ans = 0;
    int neg[ASize];
    int negnum = 0;
    int minabs = INT_MAX;
    for(int i=0; i<ASize; ++i){
        ans += A[i];
        if(A[i] < 0){
            neg[negnum] = A[i];
            ++negnum;
        }
        minabs = minabs < abs(A[i]) ? minabs : abs(A[i]);
    }
    QuickSort(neg, 0, negnum-1);
    if(K <= negnum){
        for(int i=0; i<K; ++i){
            ans -= 2*neg[i];
        }
    }
    else{
        for(int i=0; i<negnum; ++i){
            ans -= 2*neg[i];
        }
        ans -= 2*((K-negnum)%2)*minabs;
    }
    return ans;
}