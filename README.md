🛒 Sistema de Carrinho de Compras - Lojinha de Periféricos 
Um sistema simples e interativo de carrinho de compras desenvolvido em Python, com autenticação de usuário e interface no terminal.

📁 Estrutura do Projeto
text
projeto_lojinha/
├── main.py              # Arquivo principal que inicia o sistema
├── funcoes.py           # Funções principais do sistema
├── processamentos.py    # Funções de processamento (limpeza, login, menus)
├── style.py             # Funções de formatação e exibição visual
└── README.md            # Este arquivo
🚀 Funcionalidades
🔐 Sistema de Login Seguro
Usuário padrão: adminloja

Senha padrão: lojinha@123

3 tentativas de login antes do bloqueio

Interface limpa e com mensagens de erro claras

🛍️ Sistema de Carrinho
Adicionar produtos com nome e valor

Calcular total das compras automaticamente

Visualizar todos os produtos adicionados

Validação para carrinho vazio

🎨 Interface Amigável
Menus formatados com bordas visuais

Limpeza automática da tela entre operações

Ícones e emojis para melhor experiência

Mensagens de confirmação e erro claras

📋 Menu Principal
text
╔══════════════════════════════════════╗
║         📦 MENU DE COMPRAS           ║
╠══════════════════════════════════════╣
║                                      ║
║  [1] ➕ ADICIONAR AO CARRINHO        ║
║  [2] 🧮 CALCULAR COMPRAS             ║
║  [3] 🛒 CARRINHO                     ║
║  [4] ❌ SAIR DA LOJA                 ║
║                                      ║
╚══════════════════════════════════════╝
🛠️ Como Executar
Pré-requisitos:

Python 3.x instalado

Sistema operacional Windows, Linux ou macOS

Execução:

bash
python main.py
Credenciais de acesso:

text
Usuário: adminloja
Senha: lojinha@123
📦 Funcionalidades Detalhadas
1. Adicionar Produto
Solicita nome do produto

Solicita valor em R$

Adiciona ao carrinho como dicionário

Limpa a tela após adição

2. Calcular Total
Soma todos os valores dos produtos

Exibe resultado formatado com bordas

Formato: VALOR TOTAL: R$ X.XX

3. Ver Carrinho
Lista todos os produtos adicionados

Mostra nome e valor de cada item

Mensagem especial para carrinho vazio

4. Sair do Sistema
Mensagem de despedida personalizada

Encerra o programa corretamente

🔧 Módulos e Funções
funcoes.py
adicionar_produto(): Adiciona produto ao carrinho

calcular_valor_produto(): Calcula valor total

todos_os_produtos_adicionados(): Lista todos os produtos

senha(): Valida credenciais de login

processamentos.py
limpar_tela(): Limpa console (multiplataforma)

login_clt(): Gerencia sistema de login

menu(): Exibe menu principal

exibir_resultado_formatado(): Formata saída de valores

style.py
Funções de formatação visual

Personalização da experiência no terminal

💾 Estrutura de Dados
Produto no Carrinho
python
produto = {
    "PRODUTO:": "Nome do Produto",
    "VALOR R$:": 99.90
}
Carrinho
Lista de dicionários

Cada item representa um produto

Mantém ordem de inserção

🛡️ Segurança
Credenciais fixas para simplicidade (em produção, usar banco de dados)

Limite de tentativas para prevenir ataques de força bruta

Validação completa de entrada do usuário

🎯 Possíveis Melhorias Futuras
Persistência de dados (salvar em arquivo JSON)

Sistema de estoque com quantidades

Múltiplos usuários com perfis diferentes

Histórico de compras

Sistema de cupons de desconto

Exportação para PDF do recibo

Categorização de produtos

⚠️ Observações
Sistema desenvolvido para fins educacionais

Interface baseada em terminal

Fácil de modificar e expandir

Código modular e bem comentado

👨‍💻 Autor
Yuri - Lojinha de Periféricos

📄 Licença
Este projeto é de uso livre para fins educacionais.
