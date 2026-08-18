/*
=== 423. Reconstruct Original Digits from English ===

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
    1. Input contains only lowercase English letters.
    2. Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
    3. Input length is less than 50,000.

Example 1:
    Input: "owoztneoer"
    Output: "012"
Example 2:
    Input: "fviefuro"
    Output: "45"
*/
// === 4ms(100%) && 7.9MB(100%) === //
char * originalDigits(char * s){
    char* number[10] = {"zero", "one", "two", "three", "four", 
                        "five", "six", "seven", "eight", "nine"};
    int order[10] = {6, 7, 5, 4, 2, 0, 8, 3, 1, 9};
    char key[10] = {'x', 's', 'v', 'u', 'w', 'z', 'g', 't', 'o', 'i'};
    
    int alphabet[26] = {0};
    for(int i=0; s[i]; ++i){
        ++ alphabet[s[i] - 'a'];
    }
    // for(int i=0; i<26; ++i){
    //     printf("%c:%d  ", 'a' + i, alphabet[i]);
    // }
    // printf("\n");
    
    int count[10] = {0};
    for(int i=0; i<10; ++i){
        int n = order[i];
        char k = key[i];
        char* num = number[n];
        // printf("%d -> %d <-> %s (%c)\n", i, n, num, k);
        count[n] = alphabet[k-'a'];
        for(int j=0; num[j]; ++j){
            alphabet[num[j] - 'a'] -= count[n];
        }
    }
    // for(int i=0; i<10; ++i){
    //     printf("%d:%d  ", i, count[i]);
    // }
    // printf("\n");
    
    char* ans = (char*)malloc(20000*sizeof(char));
    int index = 0;
    for(int i=0; i<10; ++i){
        for(int j=0; j<count[i]; ++j){
            ans[index] = '0' + i;
            ++ index;
        }
    }
    ans[index] = '\0';
    return ans;
}

