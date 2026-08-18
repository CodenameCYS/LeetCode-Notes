/*
=== 1014. Capacity To Ship Packages Within D Days ===

A conveyor belt has packages that must be shipped from one port to another within D days.
The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

Example 1:
    Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
    Output: 15
- Explanation: 
    A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
    1st day: 1, 2, 3, 4, 5
    2nd day: 6, 7
    3rd day: 8
    4th day: 9
    5th day: 10
- Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 
Example 2:
    Input: weights = [3,2,2,4,1,4], D = 3
    Output: 6
- Explanation: 
    A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
    1st day: 3, 2
    2nd day: 2, 4
    3rd day: 1, 4
Example 3:
    Input: weights = [1,2,3,1,1], D = 4
    Output: 3
- Explanation: 
    1st day: 1
    2nd day: 2
    3rd day: 3
    4th day: 1, 1
 
Note:
    1. 1 <= D <= weights.length <= 50000
    2. 1 <= weights[i] <= 500
*/
// === 644ms & 9.5MB === //
int shipWithinDays(int* weights, int weightsSize, int D) {
    if(D == 1){
        int ans = 0;
        for(int i=0; i<weightsSize; ++i){
            ans += weights[i];
        }
        return ans;
    }
    int ans = INT_MAX;
    for(int len=1; len<=weightsSize-D; ++len){
        int tempans = 0;
        for(int i=0; i<len; ++i){
            tempans += weights[i];
        }
        int uplimit = tempans+weights[len] ;
        // printf("%d\t", tempans);
        
        for(int t=tempans; t<uplimit; ++t){
            int dayleft = D-1;
            int temp = 0;
            for(int i=len; i<weightsSize; ++i){
                if(weights[i] > t){
                    dayleft = 0;
                    break;
                }
                temp += weights[i];
                if(temp > t){
                    --dayleft;
                    temp = weights[i];
                    if(dayleft <= 0){
                        break;
                    }
                }
            }
            // printf("%d\n", t);
            if(dayleft <= 0){
                continue;
            }
            else{
                ans = t;
                break;
            }
        }
        if(ans != INT_MAX){
            break;
        }
    }
    if(ans == INT_MAX){
        ans = 0;
        for(int i=0; i<weightsSize; ++i){
            ans = ans > weights[i] ? ans : weights[i];
        }
    }
    return ans;
}