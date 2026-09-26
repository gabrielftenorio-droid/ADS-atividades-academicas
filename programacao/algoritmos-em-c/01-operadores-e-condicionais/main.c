#include <stdio.h>

int main() {
    int num1, num2, num3;

    printf("Digite o primeiro numero: ");
    scanf("%d", &num1);

    printf("Digite o segundo numero: ");
    scanf("%d", &num2);

    printf("Digite o terceiro numero: ");
    scanf("%d", &num3);

    printf("\n--- Operacoes Aritmeticas ---\n");
    printf("Soma: %d\n", num1 + num2 + num3);
    printf("Subtracao: %d\n", num1 - num2 - num3);
    printf("Multiplicacao: %d\n", num1 * num2 * num3);

    if (num2 != 0 && num3 != 0) {
        printf("Divisao: %.2f\n",
               (float) num1 / num2 / num3);
    } else {
        printf("Divisao nao pode ser realizada: divisao por zero.\n");
    }

    printf("\n--- Operadores Relacionais ---\n");

    if (num1 > num2) {
        printf("O primeiro numero e maior que o segundo: Verdadeiro\n");
    } else {
        printf("O primeiro numero e maior que o segundo: Falso\n");
    }

    if (num2 < num3) {
        printf("O segundo numero e menor que o terceiro: Verdadeiro\n");
    } else {
        printf("O segundo numero e menor que o terceiro: Falso\n");
    }

    printf("\n--- Operadores Logicos ---\n");

    if (num1 > 0 && num2 % 2 == 0) {
        printf("O primeiro numero e positivo e o segundo e par: Verdadeiro\n");
    } else {
        printf("O primeiro numero e positivo e o segundo e par: Falso\n");
    }

    return 0;
}