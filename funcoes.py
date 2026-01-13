def adicionar_produto(qual_produto, valor_produto, lista_estoque):
    carrinho = {
        "PRODUTO:": qual_produto,
        "VALOR R$:": valor_produto
    }

    lista_estoque.append(carrinho)

def calcular_valor_produto(lista_estoque):
    total = 0 
    for item in lista_estoque:
        total += item["VALOR R$:"]
    return total

def todos_os_produtos_adicionados(total_itens):
    if len(total_itens)== 0:
        print("Nenhum produto foi adcionado!\n")
    else:
        for item in total_itens:
            print("PRODUTO:", item["PRODUTO:"])
            print("VALOR R$ ", item["VALOR R$:"])
            print()

def senha(usuario_digitado, senha_digitada):
    fixo_lojinha = {
    "user": "adminloja",
    "senha": "lojinha@123"
    }
    if usuario_digitado == fixo_lojinha["user"] and senha_digitada == fixo_lojinha["senha"]:
        return True
    else:
        return False 


    

