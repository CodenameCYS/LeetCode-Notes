/*
=== 551. Student Attendance Record I ===

You are given a string representing an attendance record for a student. The record only contains the following three characters:
    1. 'A' : Absent.
    2. 'L' : Late.
    3. 'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
You need to return whether the student could be rewarded according to his attendance record.

Example 1:
    Input: "PPALLP"
    Output: True
Example 2:
    Input: "PPALLL"
    Output: False
*/
// === 0ms(100%) && 6.6MB(100%) === //
bool checkRecord(char * s){
    int acount=0, lcount=0;
    for(int i=0; s[i]; ++i){
        if(s[i] == 'A'){
            ++ acount;
            lcount = 0;
        }
        else if(s[i] == 'L'){
            ++ lcount;
            if(lcount > 2){
                return false;
            }
        }
        else{
            lcount = 0;
        }
    }
    return acount <= 1 && lcount <= 2;
}

