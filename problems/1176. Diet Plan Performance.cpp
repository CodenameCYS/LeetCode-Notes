/*
=== 1176. Diet Plan Performance ===

A dieter consumes calories[i] calories on the i-th day.  For every consecutive sequence of k days, they look at T, the total calories consumed during that sequence of k days:
    - If T < lower, they performed poorly on their diet and lose 1 point; 
    - If T > upper, they performed well on their diet and gain 1 point;
    - Otherwise, they performed normally and there is no change in points.
Return the total number of points the dieter has after all calories.length days.
- Note that: The total points could be negative.
 
Example 1:
    Input: calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
    Output: 0
    - Explaination: calories[0], calories[1] < lower and calories[3], calories[4] > upper, total points = 0.
Example 2:
    Input: calories = [3,2], k = 2, lower = 0, upper = 1
    Output: 1
    - Explaination: calories[0] + calories[1] > upper, total points = 1.
Example 3:
    Input: calories = [6,5,0,0], k = 2, lower = 1, upper = 5
    Output: 0
    - Explaination: calories[0] + calories[1] > upper, calories[2] + calories[3] < lower, total points = 0.
 
Constraints:
    1. 1 <= k <= calories.length <= 10^5
    2. 0 <= calories[i] <= 20000
    3. 0 <= lower <= upper
*/
// === 28ms && 11.4MB === //
int dietPlanPerformance(int* calories, int caloriesSize, int k, int lower, int upper){
    int sum_k[caloriesSize - k + 1];
    sum_k[0] = 0;
    for(int i=0; i<k; ++i){
        sum_k[0] += calories[i];
    }
    for(int i=k; i<caloriesSize; ++i){
        sum_k[i-k+1] = sum_k[i-k] + calories[i] - calories[i-k];
    }
    int ans = 0;
    for(int i=0; i<caloriesSize - k + 1; ++i){
        if(sum_k[i] < lower){
            --ans;
        }
        else if(sum_k[i] > upper){
            ++ans;
        }
    }
    return ans;
}

