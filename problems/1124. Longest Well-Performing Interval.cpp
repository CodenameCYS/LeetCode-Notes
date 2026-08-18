/*
=== 1124. Longest Well-Performing Interval ===

We are given hours, a list of the number of hours worked per day for a given employee.
A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.
A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.
Return the length of the longest well-performing interval.

Example 1:
    Input: hours = [9,9,6,0,6,6,9]
    Output: 3
    - Explanation: The longest well-performing interval is [9,9,6].
 
Constraints:
    1. 1 <= hours.length <= 10000
    2. 0 <= hours[i] <= 16
*/
// === 1488ms && 8MB === //
int longestWPI(int* hours, int hoursSize){
    int tmp[hoursSize + 1];
    tmp[0] = 0;
    for(int i=1; i<=hoursSize; ++i){
        if(hours[i-1] > 8){
            tmp[i] = tmp[i-1] + 1;
        }
        else{
            tmp[i] = tmp[i-1] - 1;
        }
        // printf("%d\t", tmp[i]);
    }
    int ans = 0;
    for(int i=1; i<=hoursSize; ++i){
        for(int j=0; j<i; ++j){
            if(tmp[i] - tmp[j] > 0){
                ans = ans > i-j ? ans : i-j;
            }
        }
    }
    return ans;
}

