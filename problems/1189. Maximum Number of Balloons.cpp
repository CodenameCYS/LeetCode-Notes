/*
=== 1189. Maximum Number of Balloons ===

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.
 
Example 1:
    Input: text = "nlaebolko"
    Output: 1
Example 2:
    Input: text = "loonbalxballpoon"
    Output: 2
Example 3:
    Input: text = "leetcode"
    Output: 0
 
Constraints:
    1. 1 <= text.length <= 10^4
    2. text consists of lower case English letters only.
*/
// === 0ms & 7.1MB === //
int maxNumberOfBalloons(char * text){
    int alphabet[26];
    for(int i=0; i<26; ++i){
        alphabet[i] = 0;
    }
    int len = strlen(text);
    for(int i=0; i<len; ++i){
        ++ alphabet[text[i]-'a'];
    }
    int ans = alphabet[0];
    ans = alphabet['b'-'a'] < ans ? alphabet['b'-'a'] : ans;
    ans = alphabet['l'-'a']/2 < ans ? alphabet['l'-'a']/2 : ans;
    ans = alphabet['n'-'a'] < ans ? alphabet['n'-'a'] : ans;
    ans = alphabet['o'-'a']/2 < ans ? alphabet['o'-'a']/2 : ans;
    return ans;
}

