/*
=== 926. Flip String to Monotone Increasing ===

A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0.)
We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.
Return the minimum number of flips to make S monotone increasing.

Example 1:
    Input: "00110"
    Output: 1
Explanation: We flip the last digit to get 00111.

Example 2:
    Input: "010110"
    Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Example 3:
    Input: "00011000"
    Output: 2
Explanation: We flip to get 00000000.
 
Note:
    1. 1 <= S.length <= 20000
    2. S only consists of '0' and '1' characters.
*/
int minFlipsMonoIncr(char* S) {
    int len = strlen(S);

    int zeros[len], ones[len];
    zeros[0] = S[0] - 48;
    ones[len-1] = 49 - S[len-1];
    
    for(int i=1; i<len; ++i){
        zeros[i] = zeros[i-1] + S[i] - 48;
        ones[len-1-i] = ones[len-i] + 49 - S[len-1-i];
    }
    if(zeros[len-1] == 0 || ones[0] == 0){
        return 0;
    }
    int ans = zeros[len-1] < ones[0] ? zeros[len-1] : ones[0];
    for(int i=1; i<len-1; ++i){
        int temp = zeros[i-1] + ones[i+1];
        ans = ans < temp ? ans : temp;
    }
    return ans;
}