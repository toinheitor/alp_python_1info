#include <stdio.h>

int main() {
    int codigo;
    float valor, desconto, valorFinal;

    do {
        printf("\n=== BLACK FRIDAY ===\n");
        printf("Forma de pagamento:\n");
        printf("1 - A vista (15%% de desconto)\n");
        printf("2 - Cartao de debito (10%% de desconto)\n");
        printf("3 - Cartao de credito (5%% de desconto)\n");
        printf("0 - Sair\n");
        printf("Digite a opcao: ");
        scanf("%d", &codigo);

        if (codigo == 0) {
            break;
        }

        printf("Digite o valor da venda: R$ ");
        scanf("%f", &valor);

        switch (codigo) {
            case 1:
                desconto = valor * 0.15;
                break;
            case 2:
                desconto = valor * 0.10;
                break;
            case 3:
                desconto = valor * 0.05;
                break;
            default:
                printf("Codigo de pagamento invalido!\n");
                continue;
        }

        valorFinal = valor - desconto;

        printf("Desconto: R$ %.2f\n", desconto);
        printf("Valor final a pagar: R$ %.2f\n", valorFinal);

    } while (1);

    printf("\nPrograma encerrado!\n");

    return 0;
}
