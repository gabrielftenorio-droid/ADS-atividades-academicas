#include <stdio.h>

int main() {
    int numero;
    int soma_total = 0;

    printf("Digite um numero inteiro (0 para encerrar): ");
    scanf("%d", &numero);

    while (numero != 0) {
        soma_total = soma_total + numero;

        printf("Digite outro numero inteiro (0 para encerrar): ");
        scanf("%d", &numero);
    }

    printf("\nPrograma encerrado.\n");
    printf("Soma total: %d\n", soma_total);

    return 0;
}