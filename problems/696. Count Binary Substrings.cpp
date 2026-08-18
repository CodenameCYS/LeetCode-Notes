/*
=== 696. Count Binary Substrings ===

Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.

Example 1:
    Input: "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
    Notice that some of these substrings repeat and are counted the number of times they occur.
    Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
    Input: "10101"
    Output: 4
    Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Note:
    1. s.length will be between 1 and 50,000.
    2. s will only consist of "0" or "1" characters.
*/
// === 8ms(91.67%) && 6.6MB(100%) === //
int countBinarySubstrings(char * s){
    int n = strlen(s);
    if(n == 0){
        return 0;
    }
    int counter[n], size = 0, count = 0;
    char bit = s[0];
    for(int i=0; i<n; ++i){
        if(s[i] == bit){
            ++ count;
        }
        else{
            counter[size] = count;
            ++ size;
            bit = s[i];
            count = 1;
        }
    }
    counter[size] = count;
    ++ size;
    
    int ans = 0;
    for(int i=0; i<size-1; ++i){
        ans += counter[i] < counter[i+1] ? counter[i] : counter[i+1];
    }
    return ans;
}

