# Explicação Técnica: Verificação de Números Primos em Python

## 📋 Visão Geral

Este documento descreve em detalhes a função `eh_primo()`, que implementa um algoritmo eficiente para determinar se um número inteiro é primo.

---

## 🎯 O que é um Número Primo?

Um **número primo** é um número natural maior que 1 que possui exatamente dois divisores distintos:
- O número 1
- O próprio número

**Exemplos:** 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...

**Contraexemplos:** 1 (não é primo), 4 (divisível por 2), 9 (divisível por 3), 10 (divisível por 2 e 5)

---

## 🔧 Análise do Código

### Assinatura da Função

```python
def eh_primo(numero):
```

- **Parâmetro:** `numero` (int) - o número inteiro a ser testado
- **Retorno:** bool - `True` se primo, `False` se não primo

### Passo 1: Validação Inicial (números < 2)

```python
if numero < 2:
    return False
```

**Razão:** Por definição matemática, números menores que 2 (como 0, 1 e números negativos) **não são primos**. Este é o caso base mais simples.

**Complexidade:** O(1) - tempo constante

### Passo 2: Caso Especial - Número 2

```python
if numero == 2:
    return True
```

**Razão:** O número 2 é o **único número primo par**. É importante tratá-lo separadamente porque:
- 2 só é divisível por 1 e por 2
- Permite otimizar o algoritmo descartando todos os outros pares

**Complexidade:** O(1) - tempo constante

### Passo 3: Descartar Números Pares

```python
if numero % 2 == 0:
    return False
```

**Razão:** Qualquer número par maior que 2 é divisível por 2, logo não é primo. Isso elimina 50% dos candidatos imediatamente.

**Complexidade:** O(1) - tempo constante

**Operador `%`:** Retorna o resto da divisão. Se `numero % 2 == 0`, o número é par.

### Passo 4: Verificação de Divisibilidade (Loop Principal)

```python
i = 3
while i * i <= numero:
    if numero % i == 0:
        return False
    i += 2
```

#### 4.1 - Por que verificar até √n?

**Princípio Matemático:** Se um número `n` tem um divisor `d` maior que √n, então também possui um divisor `d' = n/d` menor que √n.

**Exemplo:** Para 36:
- √36 = 6
- Se 36 é divisível por 9 (> 6), também é por 36/9 = 4 (< 6)
- Logo, só precisamos verificar divisores até 6

**Implicação:** Se nenhum divisor até √n foi encontrado, o número é primo.

**Redução de Complexidade:**
- Abordagem ingênua: O(n) - verifica até n-1
- Abordagem otimizada: O(√n) - verifica até √n

Para n = 1.000.000:
- Ingênua: 999.999 iterações
- Otimizada: apenas ~1.000 iterações ✓

#### 4.2 - Por que incrementar de 2 em 2?

```python
i += 2  # Só verifica números ímpares
```

**Razão:** Como já descartamos números pares, só precisamos testar divisores ímpares:
- i começa em 3
- Incrementa em 2: 3, 5, 7, 9, 11, 13...
- Isso elimina metade dos testes dentro do loop

#### 4.3 - Condição do While

```python
while i * i <= numero:
```

**Equivalente a:** `while i <= sqrt(numero)`

**Evita calcular √n** (que é mais custoso computacionalmente). A condição `i * i <= numero` é verificada em O(1).

**Exemplo prático para 97:**
- √97 ≈ 9.85
- Itera: i = 3, 5, 7, 9
- 9 × 9 = 81 ≤ 97 ✓ (continua)
- 11 × 11 = 121 > 97 ✗ (para)
- Nenhum divisor encontrado → 97 é primo

---

## 📊 Análise de Complexidade

| Métrica | Valor |
|---------|-------|
| **Complexidade de Tempo** | O(√n) |
| **Complexidade de Espaço** | O(1) |
| **Caso Melhor** | O(1) - número par > 2 |
| **Caso Pior** | O(√n) - número primo grande |

**Comparação com outras abordagens:**

```
Ingênua (divide por todos):           O(n)        - muito lenta
Otimizada (até √n, pares):           O(√n)       - boa performance ✓
Crivo de Eratóstenes (múltiplos):    O(n log log n) - para vários números
```

---

## 🧪 Exemplos de Execução

### Exemplo 1: Número Par Simples (4)
```
eh_primo(4)
├─ 4 < 2? Não
├─ 4 == 2? Não
├─ 4 % 2 == 0? Sim → Retorna False
```
**Resultado:** `False` (4 não é primo)

### Exemplo 2: Número Primo Pequeno (5)
```
eh_primo(5)
├─ 5 < 2? Não
├─ 5 == 2? Não
├─ 5 % 2 == 0? Não
├─ Loop:
│  ├─ i = 3: 3×3 = 9 ≤ 5? Não → para loop
├─ Retorna True
```
**Resultado:** `True` (5 é primo)

### Exemplo 3: Número Primo Grande (97)
```
eh_primo(97)
├─ 97 < 2? Não
├─ 97 == 2? Não
├─ 97 % 2 == 0? Não
├─ Loop:
│  ├─ i = 3: 97 % 3 ≠ 0, continua
│  ├─ i = 5: 97 % 5 ≠ 0, continua
│  ├─ i = 7: 97 % 7 ≠ 0, continua
│  ├─ i = 9: 97 % 9 ≠ 0, continua
│  ├─ i = 11: 11×11 = 121 > 97? Sim → para loop
├─ Retorna True
```
**Resultado:** `True` (97 é primo)

---

## 💡 Otimizações Aplicadas

1. **Early Exit:** Retorna `False` assim que encontra um divisor
2. **Redução por Metade:** Descarta números pares no começo
3. **Raiz Quadrada:** Limita iterações a O(√n)
4. **Incremento em 2:** Testa apenas divisores ímpares

---

## 🚀 Performance

Para testar números de 2 a 1.000.000:
- **Velocidade:** Detecta todos os ~78.498 primos rapidamente
- **Memória:** Apenas uma variável (`i`) além do parâmetro
- **Escala:** Ainda eficiente para números muito grandes

---

## 📝 Casos de Uso

✅ Validação de números primos em criptografia  
✅ Otimização de algoritmos matemáticos  
✅ Verificação de chaves em estruturas de dados  
✅ Aplicações de processamento numérico  

---

## 🔗 Referências Matemáticas

- **Teorema Fundamental da Aritmética:** Todo inteiro > 1 é primo ou produto de primos
- **Teorema dos Números Primos:** Densidade de primos diminui conforme n aumenta
- **Otimização √n:** Baseia-se no princípio dos divisores complementares
