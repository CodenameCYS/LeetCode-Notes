/*
=== 1239. Maximum Length of a Concatenated String with Unique Characters ===

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.
Return the maximum possible length of s.
 
Example 1:
    Input: arr = ["un","iq","ue"]
    Output: 4
    - Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
    Maximum length is 4.
Example 2:
    Input: arr = ["cha","r","act","ers"]
    Output: 6
    - Explanation: Possible solutions are "chaers" and "acters".
Example 3:
    Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
    Output: 26
 
Constraints:
    1. 1 <= arr.length <= 16
    2. 1 <= arr[i].length <= 26
    3. arr[i] contains only lower case English letters.
*/
int my_max_len(int i, int length, char** arr, int arrSize, bool* state){
    if(i == arrSize){
        return length;
    }
    int l1 = my_max_len(i+1, length, arr, arrSize, state);
    bool new_state[26], use = true;
    for(int j=0; j<26; ++j){
        new_state[j] = state[j];
    }
    int len = strlen(arr[i]);
    for(int j=0; j<len; ++j){
        if(!new_state[arr[i][j] - 'a']){
            new_state[arr[i][j] - 'a'] = true;
        }
        else{
            use = false;
            break;
        }
    }
    int l2 = 0;
    if(use){
        l2 = my_max_len(i+1, length + len, arr, arrSize, new_state);
    }
    return l1 > l2 ? l1 : l2;
}
// === 12ms & 7MB === //
int maxLength(char ** arr, int arrSize){
    bool state[26];
    for(int i=0; i<26; ++i){
        state[i] = false;
    }
    return my_max_len(0, 0, arr, arrSize, state);
}

