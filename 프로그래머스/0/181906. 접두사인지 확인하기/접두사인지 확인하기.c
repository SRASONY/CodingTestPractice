#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* my_string, const char* is_prefix) {
    int answer = 0;
    if (strlen(my_string)>=strlen(is_prefix)){
        for(int i=0; i<strlen(is_prefix); i++){
            if(is_prefix[i]==my_string[i]){
                answer = 1;
            }
            else{
                answer = 0;
                return answer;
            }
        }
    }
    return answer;
}