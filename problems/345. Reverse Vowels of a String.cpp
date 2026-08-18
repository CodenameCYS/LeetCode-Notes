/*
=== 345. Reverse Vowels of a String ===

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
    Input: "hello"
    Output: "holle"
Example 2:
    Input: "leetcode"
    Output: "leotcede"

Note:
    - The vowels does not include the letter "y".
*/
bool isVowel(char c){
    return c=='a' || c=='e' || c=='i' || c=='o' || c=='u' || c=='A' || c=='E' || c=='I' || c=='O' || c=='U';
}
// === 8ms(66.08%) && 8MB(12.12%) === //
char* reverseVowels(char* s) {
    int len = strlen(s);
    char* ans = (char*)malloc((len+1)*sizeof(char));
    ans[len] = '\0';
    
    int st = 0, ed=len-1;
    while(st < ed){
        while(st<ed && !isVowel(s[st])){
            ans[st] = s[st];
            ++st;
        }
        while(st<ed && !isVowel(s[ed])){
            ans[ed] = s[ed];
            --ed;
        }
        if(st < ed){
            ans[st] = s[ed];
            ans[ed] = s[st];
            ++st;
            --ed;
        }
    }
    if(st == ed){
        ans[st] = s[st];
    }
    return ans;
}
// === 4ms(100%) && 7.9MB(15.15%) === //
char* reverseVowels(char* s) {
    int len = strlen(s);
    
    int st = 0, ed=len-1;
    while(st < ed){
        while(st<ed && !isVowel(s[st])){
            ++st;
        }
        while(st<ed && !isVowel(s[ed])){
            --ed;
        }
        if(st < ed){
            char temp = s[ed];
            s[ed] = s[st];
            s[st] = temp;
            ++st;
            --ed;
        }
    }
    return s;
}