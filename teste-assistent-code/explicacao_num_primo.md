# Explicação Técnica: Verificação de Números Primos em Python

## 📋 Visão Geral

Este documento descreve a implementação otimizada e orientada a **Clean Code** da funcionalidade de verificação de números primos. O módulo oferece múltiplas funções para diferentes casos de uso, com type hints completos e tratamento de erros robusto.

---

## 🎯 O que é um Número Primo?

Um **número primo** é um número natural maior que 1 que possui exatamente dois divisores distintos:
- O número 1
- O próprio número

**Exemplos:** 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...

**Contraexemplos:** 1 (não é primo), 4 (divisível por 2), 9 (divisível por 3), 10 (divisível por 2 e 5)

---

## 📦 Estrutura do Módulo

```
num_primos.py
├── eh_primo(numero: int) → bool
├── filtrar_primos(numeros: List[int]) → List[int]
├── contar_primos(inicio: int, fim: int) → int
├── obter_lista_primos(inicio: int, fim: int) → List[int]
├── exibir_resultado_teste(numero: int) → None
└── executar_testes() → None
```

---

## 🔧 Análise Detalhada das Funções

### 1️⃣ Função Principal: `eh_primo(numero: int) -> bool`

#### Assinatura com Type Hints

```python
def eh_primo(numero: int) -> bool:
```

**Type Hints:**
- `numero: int` - parâmetro deve ser inteiro
- `-> bool` - retorna booleano

**Benefícios:**
- Detecta erros de tipo em tempo de desenvolvimento
- Melhora documentação automática
- Facilita uso com IDEs modernas

#### Validação de Entrada

```python
if not isinstance(numero, int):
    raise TypeError(f"Esperado int, obtido {type(numero).__name__}")
```

**Princípio Clean Code:** Falhe rapidamente com mensagens claras. Evita erros silenciosos e comportamentos inesperados.

#### Lógica de Verificação

| Etapa | Descrição | Tempo |
|-------|-----------|-------|
| 1 | `numero < 2` → False | O(1) |
| 2 | `numero == 2` → True | O(1) |
| 3 | `numero % 2 == 0` → False | O(1) |
| 4 | Loop até √n com passo 2 | O(√n) |

#### Variável com Nome Descritivo

```python
divisor = 3  # Antes: i = 3
while divisor * divisor <= numero:
    if numero % divisor == 0:
        return False
    divisor += 2
```

**Melhoria Clean Code:** `divisor` é mais legível que `i`. O nome reflete o propósito da variável.

---

### 2️⃣ Função: `filtrar_primos(numeros: List[int]) -> List[int]`

Filtra números primos de uma lista usando list comprehension.

```python
def filtrar_primos(numeros: List[int]) -> List[int]:
    return [num for num in numeros if eh_primo(num)]
```

**Uso:**
```python
>>> filtrar_primos([2, 3, 4, 5, 10])
[2, 3, 5]
```

**Benefícios:**
- Reutiliza função principal
- Código conciso e Pythônico
- Type hints claros sobre entrada/saída

---

### 3️⃣ Função: `contar_primos(inicio: int, fim: int) -> int`

Conta quantos primos existem em um intervalo sem armazenar a lista.

```python
def contar_primos(inicio: int, fim: int) -> int:
    return sum(1 for num in range(inicio, fim + 1) if eh_primo(num))
```

**Vantagens:**
- Economiza memória (não cria lista intermediária)
- Eficiente para intervalos grandes
- Usa generator expression

**Uso:**
```python
>>> contar_primos(2, 100)
25
```

---

### 4️⃣ Função: `obter_lista_primos(inicio: int, fim: int) -> List[int]`

Retorna lista de primos em um intervalo.

```python
def obter_lista_primos(inicio: int, fim: int) -> List[int]:
    return [num for num in range(inicio, fim + 1) if eh_primo(num)]
```

**Uso:**
```python
>>> obter_lista_primos(10, 20)
[11, 13, 17, 19]
```

---

### 5️⃣ Função: `exibir_resultado_teste(numero: int) -> None`

Exibe resultado formatado com tratamento de erros.

```python
def exibir_resultado_teste(numero: int) -> None:
    try:
        eh_prime = eh_primo(numero)
        status = "primo" if eh_prime else "não primo"
        print(f"{numero:4d} → {status}")
    except TypeError as e:
        print(f"Erro ao testar {numero}: {e}")
```

**Princípio Clean Code:**
- Responsabilidade única: apenas exibir resultado
- Tratamento de exceções específicas
- Formatação clara com f-string

---

### 6️⃣ Função: `executar_testes() -> None`

Orquestra todos os testes do módulo.

```python
def executar_testes() -> None:
    # Testes individuais
    # Teste em intervalo
    # Estatísticas
```

**Organização:**
1. **Teste Individual** - verifica números específicos
2. **Teste em Intervalo** - lista primos em range
3. **Estatísticas** - resumo das operações

**Saída Formatada:**
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
```

---

## ✨ Princípios Clean Code Aplicados

### 1. **Type Hints Completos**
```python
# ✅ Bom - Type hints explícitos
def filtrar_primos(numeros: List[int]) -> List[int]:

# ❌ Ruim - Sem informação de tipo
def filtrar_primos(numeros):
```

### 2. **Nomes Significativos**
```python
# ✅ Bom - Nome descreve o propósito
divisor = 3

# ❌ Ruim - Nome vago
i = 3
```

### 3. **Funções com Responsabilidade Única**
- `eh_primo()` - apenas verifica
- `filtrar_primos()` - apenas filtra
- `exibir_resultado_teste()` - apenas exibe

### 4. **Docstrings Descritivas**
Cada função possui docstring com:
- Descrição clara do propósito
- Args e Returns documentados
- Exemplos de uso (doctest)

### 5. **Tratamento de Erros**
```python
if not isinstance(numero, int):
    raise TypeError(f"Esperado int, obtido {type(numero).__name__}")
```

### 6. **Legibilidade**
- Variáveis nomeadas apropriadamente
- Funções pequenas e focadas
- Comentários apenas quando necessário

### 7. **DRY (Don't Repeat Yourself)**
- `filtrar_primos()` reutiliza `eh_primo()`
- `contar_primos()` reutiliza `eh_primo()`
- Evita duplicação de lógica

---

## 📊 Análise de Complexidade

| Função | Tempo | Espaço |
|--------|-------|--------|
| `eh_primo(n)` | O(√n) | O(1) |
| `filtrar_primos(lista)` | O(m × √n)* | O(k)* |
| `contar_primos(a, b)` | O((b-a) × √n) | O(1) |
| `obter_lista_primos(a, b)` | O((b-a) × √n) | O(k) |

*m = tamanho da lista, n = maior número, k = quantidade de primos

---

## 🧪 Exemplos de Execução

### Teste 1: Número Individual
```python
>>> eh_primo(17)
True
```

### Teste 2: Filtrar Lista
```python
>>> filtrar_primos([10, 11, 12, 13, 14, 15])
[11, 13]
```

### Teste 3: Contar em Intervalo
```python
>>> contar_primos(2, 50)
15  # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
```

### Teste 4: Listar Primos
```python
>>> obter_lista_primos(20, 40)
[23, 29, 31, 37]
```

### Teste 5: Tratamento de Erro
```python
>>> eh_primo("17")
TypeError: Esperado int, obtido str
```

---

## 🚀 Performance Real

Para números até **1.000.000**:
- ✅ `eh_primo(999983)`: ~317 verificações (√999983 ≈ 999)
- ✅ `contar_primos(2, 1000)`: detecta 168 primos em ms
- ✅ `obter_lista_primos(1, 10000)`: encontra 1229 primos rapidamente

**Comparação:**
- Algoritmo ingênuo O(n): 999.999 operações
- Algoritmo otimizado O(√n): apenas ~999 operações ✓

---

## 📝 Casos de Uso

✅ Criptografia RSA (geração de números primos grandes)  
✅ Otimização de tabelas hash (tamanho primo)  
✅ Análise de sequências numéricas  
✅ Algoritmos de fatoração  
✅ Educação em otimização de algoritmos  

---

## 🔗 Referências

- **Teorema Fundamental da Aritmética:** Todo inteiro > 1 é primo ou produto de primos
- **Otimização √n:** Baseia-se no princípio dos divisores complementares
- **PEP 257:** Docstring Conventions (Python)
- **PEP 484:** Type Hints (Python)
