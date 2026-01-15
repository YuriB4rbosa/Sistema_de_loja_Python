import json
import os

def salvar_dados(produtos_carrinho, nome_arquivo = "carrinho.json"):
    try:
        with open(nome_arquivo, 'w', encoding= 'utf-8') as f:
            json.dump(produtos_carrinho, f, indent=4, sort_keys= True)
            print("Carrinho salvo!")
    except IOError as e:
        print(f"ERRO {e}")

def carregar_dados(nome_arquivo = "carrinho.json"):
    if not os.path.exists(nome_arquivo):
        return []
    try:
        with open(nome_arquivo, 'r' , encoding= 'utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("ARQUIVO COMRROPIDO")
        return []


