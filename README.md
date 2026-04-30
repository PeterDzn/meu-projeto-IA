# Projeto de Testes e Assistência de Código

Um projeto educacional em Python focado em demonstrar boas práticas de programação, debugging e refatoração, com ênfase em algoritmos numéricos e processamento de dados.

## 📋 Descrição do Projeto

Este projeto contém exemplos práticos de código Python bem estruturado, documentado e testado, com foco em:

- **Verificação de Números Primos**: Implementação otimizada com cálculo até raiz quadrada
- **Processamento de Dados**: Filtragem, contagem e listagem de números
- **Cálculo de Nota Fiscal**: Sistema de entrada de dados com cálculos financeiros
- **Debugging e Refatoração**: Explicações e melhorias progressivas de código

---

## 📁 Estrutura de Arquivos

### Módulos Principais

#### `num_primos.py`
Módulo completo para verificação de números primos com implementação otimizada.

**Funcionalidades:**
- `eh_primo(numero)` - Verifica se um número é primo
- `filtrar_primos(numeros)` - Filtra primos de uma lista
- `contar_primos(inicio, fim)` - Conta primos em um intervalo
- `obter_lista_primos(inicio, fim)` - Retorna lista de primos em intervalo
- `exibir_resultado_teste(numero)` - Exibe resultado formatado
- `executar_testes()` - Executa bateria completa de testes

#### `debug.py`
Script interativo para cálculo de nota fiscal com três itens, imposto e desconto.

**Funcionalidades:**
- Entrada de dados de cliente e itens
- Cálculo automático de totais
- Aplicação de impostos (10%)
- Processamento de cupom de desconto
- Exibição formatada da nota fiscal

### Arquivos de Documentação

- `explicacao_num_primo.md` - Explicação detalhada do módulo de primos
- `explicacao-debug.md` - Análise do script de nota fiscal
- `explicacao-refatoracao.md` - Guia de refatoração e melhorias
- `refatoracao.py` - Versão refatorada com melhorias de código

---

## 🚀 Como Usar

### Verificação de Números Primos

#### Executar Testes Completos

```bash
python num_primos.py
```

Saída esperada:
```
==================================================
VERIFICAÇÃO DE NÚMEROS PRIMOS
==================================================

📊 Teste Individual:
--------------------------------------------------
   2 → primo
   3 → primo
   4 → não primo
...

🔍 Primos no intervalo [2, 30]:
--------------------------------------------------
Primos encontrados: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
Total: 10 números primos

📈 Estatísticas:
--------------------------------------------------
Primos entre 2 e 100: 25
```

#### Usar como Módulo

```python
from num_primos import eh_primo, obter_lista_primos, contar_primos

# Verificar se um número é primo
print(eh_primo(17))  # True
print(eh_primo(20))  # False

# Obter lista de primos em intervalo
primos = obter_lista_primos(10, 50)
print(primos)  # [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Contar primos
quantidade = contar_primos(1, 100)
print(quantidade)  # 25
```

### Cálculo de Nota Fiscal

```bash
python debug.py
```

O programa solicitará:
1. Nome do cliente
2. Quantidade e preço de 3 itens
3. Percentual de desconto (se houver cupom)

Exemplo de entrada:
```
Qual é seu nome? João Silva
Quantidade do item 1: 2
Preço do item 1? 50.00
Quantidade do item 2: 1
Preço do item 2? 100.00
Quantidade do item 3: 3
Preço do item 3? 25.00
Você tem um cupom de desconto? (Digite o percentual ou 0): 10
```

Saída:
```
===============================
 Cliente: João Silva
===============================
 Item 1:        R$ 100.00
 Item 2:        R$ 100.00
 Item 3:        R$ 75.00
-------------------------------
 Subtotal:      R$ 275.00
 Imposto (10%): R$ 27.50
 Desconto (10%): -R$ 27.50
===============================
 TOTAL:         R$ 275.00
===============================
```

---

## 📚 Detalhes das Funções

### `eh_primo(numero: int) -> bool`

Verifica se um número inteiro é primo.

**Otimizações:**
- Verifica até a raiz quadrada do número
- Testa apenas divisores ímpares
- Tratamento especial para 2 e números pares

**Exemplo:**
```python
>>> eh_primo(2)
True
>>> eh_primo(17)
True
>>> eh_primo(10)
False
```

### `filtrar_primos(numeros: List[int]) -> List[int]`

Filtra números primos de uma lista fornecida.

**Exemplo:**
```python
>>> filtrar_primos([2, 3, 4, 5, 10, 11])
[2, 3, 5, 11]
```

### `contar_primos(inicio: int, fim: int) -> int`

Conta a quantidade de primos em um intervalo (inclusivo).

**Exemplo:**
```python
>>> contar_primos(10, 20)
4  # 11, 13, 17, 19
```

### `obter_lista_primos(inicio: int, fim: int) -> List[int]`

Retorna lista de todos os primos em um intervalo (inclusivo).

**Exemplo:**
```python
>>> obter_lista_primos(10, 20)
[11, 13, 17, 19]
```

---

## 🔧 Boas Práticas Implementadas

✅ **Type Hints**: Todas as funções possuem anotações de tipo
✅ **Docstrings Google**: Documentação no padrão Google em português
✅ **Tratamento de Exceções**: Validação de entrada com erros informáticos
✅ **Exemplos de Uso**: Doctests em todas as funções
✅ **Otimização de Algoritmo**: Algoritmo com complexidade O(√n)
✅ **Formatação Clara**: Saída bem estruturada e legível
✅ **Modularização**: Funções pequenas e reutilizáveis

---

## 📖 Referências de Aprendizado

- **Números Primos**: Algoritmo de teste de primalidade por divisão de trial
- **Type Hints**: Documentação do Python PEP 484
- **Google Docstring**: Guia de estilo de docstrings Google
- **List Comprehension**: Construção eficiente de listas em Python

---

## 💡 Próximos Passos

Possibilidades de expansão do projeto:

1. Testes unitários com `pytest`
2. Implementação de algoritmos mais avançados (Crivo de Eratóstenes)
3. Análise de performance com `timeit`
4. Integração com banco de dados
5. Interface gráfica com `tkinter`
6. API REST com `FastAPI`

---

## 📝 Licença

Este projeto é educacional e pode ser usado livremente para fins de aprendizado.

---

## 👨‍💻 Autor

Projeto desenvolvido como exemplo de boas práticas em Python com assistência de IA.

**Data**: Abril de 2026
