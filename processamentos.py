from funcoes import *
from style import *


def iniciar_sistema():
    carrinho_loja = []
    limpar_tela()
    if not login_clt():
        return 
    limpar_tela()
    

    while True:
        
        menu()
        opcao = int(input("\nEscolha uma opção entre [1] [2] [3] ou [4]: "))
        print("\n")
        if opcao == 1:
            limpar_tela() 
            produto = str(input("📦 Coloque o produto no carrinho de compras: "))
            valor = float(input("💵 Valor R$: "))
            adicionar_produto(produto, valor, carrinho_loja)
            limpar_tela()
        
        elif opcao == 2:
            limpar_tela()
            total_calculado = calcular_valor_produto(carrinho_loja)
            exibir_resultado_formatado(total_calculado)
            
        elif opcao == 3:
            limpar_tela()
            todos_os_produtos_adicionados(carrinho_loja)
        elif opcao == 4:
            limpar_tela()
            print("Saindo da lojinha de periféricos do Yuri...")
            break
        else:
            limpar_tela()
            print("❌ VALOR INVALIDO! CLIQUE [1], [2], [3] ou [4]\n")