from funcoes import *
import os 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def login_clt():
    tentativas = 3
    
    while tentativas > 0:
        limpar_tela()
        print(f"--- LOGIN (Tentativas restantes: {tentativas}) ---")
        usuario = input("Usuário: ")
        passw = input("Senha: ")
        
        
        if senha(usuario, passw):
            print("\n✅ Acesso concedido! Bem-vindo.")
            print("╔═══════════════════════════════════════╗")
            print("║  Pressione Enter para entrar na loja  ║")
            print("╚═══════════════════════════════════════╝")
            input()
            return True
        else:
            tentativas -= 1
            print(f"\n❌ Usuário ou senha incorretos!")
            if tentativas > 0:
                input(f"Tente novamente... (Restam {tentativas})")
    
    print("\n🚫 Número de tentativas excedido. Sistema bloqueado.")
    return False


  
def menu():
    
    print("╔══════════════════════════════════════╗")
    print("║         📦 MENU DE COMPRAS           ║")
    print("╠══════════════════════════════════════╣")
    print("║                                      ║")
    print("║  [1] ➕ ADICIONAR AO CARRINHO        ║")
    print("║  [2] 🧮 CALCULAR COMPRAS             ║")
    print("║  [3] 🛒 CARRINHO                     ║")
    print("║  [4] ❌ SAIR DA LOJA                 ║")
    print("║                                      ║")
    print("╚══════════════════════════════════════╝")
    

def exibir_resultado_formatado(valor):
    print('=' *30)
    print(f"VALOR TOTAL: R$ {valor}")
    print('=' *30)