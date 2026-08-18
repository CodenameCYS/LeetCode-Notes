/*
=== 1154. Day of the Year ===

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Example 1:
    Input: date = "2019-01-09"
    Output: 9
    - Explanation: Given date is the 9th day of the year in 2019.
Example 2:
    Input: date = "2019-02-10"
    Output: 41
Example 3:
    Input: date = "2003-03-01"
    Output: 60
Example 4:
    Input: date = "2004-03-01"
    Output: 61
 
Constraints:
    1. date.length == 10
    2. date[4] == date[7] == '-', and all other date[i]'s are digits
    3. date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
*/
bool is_bissextile(int year){
    if(year % 4 != 0){
        return false;
    }
    else if(year % 100 == 0 && year % 400 != 0){
        return false;
    }
    return true;
}

int char2int(char* date, int len){
    int ans = 0;
    for(int i=0; i<len; ++i){
        ans = ans*10 + date[i]-'0';
    }
    return ans;
}
// === 4ms && 6.6MB === //
int dayOfYear(char * date){
    int day_num[13] = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365};
    int year = char2int(date, 4);
    int month = char2int(&date[5], 2);
    int day = char2int(&date[8], 2);
    int ans = day_num[month-1] + day;
    if(is_bissextile(year) && month > 2){
        ++ ans;
    }
    return ans;
}
// === best answer === //
int dayOfYear(char * date){
    int days[] = {0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};
    int y, m , d;
    sscanf(date, "%d-%d-%d", &y, &m, &d);
    int leap = 0;
    if(m > 2 && (y % 400 == 0 || (y % 4 == 0 && y % 100 != 0)))leap++;
    return days[m] + d + leap;
}
