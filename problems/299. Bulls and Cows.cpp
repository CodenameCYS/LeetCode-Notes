/*
=== 299. Bulls and Cows ===

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.
Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 
Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:
    Input: secret = "1807", guess = "7810"
    Output: "1A3B"
- Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:
    Input: secret = "1123", guess = "0111"
    Output: "1A1B"
- Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

Note:
- You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
*/
// === 28ms(68.18) & 7.1MB(20%) === //
char* str2int(int n){
    if(n==0){
        char* ans = (char*)malloc(2*sizeof(char));
        ans[0] = '0';
        ans[1] = '\0';
        return ans;
    }
    int len = (int)(log(n)/log(10)) + 1;
    char* ans = (char*)malloc((len+1)*sizeof(char));
    ans[len] = '\0';
    --len;
    while(n > 0){
        ans[len] = n % 10 + '0';
        n /= 10;
        --len;
    }
    return ans;
}
char* getHint(char* secret, char* guess) {
    int len = strlen(secret);
    int sstate[len], gstate[len];
    int acount=0, bcount=0;
    for(int i=0; i<len; ++i){
        if(secret[i] == guess[i]){
            ++acount;
            sstate[i] = 1;
            gstate[i] = 1;
        }
        else{
            sstate[i] = 0;
            gstate[i] = 0;
        }
    }
    for(int i=0; i<len; ++i){
        if(sstate[i] == 1){
            continue;
        }
        for(int j=0; j<len; ++j){
            if(gstate[j] == 1){
                continue;
            }
            if(guess[j] == secret[i]){
                ++bcount;
                gstate[j] = 1;
                break;
            }
        }
    }
    
    char* bull = str2int(acount);
    char* cow = str2int(bcount);
    char* ans = (char*)malloc((strlen(bull)+strlen(cow)+3)*sizeof(char));
    int count = 0;
    for(int i=0; i<strlen(bull); ++i){
        ans[count] = bull[i];
        ++count;
    }
    ans[count] = 'A';
    ++count;
    for(int i=0; i<strlen(cow); ++i){
        ans[count] = cow[i];
        ++count;
    }
    ans[count] = 'B';
    ++count;
    ans[count] = '\0';
    free(bull);
    free(cow);
    return ans;
}
// === 28ms(68.18) & 7.1MB(20%) === // *注意sprintf()函数
char* getHint(char* secret, char* guess) {
    int len = strlen(secret);
    int sstate[len], gstate[len];
    int acount=0, bcount=0;
    for(int i=0; i<len; ++i){
        if(secret[i] == guess[i]){
            ++acount;
            sstate[i] = 1;
            gstate[i] = 1;
        }
        else{
            sstate[i] = 0;
            gstate[i] = 0;
        }
    }
    for(int i=0; i<len; ++i){
        if(sstate[i] == 1){
            continue;
        }
        for(int j=0; j<len; ++j){
            if(gstate[j] == 1){
                continue;
            }
            if(guess[j] == secret[i]){
                ++bcount;
                gstate[j] = 1;
                break;
            }
        }
    }
    
    char* str=(char*)malloc(sizeof(char)*50);
    sprintf(str, "%dA%dB", acount, bcount);
    return str;
}