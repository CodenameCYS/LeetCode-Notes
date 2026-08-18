/*
=== 372. Super Pow ===

Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example 1:
    Input: a = 2, b = [3]
    Output: 8
Example 2:
    Input: a = 2, b = [1,0]
    Output: 1024
*/
// === 8ms(95.45%) && 7MB(100%) === //
int superPow(int a, int* b, int bSize){
    long ans = 1;
    a = a % 1337;
    for(int i=0; i<bSize; ++i){
        long tmp = ans;
        for(int j=0; j<9; ++j){
            tmp = tmp * ans % 1337;
        }
        for(int j=0; j<b[i]; ++j){
            tmp = tmp * a % 1337;
        }
        ans = tmp;
        // printf("%ld\t", ans);
        // ans = (ans + 1337) % 1337;
        // printf("%ld\n", ans);
    }
    return ans;
}

