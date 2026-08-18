/*
=== 1029. Two City Scheduling ===

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].
Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:
    Input: [[10,20],[30,200],[400,50],[30,20]]
    Output: 110
    - Explanation: 
    The first person goes to city A for a cost of 10.
    The second person goes to city A for a cost of 30.
    The third person goes to city B for a cost of 50.
    The fourth person goes to city B for a cost of 20.
    The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 
Note:
    1. 1 <= costs.length <= 100
    2. It is guaranteed that costs.length is even.
    3. 1 <= costs[i][0], costs[i][1] <= 1000
*/
// === 4ms(100%) & 9.1MB === //
class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        int ans = 0;
        int n = costs.size();
        int delta[n];
        for(int i=0; i<n; ++i){
            ans += costs[i][0];
            delta[i] = costs[i][1] - costs[i][0];
        }
        QuickSort(delta, 0, n-1);
        for(int i=0; i<n/2; ++i){
            ans += delta[i];
        }
        return ans;
    }
    
    void QuickSort(int* nums, int st, int ed){
        if(st >= ed){
            return;
        }
        int temp = nums[st];
        int i = st, j = ed;
        while(i < j){
            while(i < j && nums[j] >= temp){
                --j;
            }
            if(i < j){
                nums[i] = nums[j];
                ++i;
            }
            while(i < j && nums[i] <= temp){
                ++i;
            }
            if(i < j){
                nums[j] = nums[i];
                --j;
            }
        }
        nums[i] = temp;
        QuickSort(nums, st, i-1);
        QuickSort(nums, i+1, ed);
    }
};