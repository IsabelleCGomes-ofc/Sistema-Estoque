# Testes do Sistema de Controle de Estoque

Este documento descreve os testes realizados para validar o funcionamento
do sistema de controle de estoque, garantindo a integridade dos dados,
o correto funcionamento das regras de negócio e a experiência do usuário.

---

## Teste 1 — Validação de Quantidade (Número Inteiro)

**Descrição:**  
Verificar se o sistema impede o cadastro ou movimentação quando a quantidade
informada é inválida.

**Entradas inválidas testadas:**
- campo vazio
- valor negativo
- texto
- número não inteiro

**Resultado esperado:**  
O sistema deve exibir mensagens de erro específicas e solicitar nova digitação
da quantidade até que um valor inteiro positivo seja informado.

**Resultado obtido:**  
O sistema apresentou comportamento conforme esperado, não permitindo o avanço
do fluxo enquanto a entrada fosse inválida.

---

## Teste 2 — Validação de Preço (Número Real)

**Descrição:**  
Verificar se o sistema impede o cadastro quando o preço informado é inválido.

**Entradas inválidas testadas:**
- campo vazio
- valor negativo
- texto (valor não numérico)

**Resultado esperado:**  
O sistema deve exibir mensagem de erro e solicitar nova digitação do preço.

**Resultado obtido:**  
O sistema aceitou apenas valores numéricos positivos, conforme esperado.

---

## Teste 3 — Retirada Maior que a Quantidade em Estoque

**Descrição:**  
Verificar se o sistema impede a retirada de uma quantidade maior do que a
disponível em estoque.

**Entrada:**  
- quantidade >= quantidadeRetirada

**Resultado esperado:**  
O sistema deve impedir a operação e solicitar nova digitação da quantidade.

**Resultado obtido:**  
A operação foi corretamente bloqueada, mantendo a quantidade do estoque
inalterada.

---

## Teste 4 — ID de Produto Inexistente

**Descrição:**  
Verificar o comportamento do sistema ao informar um ID que não está cadastrado.

**Entrada:**  
- ID inexistente

**Resultado esperado:**  
O sistema deve informar que o produto não foi encontrado e não realizar
alterações nos dados.

**Resultado obtido:**  
O sistema exibiu a mensagem adequada e não efetuou nenhuma modificação no estoque.

---

## Teste 5 — Operações com Dados Válidos

**Descrição:**  
Verificar o funcionamento correto do sistema quando todos os dados informados
são válidos.

**Entradas:**
- quantidade válida
- preço válido
- ID existente

**Resultado esperado:**  
O sistema deve realizar a operação com sucesso.

**Resultado obtido:**  
As operações foram executadas corretamente e os dados foram atualizados conforme esperado.

---

## Conclusão dos Testes

Os testes realizados demonstram que o sistema lida corretamente com entradas
válidas e inválidas, impedindo a persistência de dados incorretos e garantindo
o cumprimento das regras de negócio. O comportamento observado foi consistente
com os resultados esperados, validando a estabilidade da versão 1.0.0.
