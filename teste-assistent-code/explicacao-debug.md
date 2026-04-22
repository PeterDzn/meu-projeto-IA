# Explicação dos Erros no Código de Debug

## 1. Falta de aspas na string da entrada do preço do item 1

No código original, a linha abaixo causa um erro de sintaxe porque o texto do prompt não está entre aspas:

```python
item1 = float(input(Preço do item 1? ))
```

O Python interpreta `Preço` como um nome de variável em vez de uma string literal. A correção é usar aspas:

```python
item1 = float(input("Preço do item 1? "))
```

## 2. `desconto_cupom` é uma string, mas é usado em cálculo numérico

O valor lido por `input()` é sempre uma string. A linha abaixo gera um erro de tipo ao tentar dividir a string por 100:

```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```

A correção é converter o valor para número antes de usar:

```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

## 3. String de formatação faltando o prefixo `f` no print do item 2

A linha abaixo não formata a variável `total_item2`, deixando o texto fixo e exibindo a chave literal:

```python
print(" Item 2:        R$ {total_item2:.2f}")
```

O correto é usar f-string:

```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

## 4. Indentação incorreta dentro do `if`

A condição abaixo está incorreta porque o bloco do `if` não está indentado. Isso causa um erro de sintaxe:

```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

O bloco do `if` precisa ser indentado:

```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

## 5. Ajuste de formatação final do total

A linha original usa `round(total, 2)` dentro de uma f-string com formatação que já define duas casas decimais. O uso de `round()` é redundante aqui, mas não é um erro grave.

```python
print(f" TOTAL:         R$ {round(total, 2):.2f}")
```

A forma mais limpa é:

```python
print(f" TOTAL:         R$ {total:.2f}")
```

## Resumo das correções aplicadas

- Adicionado aspas no prompt do `input()` para o preço do item 1
- Convertido `desconto_cupom` para `float` antes do cálculo
- Ajustado o `print` do item 2 para usar f-string
- Corrigida a indentação do bloco `if`
- Simplificada a formatação final do total

Essas correções resolvem os erros de sintaxe e de tipo presentes no código original.