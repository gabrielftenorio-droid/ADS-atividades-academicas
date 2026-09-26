#include <stdio.h>

int main() {
    int vendas_diarias[5];
    int soma_total = 0;
    int i;

    printf("--- Registro de Vendas Diarias ---\n");

    for (i = 0; i < 5; i++) {
        printf("Digite o valor das vendas do dia %d: ", i + 1);
        scanf("%d", &vendas_diarias[i]);
    }

    printf("\n--- Vendas Registradas ---\n");

    for (i = 0; i < 5; i++) {
        printf("Dia %d: %d\n", i + 1, vendas_diarias[i]);
        soma_total += vendas_diarias[i];
    }

    printf("\nTotal de vendas no periodo: %d\n", soma_total);

    return 0;
}