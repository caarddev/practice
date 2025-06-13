#include <stdio.h>
#include <stdlib.h>

int main(){

    int num, cont;
    printf("Digite um número: \n");
    scanf("%d", &num);
    for (cont=1; cont<=20; cont=cont+1)
    {
        printf("\n Num: %d", num);
    }
    return 0;
}