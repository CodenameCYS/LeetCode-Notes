/*
=== 1317. Convert Integer to the Sum of Two No-Zero Integers ===

Given an integer n. No-Zero integer is a positive integer which doesn't contain any 0 in its decimal representation.
Return a list of two integers [A, B] where:
    - A and B are No-Zero integers.
    - A + B = n
It's guarateed that there is at least one valid solution. If there are many valid solutions you can return any of them.

Example 1:
    Input: n = 2
    Output: [1,1]
    - Explanation: A = 1, B = 1. A + B = n and both A and B don't contain any 0 in their decimal representation.
Example 2:
    Input: n = 11
    Output: [2,9]
Example 3:
    Input: n = 10000
    Output: [1,9999]
Example 4:
    Input: n = 69
    Output: [1,68]
Example 5:
    Input: n = 1010
    Output: [11,999]
 
Constraints:
    1. 2 <= n <= 10^4
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool has_no_zero(int a){
    while(a != 0){
        if(a % 10 == 0){
            return false;
        }
        a /= 10;
    }
    return true;
}
// === 4ms && 6.6MB === //
int* getNoZeroIntegers(int n, int* returnSize){
    *returnSize = 2;
    int* ans = (int*)malloc(2*sizeof(int));
    for(int a=1; a<=n/2; ++a){
        int b = n - a;
        // printf("%d\t%d\n",a,b);
        if(has_no_zero(a) && has_no_zero(b)){
            ans[0] = a;
            ans[1] = b;
            break;
        }
    }
    return ans;
}