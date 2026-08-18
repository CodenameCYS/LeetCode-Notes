/*
=== 989. Add to Array-Form of Integer ===

For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].
Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

Example 1:
    Input: A = [1,2,0,0], K = 34
    Output: [1,2,3,4]
    Explanation: 1200 + 34 = 1234
Example 2:
    Input: A = [2,7,4], K = 181
    Output: [4,5,5]
    Explanation: 274 + 181 = 455
Example 3:
    Input: A = [2,1,5], K = 806
    Output: [1,0,2,1]
    Explanation: 215 + 806 = 1021
Example 4:
    Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
    Output: [1,0,0,0,0,0,0,0,0,0,0]
    Explanation: 9999999999 + 1 = 10000000000
 
Note：
    1. 1 <= A.length <= 10000
    2. 0 <= A[i] <= 9
    3. 0 <= K <= 10000
    4. If A.length > 1, then A[0] != 0
*/
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
// === 100 ms & 18.1 MB (85.71%) === //
int max(int x, int y){
    return x > y ? x : y;
}
int* addToArrayForm(int* A, int ASize, int K, int* returnSize) {
    int ansSize = max(ASize, (log(K-1)/log(10)+1));
    //printf("%d\n", ansSize);
    int* ans = (int*)malloc((ansSize+1)*sizeof(int));
    *returnSize=0;
    int carry=0;
    for(int i=ASize-1; i>=0; --i){
        int bit = K % 10;
        ans[ansSize - *returnSize] = (bit + A[i] + carry) % 10;
        carry = (bit + A[i] + carry) / 10;
        ++ *returnSize;
        K /= 10;
    }
    //printf("%d\n", *returnSize);
    while(K > 0 || carry > 0){
        int bit = K % 10;
        ans[ansSize - *returnSize] = (bit + carry) % 10;
        carry = (bit + carry) / 10;
        ++ *returnSize;
        K /= 10;
    }
    //printf("%d\n", *returnSize);
    return &ans[ansSize + 1 - *returnSize];
}