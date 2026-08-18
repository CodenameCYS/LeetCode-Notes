/*
=== 682. Baseball Game ===

You're now a baseball game point recorder.
Given a list of strings, each string can be one of the 4 following types:
    1. Integer (one round's score): Directly represents the number of points you get in this round.
    2. "+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
    3. "D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
    4. "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.
You need to return the sum of the points you could get in all the rounds.

Example 1:
    Input: ["5","2","C","D","+"]
    Output: 30
    Explanation: 
    Round 1: You could get 5 points. The sum is: 5.
    Round 2: You could get 2 points. The sum is: 7.
    Operation 1: The round 2's data was invalid. The sum is: 5.  
    Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
    Round 4: You could get 5 + 10 = 15 points. The sum is: 30.
Example 2:
    Input: ["5","-2","4","C","D","9","+","+"]
    Output: 27
    Explanation: 
    Round 1: You could get 5 points. The sum is: 5.
    Round 2: You could get -2 points. The sum is: 3.
    Round 3: You could get 4 points. The sum is: 7.
    Operation 1: The round 3's data is invalid. The sum is: 3.  
    Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
    Round 5: You could get 9 points. The sum is: 8.
    Round 6: You could get -4 + 9 = 5 points. The sum is 13.
    Round 7: You could get 9 + 5 = 14 points. The sum is 27.

Note:
    1. The size of the input list will be between 1 and 1000.
    2. Every integer represented in the list will be between -30000 and 30000.
*/
int str2int(char* s){
    int ans = 0;
    if(s[0] != '-'){
        for(int i=0; s[i]; ++i){
            ans = ans*10 + s[i]-'0';
        }
    }
    else{
        for(int i=1; s[i]; ++i){
            ans = ans*10 - s[i]+'0';
        }
    }
    return ans;
}
// === 0ms(100%) && 5.9MB(100%) === //
int calPoints(char ** ops, int opsSize){
    int score[1001] = {0}, size=1;;
    for(int i=0; i<opsSize; ++i){
        if(ops[i][0] == 'C'){
            -- size;
        }
        else if(ops[i][0] == 'D'){
            score[size] = 2*score[size-1];
            ++ size;
        }
        else if(ops[i][0] == '+'){
            score[size] = score[size-1] + score[size-2];
            ++ size;
        }
        else{
            score[size] = str2int(ops[i]);
            ++ size;
        }
    }
    int ans = 0;
    for(int i=1; i<size; ++i){
        // printf("%d ", score[i]);
        ans += score[i];
    }
    // printf("\n");
    return ans;
}

