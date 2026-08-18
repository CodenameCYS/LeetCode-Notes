/*
=== 318. Maximum Product of Word Lengths ===

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
    Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
    Output: 16 
    Explanation: The two words can be "abcw", "xtfn".
Example 2:
    Input: ["a","ab","abc","d","cd","bcd","abcd"]
    Output: 4 
    Explanation: The two words can be "ab", "cd".
Example 3:
    Input: ["a","aa","aaa","aaaa"]
    Output: 0 
    Explanation: No such pair of words.
*/
// === 1712ms(5.71%) & 8.8MB(100%) === //
bool hasCommonLetter(char* str1, char* str2){
    int state[26];
    for(int i=0; i<26; ++i){
        state[i] = 0;
    }
    
    for(int i=0; i<strlen(str1); ++i){
        state[str1[i]-'a'] = 1;
    }
    for(int i=0; i<strlen(str2); ++i){
        if(state[str2[i]-'a'] == 1){
            return true;
        }
    }
    return false;
}
int maxProduct(char** words, int wordsSize) {
    int ans = 0;
    for(int i=0; i<wordsSize-1; ++i){
        for(int j=i+1; j<wordsSize; ++j){
            if(!hasCommonLetter(words[i], words[j])){
                int temp = strlen(words[i]) * strlen(words[j]);
                ans = ans > temp ? ans : temp;
            }
        }
    }
    return ans;
}