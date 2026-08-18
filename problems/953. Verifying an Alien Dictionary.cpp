/*
=== 953. Verifying an Alien Dictionary ===

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 
Note:
1. 1 <= words.length <= 100
2. 1 <= words[i].length <= 20
3. order.length == 26
4. All characters in words[i] and order are english lowercase letters.
*/
bool compareAlien(char* word1, char* word2, char* order){
    char w1, w2;
    for(int i=0; ;++i){
        w1 = word1[i];
        w2 = word2[i];
        if(w1 == '\0'){
            return true;
        }
        else if(w2 == '\0'){
            return false;
        }
        else if(w1 != w2){
            break;
        }
    }
    for(int i=0; ;++i){
        if(order[i] == w1){
            return true;
        }
        else if(order[i] == w2){
            return false;
        }
    }
}
bool isAlienSorted(char** words, int wordsSize, char* order) {
    for(int i=0; i<wordsSize-1; ++i){
        if(!compareAlien(words[i], words[i+1], order)){
            return false;
        }
    }
    return true;
}