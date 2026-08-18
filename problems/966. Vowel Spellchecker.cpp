/*
=== 966. Vowel Spellchecker ===

Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.
For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
    Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
    Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
    Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
    Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
    Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
    Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:
    When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
    When the query matches a word up to capitlization, you should return the first such match in the wordlist.
    When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
    If the query has no matches in the wordlist, you should return the empty string.
    Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

Example 1:
    Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
 
Note:
    1. 1 <= wordlist.length <= 5000
    2. 1 <= queries.length <= 5000
    3. 1 <= wordlist[i].length <= 7
    4. 1 <= queries[i].length <= 7
    5. All strings in wordlist and queries consist only of english letters.
*/
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
// === Time Limit Exceeded === //
bool isVowel(char c){
    if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
        return true;
    }
    return false;
}
void checkspell(char** wordlist, int wordlistSize, char* query, char** ans){
    int querylen = strlen(query);
    int matchlevel = 1;
    *ans = (char*)malloc(sizeof(char));
    ans[0][0] = '\0';
    for(int i=0; i<wordlistSize; ++i){
        int wordlen = strlen(wordlist[i]);
        if(wordlen != querylen){
            continue;
        }
        bool ismatch = true;
        int level = 1;
        for(int j=0; j<wordlen; ++j){
            if(wordlist[i][j] == query[j]){
                continue;
            }
            char w = tolower(wordlist[i][j]);
            char q = tolower(query[j]);
            if(w == q){
                if(level < 2){
                    level = 2;
                }
            }
            else if(isVowel(w) && isVowel(q)){
                level = 3;
            }
            else{
                ismatch = false;
                break;
            }
        }
        if(ismatch){
            if(level == 1){
                free(*ans);
                *ans = (char*)malloc((wordlen+1)*sizeof(char));
                for(int j=0; j<wordlen; ++j){
                    ans[0][j] = wordlist[i][j];
                }
                ans[0][wordlen] = '\0';
                return;
            }
            else if(level == 2){
                if(matchlevel != 2){
                    free(*ans);
                    *ans = (char*)malloc((wordlen+1)*sizeof(char));
                    for(int j=0; j<wordlen; ++j){
                        ans[0][j] = wordlist[i][j];
                    }
                    ans[0][wordlen] = '\0';
                    matchlevel = 2;
                }
            }
            else{ // level == 3
                if(matchlevel == 1){
                    free(*ans);
                    *ans = (char*)malloc((wordlen+1)*sizeof(char));
                    for(int j=0; j<wordlen; ++j){
                        ans[0][j] = wordlist[i][j];
                    }
                    ans[0][wordlen] = '\0';
                    matchlevel = 3;
                }
            }
        }
    }
}
char** spellchecker(char** wordlist, int wordlistSize, char** queries, int queriesSize, int* returnSize) {
    *returnSize = queriesSize;
    char** ans = (char**)malloc(queriesSize*sizeof(char*));
    for(int i=0; i<queriesSize; ++i){
        checkspell(wordlist, wordlistSize, queries[i], &ans[i]);
    }
    return ans;
}