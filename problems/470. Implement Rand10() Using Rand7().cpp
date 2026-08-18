/*
=== 470. Implement Rand10() Using Rand7() ===

Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.
Do NOT use system's Math.random().

Example 1:
    Input: 1
    Output: [7]
Example 2:
    Input: 2
    Output: [8,4]
Example 3:
    Input: 3
    Output: [8,1,10]
 
Note:
    1. rand7 is predefined.
    2. Each testcase has one argument: n, the number of times that rand10 is called.
 
Follow up:
    1. What is the expected value for the number of calls to rand7() function?
    2. Could you minimize the number of calls to rand7()?
*/
// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7
int my_rand(int* candidates, int size){
    int left[size];
    int flag = 0;
    int max = 0;
    for(int i=0; i<size; ++i){
        int tmp = rand7();
        if(tmp > max){
            max = tmp;
            left[0] = candidates[i];
            flag = 1;
        }
        else if(tmp == max){
            left[flag] = candidates[i];
            ++ flag;
        }
    }
    if(flag == 1){
        return left[0];
    }
    else{
        return my_rand(left, flag);
    }
}
// === 76ms(12.5%) && 12.7MB(100%) === //
int rand10() {
    int candidates[10] = {1,2,3,4,5,6,7,8,9,10};
    return my_rand(candidates, 10);
}
// ======================================================================== //
int rand2(){
    int seed = rand7();
    while(seed == 7){
        seed = rand7();
    }
    return seed % 2 + 1;
}
int rand5(){
    int seed = rand7();
    while(seed > 5){
        seed = rand7();
    }
    return seed;
}
// === 56ms(100%) && 11.2MB(100%) === //
int rand10() {
    if(rand2() == 1){
        return rand5();
    }
    else{
        return 5 + rand5();
    }
}
// ======================================================================== //
int rand2(){
    int seed = rand7();
    while(seed == 7){
        seed = rand7();
    }
    return seed % 2 + 1;
}
int rand5(){
    int seed = rand7();
    while(seed > 5){
        seed = rand7();
    }
    return seed;
}
// === 56ms(100%) && 11.2MB(100%) === //
int rand10() {
    int ans = 0;
    for(int i=0; i<10; ++i){
        ans += i+rand7();
    }
    return ans % 10 + 1;
}