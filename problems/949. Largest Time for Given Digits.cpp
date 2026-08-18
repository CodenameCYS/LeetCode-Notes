/*
=== 949. Largest Time for Given Digits ===

Given an array of 4 digits, return the largest 24 hour time that can be made.
The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:
Input: [1,2,3,4]
Output: "23:41"

Example 2:
Input: [5,5,5,5]
Output: ""
 
Note:
1. A.length == 4
2. 0 <= A[i] <= 9
*/
char* largestTimeFromDigits(int* A, int ASize) {
    int seq[24][4];
    int state[4] = {0,0,0,0};
    int count = 0;
    int temp[4] = {0,0,0,0};
    for(int i1=0; i1<ASize; ++i1){
        temp[0] = A[i1];
        state[i1] = 1;
        for(int i2=0; i2<ASize; ++i2){
            if(state[i2] == 1){
                continue;
            }
            temp[1] = A[i2];
            state[i2] = 1;
            for(int i3=0; i3<ASize; ++i3){
                if(state[i3] == 1){
                    continue;
                }
                temp[2] = A[i3];
                state[i3] = 1;
                for(int i4=0; i4<ASize; ++i4){
                    if(state[i4] == 1){
                        continue;
                    }
                    temp[3] = A[i4];
                    for(int i=0; i<4; ++i){
                        seq[count][i] = temp[i];
                    }
                    ++ count;
                }
                state[i3] = 0;
            }
            state[i2] = 0;
        }
        state[i1] = 0;
    }

    int max[4] = {-1,-1,-1,-1};
    for(int i=0; i<24; ++i){
        if(10*seq[i][0] + seq[i][1] < 24 && 10*seq[i][2] + seq[i][3] < 60){
            if(10*seq[i][0] + seq[i][1] > 10*max[0] + max[1] || (10*seq[i][0] + seq[i][1] == 10*max[0] + max[1] && 10*seq[i][2] + seq[i][3] >= 10*max[2] + max[3])){
                for(int j=0; j<ASize; ++j){
                    max[j] = seq[i][j];
                }
            }
        }
    }
    
    if(max[0] < 0){
        char* ans = (char*)malloc(sizeof(char));
        *ans = '\0';
        return ans;
    }
    else{
        char* ans = (char*)malloc(6*sizeof(char));
        ans[2] = ':';
        ans[5] = '\0';
        ans[0] = max[0] + 48;
        ans[1] = max[1] + 48;
        ans[3] = max[2] + 48;
        ans[4] = max[3] + 48;
        return ans;
    }
}