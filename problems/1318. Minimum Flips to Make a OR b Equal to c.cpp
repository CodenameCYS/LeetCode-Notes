/*
=== 1318. Minimum Flips to Make a OR b Equal to c ===

Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

Example 1:
    Input: a = 2, b = 6, c = 5
    Output: 3
    - Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
Example 2:
    Input: a = 4, b = 2, c = 7
    Output: 1
Example 3:
    Input: a = 1, b = 2, c = 3
    Output: 0
 
Constraints:
    1. 1 <= a <= 10^9
    2. 1 <= b <= 10^9
    3. 1 <= c <= 10^9
*/
int dec2bin(int x, int* y){
    int size = 0;
    while(x != 0){
        y[size] = x % 2;
        x /= 2;
        ++ size;
    }
    for(int i=size; i<30; ++i){
        y[i] = 0;
    }
    return size;
}
int max(int a, int b, int c){
    if(a < b){
        return b < c ? c : b;
    }
    else{
        return a < c ? c : a;
    }
}
// === 0ms && 6.7MB === //
int minFlips(int a, int b, int c){
    int a2[30], b2[30], c2[30];
    int a_size = dec2bin(a, a2);
    int b_size = dec2bin(b, b2);
    int c_size = dec2bin(c, c2);
    int n = max(a_size, b_size, c_size);
    int ans = 0;
    for(int i=0; i<n; ++i){
        if(c2[i] == 0 && a2[i] + b2[i] == 0){
            continue;
        }
        else if(c2[i] == 1 && a2[i] + b2[i] > 0){
            continue;
        }
        else if(c2[i] == 0){
            ans += (a2[i] + b2[i]);
        }
        else{
            ans += 1;
        }
    }
    return ans;
}