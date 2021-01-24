#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void alphabetic(char* str, int* order){
    int len = strlen(str);
    int i, j;
    int orderCount = 0;
    for (i = 0; i < 26; i++){
        for (j = 0; j <= len; j++){
            if (str[j] - 97 == i){
                order[orderCount] = j;
                orderCount++;
            }
        }
    }
}

void removeuntill(char* str, int i){
    int len = strlen(str);
    int j;
    for (j = i + 1; j <= len; j++){
        str[j-1-i] = str[j];
    }
}

void permutate(char* str, char* sub){
    int len = strlen(str);
    int sublen = strlen(sub);
    int i, j, order[len];
    alphabetic(str,order);

    for(i = 0; i < len; i++){
        if (i > 0 && str[order[i]] == str[order[i-1]])
            continue;
        char selec = str[order[i]];
        char temp[1001];
        strncat(sub, &selec, 1);
        printf("%s\n",sub);
        strcpy(temp,str);
        removeuntill(str,order[i]);
        permutate(str,sub);
        strcpy(str,temp);
        sub[sublen] = '\0';
    }
}


int main(){
    char str[1001];
    while (scanf("%s",str) != EOF){
        char sub[1001];
        sub[0] = '\0';
        permutate(str,sub);
        printf("\n");
    }
}
