#include <stdio.h>
#include <string.h>
#include <math.h>
 
void reverse(char* str){
    int len = strlen(str);
    char temp[1001];
    strcpy(temp, str);
    int i;
    for (i = 0; i < len; i++){
        str[i] = temp[len - 1 - i];
    }
    str[len] = '\0';
}

int main() {
    int N, i;
    scanf("%d", &N);
    fflush(stdin);
    for (i = 0; i < N; i++){
        char str[1001];
        fgets(str, 1001, stdin); 
        int j = 0;
        while (str[j] != '\0'){
            char c = str[j];
            if ((c > 64 && c < 91) || (c > 96 && c < 123))
                str[j] = c + 3;
            j++;
        }
        reverse(str);
        int len = strlen(str) - 1;
        j = floor(len / 2) + 1;
        while (j < len){
            str[j] -= 1;
            j++;
        }
        printf("%s\n", str);
    }
 
    return 0;
}