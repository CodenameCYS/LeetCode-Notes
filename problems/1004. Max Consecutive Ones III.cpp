/*
=== 1004. Max Consecutive Ones III ===

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s. 

Example 1:
    Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
    Output: 6
- Explanation: 
    [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:
    Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
    Output: 10
- Explanation: 
    [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
 
Note:
    1. 1 <= A.length <= 20000
    2. 0 <= K <= A.length
    3. A[i] is 0 or 1 
*/
int longestOnes(int* A, int ASize, int K) {
    bool isbegin = true;
    int ans = 0;
    int tempans = 0;
    for(int i=0; i<ASize; ++i){
        if(A[i] == 0 || isbegin){
            int count = 0;
            for(int j=i; j<ASize; ++j){
                if(A[j] == 1){
                    ++ tempans;
                }
                else{
                    if(count >= K){
                        break;
                    }
                    ++ count;
                    ++ tempans;
                }
            }
            ans = tempans > ans ? tempans : ans;
            isbegin = A[i] == 0;
            tempans = 0;
            // printf("%d\n", ans);
        }
        else{
            ++tempans;
        }
    }
    return ans;
}