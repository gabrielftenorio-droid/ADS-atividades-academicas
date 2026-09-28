public class Produto {
    private String nome;
    private double preco;
    private static int quantidadeTotal = 0;

    public Produto() {
        quantidadeTotal++;
    }

    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
        quantidadeTotal++;
    }

    public void exibirDados() {
        System.out.println("Nome: " + nome);
        System.out.println("Preço: R$ " + preco);
    }

    public static void exibirQuantidadeTotal() {
        System.out.println("Quantidade total de produtos: " + quantidadeTotal);
    }
}