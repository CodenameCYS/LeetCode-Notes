/*
=== 930. Binary Subarrays With Sum ===

In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Example 1:
    Input: A = [1,0,1,0,1], S = 2
    Output: 4
Explanation: 
    The 4 subarrays are bolded below:
        [**1,0,1**,0,1]
        [**1,0,1,0**,1]
        [1,**0,1,0,1**]
        [1,0,**1,0,1**]
 
Note:
    1. A.length <= 30000
    2. 0 <= S <= A.length
    3. A[i] is either 0 or 1.
*/
int numSubarraysWithSum(int* A, int ASize, int S) {
    int zeros[ASize + 1];
    int count = 0;
    int ones_num = 0;
    for(int i=0; i<ASize; ++i){
        if(A[i] == 0){
            ++ count;
        }
        else{
            zeros[ones_num] = count;
            ++ ones_num;
            count = 0;
        }
    }
    zeros[ones_num] = count;
    
    int ans = 0;
    if(S == 0){
        for(int i=0; i<=ones_num; ++i){
            ans += zeros[i]*(zeros[i]+1)/2;
        }
    }
    else{
        for(int i=0; i<=ones_num-S; ++i){
            ans += (zeros[i]+1) * (zeros[i+S]+1);
        }
    }
    return ans;
}