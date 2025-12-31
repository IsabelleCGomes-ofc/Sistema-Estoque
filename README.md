# 📦 Sistema de Controle de Estoque (Python)

Projeto desenvolvido em Python com persistência de dados em JSON, voltado para o gerenciamento básico de produtos em estoque.  
O sistema funciona em terminal e foi organizado em módulos para facilitar manutenção e leitura do código.

---

## 🎯 Objetivo do Projeto

Permitir o controle de produtos em um estoque, possibilitando:
- Cadastro de produtos
- Listagem de produtos
- Entrada e saída de estoque
- Remoção de produtos
- Armazenamento dos dados em arquivo JSON

---

## 🛠️ Tecnologias Utilizadas

- Python 
- JSON (persistência de dados)
- Execução via terminal

---

## 📂 Estrutura do Projeto

```bash
Sistema-Estoque/
│
├── main.py # Menu principal e controle do sistema
├── utils.py # Funções utilitárias (limpar tela, pausa)
├── data.py # Manipulação do arquivo JSON
├── cadastro.py # Cadastro de produtos
├── validacoes.py # Validações de entrada
├── gerenciamentoProdutos.py # Ações com produtos já existentes
```

## ⚙️ Funcionalidades

## 1 - Cadastrar Produto no Estoque
- Permite cadastrar um novo produto informando:
  - ID (gerado automaticamente)
  - Nome do produto
  - Quantidade inicial
  - Preço
- O produto é salvo no arquivo `estoque.json`

## 2 - Listar Produtos
- Exibe todos os produtos cadastrados no estoque, mostrando:
  - ID
  - Nome
  - Quantidade disponível
  - Preço

## 3️ - Entrada de Estoque
- Aumenta a quantidade de um produto existente

## 4 - Saída de Estoque
- Diminui a quantidade de um produto existente

## 5 - Remover Produto
- Remove um produto pelo ID
- Os IDs não são reorganizados (ID fixo)

---

## 🆔 Sobre o ID dos Produtos

- Cada produto possui um ID único e permanente
- Mesmo após a remoção de um produto, os IDs dos demais não são alterados
- O próximo ID gerado será sempre o maior ID existente + 1

Esse comportamento segue o padrão utilizado em sistemas reais e bancos de dados.

---

## ▶️ Como Executar o Projeto

1. Certifique-se de ter o Python 3 instalado
2. Clone ou baixe o repositório
4. Execute no terminal(ou pyCharm, mas não há erros de manutenção e exibição):

```bash
python main.py
├── gerenciamentoProdutos.py # Listar, remover e movimentar produtos
├── estoque.json # Arquivo de dados (gerado automaticamente)

└── README.md # Documentação do projeto

