#include <stdio.h>
#include <string.h>

int draw(int n, int m, int matrix[n][m], int r, int c){
    int contl, contc; 
    int aux[n][m];
    memset(aux,0,sizeof(aux));
    int contDraw = 0;
    for (contc = 0; contc < m - c + 1; contc++){
        for (contl = 0; contl < n - r + 1; contl++){
            int figl, figc;
            if (matrix[contl][contc] != aux[contl][contc]){
                for (figc = 0; figc < c; figc++)
                    for (figl = 0; figl < r; figl++)
                        aux[contl + figl][contc + figc] = !aux[contl + figl][contc + figc];
                contDraw ++;
            }
        }
    }
    for (contl = 0; contl < n; contl++)
        for (contc = 0; contc < m; contc++)
            if (aux[contl][contc] != matrix[contl][contc])
                return -1;
    return contDraw;
}

int main(){
    int n, m, r, c;
    scanf("%d %d %d %d", &n, &m, &r, &c);
    while (n != 0 || m != 0 || r != 0 || c != 0){
        int matrix[n][m];
        int contl, contc;
        memset(matrix,0,sizeof(matrix));
        for (contl = 0; contl < n; contl++){
            char aux[m];
            scanf("%s", &aux);
            for (contc = 0; contc < m; contc++)
                matrix[contl][contc] = (int)aux[contc] - 48;
        }
        printf("%d\n", draw(n, m, matrix, r, c));
        scanf("%d %d %d %d", &n, &m, &r, &c);
    } 

    return 0;
}