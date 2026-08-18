/*
=== 390. Elimination Game ===

There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.
We keep repeating the steps again, alternating left to right and right to left, until a single number remains.
Find the last number that remains starting with a list of length n.

Example:
    Input:
    n = 9,
    1 2 3 4 5 6 7 8 9
    2 4 6 8
    2 6
    6
    Output:
    6
*/
// === 0ms(100%) && 7.1MB(100%) === //
int lastRemaining(int n){
    if(n == 1){
        return 1;
    }
    else if(n < 4){
        return 2;
    }
    else if(n % 4 < 2){
        return 4 * lastRemaining(n / 4) - 2;
    }
    else{
        return 4 * lastRemaining(n / 4);
    }
}