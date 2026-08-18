/*
=== 539. Minimum Time Difference ===

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:
    Input: ["23:59","00:00"]
    Output: 1

Note:
    1. The number of time points in the given list is at least 2 and won't exceed 20000.
    2. The input time is legal and ranges from 00:00 to 23:59.
*/
int time2minutes(char* time){
    int ans = 0;
    ans = 60*(10*(time[0]-'0') + time[1]-'0') + (10*(time[3]-'0') + time[4]-'0');
    return ans;
}
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
        while(i<j && nums[i] <= tmp){
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
// === 12ms(69.23%) && 8.8MB(100%) === //
int findMinDifference(char ** timePoints, int timePointsSize){
    int time[timePointsSize];
    for(int i=0; i<timePointsSize; ++i){
        time[i] = time2minutes(timePoints[i]);
    }
    quick_sort(time, 0, timePointsSize-1);
    int min = INT_MAX;
    for(int i=0; i<timePointsSize; ++i){
        int tmp = (time[(i+1)%timePointsSize] - time[i] + 1440) % 1440;
        min = min < tmp ? min : tmp;
    }
    return min;
}

