/*
=== 825. Friends Of Appropriate Ages ===

Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 
Person A will NOT friend request person B (B != A) if any of the following conditions are true:
    - age[B] <= 0.5 * age[A] + 7
    - age[B] > age[A]
    - age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.
Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.
How many total friend requests are made?

Example 1:
    Input: [16,16]
    Output: 2
    Explanation: 2 people friend request each other.
Example 2:
    Input: [16,17,18]
    Output: 2
    Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:
    Input: [20,30,100,110,120]
    Output: 
    Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
   
Notes:
    1. 1 <= ages.length <= 20000.
    2. 1 <= ages[i] <= 120.
*/
// === 40ms(34.78%) && 6.9MB(100%) === //
int numFriendRequests(int* ages, int agesSize){
    int age_counter[121] = {0};
    for(int i=0; i<agesSize; ++i){
        ++ age_counter[ages[i]];
    }
    int ans = 0;
    for(int i=15; i<=120; ++i){
        if(age_counter[i] == 0){
            continue;
        }
        int minb = (int)(0.5*i+8);
        for(int j=minb; j<i; ++j){
            ans += age_counter[i] * age_counter[j];
        }
        ans += age_counter[i] * (age_counter[i]-1);
    }
    return ans;
}