/*
=== 475. Heaters ===

Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.
Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.
So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
1. Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
2. Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
3. As long as a house is in the heaters' warm radius range, it can be warmed.
4. All the heaters follow your radius standard and the warm radius will the same.
 
Example 1:
    Input: [1,2,3],[2]
    Output: 1
    Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
Example 2:
    Input: [1,2,3,4],[1,4]
    Output: 1
    Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
*/
void quick_sort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed, tmp=nums[st];
    while(i<j){
        while(i<j && nums[j] >= tmp){
            -- j;
        }
        if(i<j){
            nums[i] = nums[j];
            ++ i;
        }
        while(i<j && nums[i]<=tmp){
            ++ i;
        }
        if(i<j){
            nums[j] = nums[i];
            -- j;
        }
    }
    nums[i] = tmp;
    quick_sort(nums, st, i-1);
    quick_sort(nums, i+1, ed);
}
// === 1432ms(7.69%) && 9.5MB(25%) === //
int findRadius(int* houses, int housesSize, int* heaters, int heatersSize){
    quick_sort(houses, 0, housesSize-1);
    quick_sort(heaters, 0, heatersSize-1);
    
    int j = 0;
    int radius = 0;
    if(houses[0] <= heaters[0]){
        radius = heaters[0] - houses[0];
    }
    while(j<housesSize && houses[j] <= heaters[0]){
        ++ j;
    }
    for(int i=0; i<heatersSize-1; ++i){
        while(j<housesSize && houses[j] <= heaters[i+1]){
            int left = houses[j] - heaters[i];
            int right = heaters[i+1] - houses[j];
            int tmp = left < right ? left : right;
            radius = radius > tmp ? radius : tmp;
            ++ j;
        }
    }
    if(j < housesSize){
        int tmp = houses[housesSize-1] - heaters[heatersSize-1];
        radius = radius > tmp ? radius : tmp;
    }
    return radius;
}

