/*
=== 792. Number of Matching Subsequences ===
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

Note:
All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
*/
# include <stdio.h>
# include <stdlib.h>
# include <time.h>

bool isSubseq(char* s, char* word);
int numMatchingSubseq(char* S, char** words, int wordsSize);

int main(){

    system("pause");
    return 1;
}

/*
// === ver 0.0 -- interSubSeq === //
bool isSubseq(char* s, char* word){
    int i = 0;
    while(s[i] != '\0'){
        if(s[i] != word[0]){
            ++i;
        }
        else{
            int j = 1, gap = 1;
            while(word[j] != '\0' && s[i+j] == word[j]){
                ++j;
                if(word[j] == word[0]){
                    gap == j;
                }
            }
            if(word[j] == '\0'){
                return true;
            }
            else{
                i += gap;
            }
        }
    }
    return false;
}
*/
/*
// === ver 1.0 -- time limit exceeded === //
bool isSubseq(char* s, char* word){
    if(word[0] == '\0'){
        return true;
    }
    
    int i = 0;
    while(s[i] != '\0'){
        if(s[i] == word[0] && isSubseq(&s[i+1], &word[1])){
            return true;
        }
        else{
            ++i;
        }
    }
    return false;
}
*/
bool isSubseq(char* s, char* word){
    return false;
}

int numMatchingSubseq(char* S, char** words, int wordsSize) {
    int ans=0;
    
    for(int i=0; i<wordsSize; ++i){
        if(isSubseq(S, words[i])){
            ++ ans;
        }
    }
    
    return ans;
}