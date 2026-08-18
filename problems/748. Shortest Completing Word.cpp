/*
=== 748. Shortest Completing Word ===

Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. Such a word is said to complete the given string licensePlate
Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.
It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.
The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.

Example 1:
    Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
    Output: "steps"
    Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
    Note that the answer is not "step", because the letter "s" must occur in the word twice.
    Also note that we ignored case for the purposes of comparing whether a letter exists in the word.
Example 2:
    Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
    Output: "pest"
    Explanation: There are 3 smallest length words that contains the letters "s".
    We return the one that occurred first.

Note:
    1. licensePlate will be a string with length in range [1, 7].
    2. licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
    3. words will have a length in the range [10, 1000].
    4. Every words[i] will consist of lowercase letters, and have length in range [1, 15].
*/
bool match(char* word, int* alphabet){
    int w_alphabet[26] = {0};
    for(int i=0; word[i]; ++i){
        ++ w_alphabet[word[i]-'a'];
    }
    for(int i=0; i<26; ++i){
        if(w_alphabet[i] < alphabet[i]){
            return false;
        }
    }
    return true;
}
// === 8ms(100%) && 6.1MB(100%) === //
char * shortestCompletingWord(char * licensePlate, char ** words, int wordsSize){
    int alphabet[26] = {0};
    for(int i=0; licensePlate[i]; ++i){
        if(licensePlate[i] >= 'a' && licensePlate[i] <= 'z'){
            ++ alphabet[licensePlate[i]-'a'];
        }
        else if(licensePlate[i] >= 'A' && licensePlate[i] <= 'Z'){
            ++ alphabet[licensePlate[i]-'A'];
        }
    }
    
    int len = INT_MAX;
    char* ans = "";
    for(int i=0; i<wordsSize; ++i){
        if(strlen(words[i]) < len && match(words[i], alphabet)){
            ans = words[i];
            len = strlen(ans);
        }
    }
    return ans;
}

