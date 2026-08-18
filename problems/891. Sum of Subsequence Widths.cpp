/*
=== 891. Sum of Subsequence Widths ===

Given an array of integers A, consider all non-empty subsequences of A.
For any sequence S, let the width of S be the difference between the maximum and minimum element of S.
Return the sum of the widths of all subsequences of A. 
As the answer may be very large, return the answer modulo 10^9 + 7.

Example 1:
Input: [2,1,3]
Output: 6
Explanation:
Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.
 
Note:
1. 1 <= A.length <= 20000
2. 1 <= A[i] <= 20000
*/
void QuickSort(int* arr, int start, int end){
    if(start >= end){
        return;
    }
    int i = start, j= end;
    int temp = arr[start];
    while(i < j){
        while(i < j && arr[j] >= temp){
            -- j;
        }
        if(i < j){
            arr[i] = arr[j];
            ++ i;
        }
        while(i < j && arr[i] <= temp){
            ++ i;
        }
        if(i < j){
            arr[j] = arr[i];
            -- j;
        }
    }
    arr[i] = temp;
    QuickSort(arr, start, i-1);
    QuickSort(arr, i+1, end);
}
// 该代码修改自uwi大神
int sumSubseqWidths(int* A, int ASize) {
    QuickSort(A, 0, ASize-1);
    
    long mod = 1000000007;
    
    long long ans = 0;
    long long s = 0;
    long long n = 0;
    for(int i=ASize-1; i>=1; --i){
        s = s * 2 + A[i];
        n = n * 2 + 1;
        s = s % mod;
        n = n % mod;
        
        ans += s - n*A[i-1];
        ans = ans % mod;
    }
    if(ans < 0){
        ans += mod;
    }
    return ans;
}