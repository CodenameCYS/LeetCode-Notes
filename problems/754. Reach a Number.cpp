/*
=== 754. Reach a Number ===

You are standing at position 0 on an infinite number line. There is a goal at position target.
On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.
Return the minimum number of steps required to reach the destination.

Example 1:
    Input: target = 3
    Output: 2
    Explanation:
    On the first move we step from 0 to 1.
    On the second step we step from 1 to 3.
Example 2:
    Input: target = 2
    Output: 3
    Explanation:
    On the first move we step from 0 to 1.
    On the second move we step  from 1 to -1.
    On the third move we step from -1 to 2.

Note:
    1. target will be a non-zero integer in the range [-10^9, 10^9].
*/
// === 0ms(100%) && 5.2MB(100%) === //
int reachNumber(int target){
    if(target < 0){
        target = -target;
    }
    else if(target == 0){
        return 0;
    }
    int i = 1;
    int sum = 0;
    for(;; ++i){
        sum += i;
        if(sum >= target && (sum-target) % 2 == 0){
            break;
        }
    }
    return i;
}