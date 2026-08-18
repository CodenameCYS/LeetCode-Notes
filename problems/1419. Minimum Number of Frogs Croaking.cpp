/*
=== 1419. Minimum Number of Frogs Croaking ===

Given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple “croak” are mixed. Return the minimum number of different frogs to finish all the croak in the given string.
A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of valid "croak" return -1.

Example 1:
    Input: croakOfFrogs = "croakcroak"
    Output: 1 
    Explanation: One frog yelling "croak" twice.
Example 2:
    Input: croakOfFrogs = "crcoakroak"
    Output: 2 
    Explanation: The minimum number of frogs is two. 
    The first frog could yell "crcoakroak".
    The second frog could yell later "crcoakroak".
Example 3:
    Input: croakOfFrogs = "croakcrook"
    Output: -1
    Explanation: The given string is an invalid combination of "croak" from different frogs.
Example 4:
    Input: croakOfFrogs = "croakcroa"
    Output: -1
 
Constraints:
    1. 1 <= croakOfFrogs.length <= 10^5
    2. All characters in the string are: 'c', 'r', 'o', 'a' or 'k'.
*/
// === 8ms && 6.2MB === //
int minNumberOfFrogs(char * croakOfFrogs){
    int c = 0, r = 0, o = 0, a = 0, k = 0;
    for(int i=0; croakOfFrogs[i]; ++i){
        if(croakOfFrogs[i] == 'c'){
            ++ c;
            k = k - 1 > 0 ? k - 1 : 0;
        }
        else if(croakOfFrogs[i] == 'r'){
            ++ r;
            -- c;
            if(c < 0){
                return -1;
            }
        }
        else if(croakOfFrogs[i] == 'o'){
            ++ o;
            -- r;
            if(r < 0){
                return -1;
            }
        }
        else if(croakOfFrogs[i] == 'a'){
            ++ a;
            -- o;
            if(o < 0){
                return -1;
            }
        }
        else if(croakOfFrogs[i] == 'k'){
            ++ k;
            -- a;
            if(a < 0){
                return -1;
            }
        }
    }
    if(c || r || o || a){
        return -1;
    }
    return k;
}