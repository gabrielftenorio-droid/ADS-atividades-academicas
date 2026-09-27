#include <stdio.h>

// Calcula o salario bruto
double calcular_salario_bruto(double valor_hora, double horas) {
    return valor_hora * horas;
}

// Calcula o desconto de 9%
double calcular_desconto(double bruto) {
    const double TAXA_DESCONTO = 0.09;
    return bruto * TAXA_DESCONTO;
}

// Calcula o salario liquido
double calcular_salario_liquido(double bruto, double desconto) {
    return bruto - desconto;
}

int main() {
    double valor_h, horas_trab;
    double salario_b, desconto_v, salario_l;

    printf("--- Calculadora Salarial ---\n");

    printf("Informe o valor da hora de trabalho (R$): ");
    scanf("%lf", &valor_h);

    printf("Informe a quantidade de horas trabalhadas no mes: ");
    scanf("%lf", &horas_trab);

    printf("\n");

    salario_b = calcular_salario_bruto(valor_h, horas_trab);
    desconto_v = calcular_desconto(salario_b);
    salario_l = calcular_salario_liquido(salario_b, desconto_v);

    printf("--- Resultados ---\n");
    printf("Salario Bruto: R$ %.2lf\n", salario_b);
    printf("Desconto (9%%): R$ %.2lf\n", desconto_v);
    printf("Salario Liquido: R$ %.2lf\n", salario_l);
    printf("------------------\n");

    return 0;
}