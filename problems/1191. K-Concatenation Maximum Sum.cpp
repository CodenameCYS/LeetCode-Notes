/*
=== 1191. K-Concatenation Maximum Sum ===

Given an integer array arr and an integer k, modify the array by repeating it k times.
For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].
Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.
As the answer can be very large, return the answer modulo 10^9 + 7.
 
Example 1:
    Input: arr = [1,2], k = 3
    Output: 9
Example 2:
    Input: arr = [1,-2,1], k = 5
    Output: 2
Example 3:
    Input: arr = [-1,-2], k = 7
    Output: 0
 
Constraints:
    1. 1 <= arr.length <= 10^5
    2. 1 <= k <= 10^5
    3. -10^4 <= arr[i] <= 10^4
*/
long sgn(long x){
    return x > 0 ? x : 0;
}
// === 40ms(100%) && 12.1MB === //
int kConcatenationMaxSum(int* arr, int arrSize, int k){
    long max = 0, min = 0, max_ij = 0, min_ij = 0;
    long cumsum[arrSize+1];
    cumsum[0] = 0;
    for(int i=0; i<arrSize; ++i){
        cumsum[i+1] = cumsum[i] + arr[i];
        if(max < cumsum[i+1]){
            max = cumsum[i+1];
        }
        else{
            min_ij = cumsum[i+1] - max < min_ij ? cumsum[i+1] - max : min_ij;
        }
        if(min > cumsum[i+1]){
            min = cumsum[i+1];
        }
        else{
            max_ij = cumsum[i+1] - min > max_ij ? cumsum[i+1] - min : max_ij;
        }
    }
    // printf("sum = %d, max_ij = %d , min_ij = %d\n", cumsum[arrSize], max_ij, min_ij);
    long ans1 = ((sgn(cumsum[arrSize]) * (k-1)) % 1000000007 + max_ij) % 1000000007;
    long ans2 = ((sgn(cumsum[arrSize]) * (k-2)) % 1000000007 + sgn(cumsum[arrSize] - min_ij)) % 1000000007;
    return ans1 > ans2 ? ans1 : ans2;
}

