public class Principal {
    public static void main(String[] args) {
        Soma soma = new Soma();
        Divisao divisao = new Divisao();

        try {
            System.out.println("Soma de 10 + 5:");
            System.out.println(soma.calcular(10, 5));

            System.out.println("Divisão de 10 / 2:");
            System.out.println(divisao.calcular(10, 2));

            System.out.println("Tentativa de divisão de 10 / 0:");
            System.out.println(divisao.calcular(10, 0));

        } catch (DivisaoPorZeroException e) {
            System.out.println("Erro capturado: " + e.getMessage());
        }
    }
}