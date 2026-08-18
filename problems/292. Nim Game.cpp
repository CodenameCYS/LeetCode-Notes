/*
=== 292. Nim Game ===

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.
Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

Example:
    Input: 4
    Output: false 
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be 
             removed by your friend.
*/
// === 0ms(100%) & 6.7MB(16.67%) === //
bool canWinNim(int n) {
    if(n % 4 == 0){
        return false;
    }
    else{
        return true;
    }
}
// === 0ms(100%) & 6.6MB(83.33%) === //
bool canWinNim(int n) {
    return n % 4 != 0;
}
// === 这个内存是用最少的代码 === //
bool canWinNim(int n) {
    return 3&n;
}