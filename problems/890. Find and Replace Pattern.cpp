/*
=== 890. Find and Replace Pattern ===

You have a list of words and a pattern, and you want to know which words in words matches the pattern.
A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)
Return a list of the words in words that match the given pattern. 
You may return the answer in any order.

Example 1:
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
 
Note:
1. 1 <= words.length <= 50
2. 1 <= pattern.length = words[i].length <= 20
*/
# include <stdlib.h>
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool compare(char* word, char* pattern){
    int tag[20];
    for(int i=0; i<20; ++i){
        if(pattern[i] == '\0'){
            tag[i] = -1;
            break;
        }
        else{
            tag[i] = 0;
        }
    }
    int alphabet[26];
    for(int i=0; i<26; ++i){
        alphabet[i] = 0;
    }
    for(int i=0; pattern[i]!='\0'; ++i){
        if(tag[i] == 1){
            continue;
        }
        for(int j=i+1; pattern[j]!='\0'; ++j){
            if(pattern[i] == pattern[j]){
                if(word[i] == word[j] && alphabet[word[i]-'a'] == 0){
                    tag[j] = 1;
                }
                else{
                    return false;
                }
            }
        }
        if(alphabet[word[i]-'a'] == 0){
            alphabet[word[i]-'a'] = 1;
            tag[i] = 1;
        }
        else{
            return false;
        }
    }
    return true;
}

char** findAndReplacePattern(char** words, int wordsSize, char* pattern, int* returnSize) {
    char** ans = 0;
    *returnSize = 0;
    
    for(int i=0; i<wordsSize; ++i){
        if(compare(words[i], pattern)){
            if(*returnSize == 0){
                ans = (char**)malloc(sizeof(char*));
            }
            else{
                ans = (char**)realloc(ans, (*returnSize + 1)*sizeof(char*));
            }
            ans[*returnSize] = (char*)malloc(20*sizeof(char));
            int j=0;
            while(words[i][j]!='\0'){
                ans[*returnSize][j] = words[i][j];
                ++ j;
            }
            ans[*returnSize][j] = '\0';
            ++ *returnSize;
        }
    }
    
    return ans;
}