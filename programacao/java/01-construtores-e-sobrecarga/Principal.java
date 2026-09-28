public class Principal {
    public static void main(String[] args) {
        Produto produto1 = new Produto();
        Produto produto2 = new Produto("Notebook", 3500.00);
        Produto produto3 = new Produto("Mouse", 120.00);

        produto1.exibirDados();
        produto2.exibirDados();
        produto3.exibirDados();

        Produto.exibirQuantidadeTotal();
    }
}