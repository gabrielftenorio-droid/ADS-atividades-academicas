import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Livro[] livros = new Livro[5];

        livros[0] = new Livro("Dom Casmurro", "Machado de Assis", 1899);
        livros[1] = new Livro("O Alquimista", "Paulo Coelho", 1988);
        livros[2] = new Livro("Grande Sertão: Veredas", "João Guimarães Rosa", 1956);
        livros[3] = new Livro("Ensaio Sobre a Cegueira", "José Saramago", 1995);
        livros[4] = new Livro("Vidas Secas", "Graciliano Ramos", 1938);

        System.out.print("Digite uma palavra para buscar no título: ");
        String busca = scanner.nextLine();

        boolean encontrado = false;

        System.out.println("\nResultado da busca:");

        for (Livro livro : livros) {
            if (livro.titulo.toLowerCase().contains(busca.toLowerCase())) {
                livro.exibirInformacoes();
                encontrado = true;
            }
        }

        if (!encontrado) {
            System.out.println("Nenhum livro encontrado.");
        }

        scanner.close();
    }
}