/*
=== 1002. Find Common Characters ===

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order.

Example 1:
    Input: ["bella","label","roller"]
    Output: ["e","l","l"]
Example 2:
    Input: ["cool","lock","cook"]
    Output: ["c","o"]
 
Note:
    1. 1 <= A.length <= 100
    2. 1 <= A[i].length <= 100
    3. A[i][j] is a lowercase letter
*/

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
// === 8ms & 7.9MB === //
void update(char* str, int* record){
    int temp_record[26];
    for(int i=0; i<26; ++i){
        temp_record[i] = 0;
    }
    for(int i=0; str[i]!='\0'; ++i){
        ++ temp_record[str[i]-'a'];
    }
    for(int i=0; i<26; ++i){
        record[i] = (record[i] == -1 || temp_record[i] < record[i]) ? temp_record[i] : record[i];
    }
}
char** commonChars(char** A, int ASize, int* returnSize) {
    int record[26];
    for(int i=0; i<26; i++){
        record[i] = -1;
    }
    for(int i=0; i<ASize; ++i){
        update(A[i], record);
    }
    *returnSize = 0;
    for(int i=0; i<26; ++i){
        *returnSize += record[i];
    }
    char** ans = (char**)malloc(*returnSize * sizeof(char*));
    int count = 0;
    for(int i=0; i<26; ++i){
        for(int j=0; j<record[i]; ++j){
            ans[count] = (char*)malloc(2*sizeof(char));
            ans[count][0] = 'a' + i;
            ans[count][1] = '\0';
            ++ count;
        }
    }
    return ans;
}