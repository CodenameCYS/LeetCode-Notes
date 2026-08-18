/*
=== 885. Boats to Save People ===

The i-th person has weight people[i], and each boat can carry a maximum weight of limit.
Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)


Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

Note:
1. 1 <= people.length <= 50000
2. 1 <= people[i] <= limit <= 30000
*/
void QuickSort(int* nums, int start, int end){
    if(start >= end){
        return;
    }
    int temp = nums[start];
    int i = start, j = end;
    while(i < j){
        while(i < j && nums[j] >= temp){
            -- j;
        }
        if(i < j){
            nums[i] = nums[j];
            ++ i;
        }
        while(i < j && nums[i] <= temp){
            ++ i;
        }
        if(i < j){
            nums[j] = nums[i];
            -- j;
        }
    }
    nums[i] = temp;
    QuickSort(nums, start, i-1);
    QuickSort(nums, i+1, end);
}

int numRescueBoats(int* people, int peopleSize, int limit) {
    QuickSort(people, 0, peopleSize-1);
    
    int num = 0;
    int i = 0, j = peopleSize-1;
    while(i < j){
        if(people[i] + people[j] <= limit){
            ++ i;
            -- j;
        }
        else{
            -- j;
        }
        ++ num;
    }
    if(i == j){
        return num + 1;
    }
    else{
        return num;
    }
}