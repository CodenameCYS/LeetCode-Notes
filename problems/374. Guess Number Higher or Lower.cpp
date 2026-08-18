/*
=== 374. Guess Number Higher or Lower ===

We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number is higher or lower.
You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
    -1 : My number is lower
    1 : My number is higher
    0 : Congrats! You got it!

Example :
    Input: n = 10, pick = 6
    Output: 6
*/
// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);
// === 4ms(51.50%) && 8.3MB(61.11%) === //
class Solution {
public:
    int my_guess(int st, int ed){
        // printf("%d\t%d :: ", st, ed);
        int mid = ((long)st + ed) / 2;
        int ret = guess(mid);
        // printf("%d\t%d\n", mid, ret);
        if(ret == 0){
            return mid;
        }
        else if(ret == 1){
            return my_guess(mid+1, ed);
        }
        else{
            return my_guess(st, mid-1);
        }
    }
    int guessNumber(int n) {
        return my_guess(1, n);
    }
};