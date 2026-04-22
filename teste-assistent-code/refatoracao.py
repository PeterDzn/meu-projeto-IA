"""Módulo para cálculos estatísticos básicos com implementação Clean Code."""

from typing import List, Tuple, Union


def calcular_estatisticas(numeros: List[Union[int, float]]) -> Tuple[float, float, Union[int, float], Union[int, float]]:
    """
    Calcula estatísticas básicas de uma lista de números.

    Realiza todos os cálculos em um único loop para otimização,
    incluindo soma total, média, maior e menor valor.

    Args:
        numeros: Lista de números (int ou float) para análise.

    Returns:
        Tupla contendo (soma_total, media, maior_valor, menor_valor).

    Raises:
        ValueError: Se a lista estiver vazia.
        TypeError: Se o argumento não for uma lista.

    Examples:
        >>> calcular_estatisticas([1, 2, 3, 4, 5])
        (15, 3.0, 5, 1)

        >>> calcular_estatisticas([10.5, 20.3, 15.7])
        (46.5, 15.5, 20.3, 10.5)
    """
    if not isinstance(numeros, list):
        raise TypeError("Esperado uma lista de números")

    if not numeros:
        raise ValueError("Lista não pode estar vazia")

    # Inicialização com o primeiro elemento
    soma_total = 0.0
    maior_valor = menor_valor = numeros[0]

    # Loop único para todos os cálculos
    for numero in numeros:
        soma_total += numero
        if numero > maior_valor:
            maior_valor = numero
        if numero < menor_valor:
            menor_valor = numero

    # Cálculo da média
    media = soma_total / len(numeros)

    return soma_total, media, maior_valor, menor_valor


def exibir_estatisticas(numeros: List[Union[int, float]]) -> None:
    """
    Exibe estatísticas formatadas de uma lista de números.

    Args:
        numeros: Lista de números para exibir estatísticas.

    Examples:
        >>> exibir_estatisticas([1, 2, 3])
        📊 Estatísticas dos Números:
        ----------------------------------------
        📋 Lista analisada: [1, 2, 3]
        🔢 Quantidade: 3 elementos
        ➕ Soma total: 6.0
        📈 Média: 2.00
        ⬆️  Maior valor: 3
        ⬇️  Menor valor: 1
    """
    try:
        soma_total, media, maior, menor = calcular_estatisticas(numeros)

        print("📊 Estatísticas dos Números:")
        print("-" * 40)
        print(f"📋 Lista analisada: {numeros}")
        print(f"🔢 Quantidade: {len(numeros)} elementos")
        print(f"➕ Soma total: {soma_total}")
        print(f"📈 Média: {media:.2f}")
        print(f"⬆️  Maior valor: {maior}")
        print(f"⬇️  Menor valor: {menor}")
        print()

    except (ValueError, TypeError) as erro:
        print(f"❌ Erro ao calcular estatísticas: {erro}")


def executar_testes() -> None:
    """Executa testes com diferentes listas de exemplo."""
    print("=" * 60)
    print("TESTES DE CÁLCULOS ESTATÍSTICOS")
    print("=" * 60)

    # Teste 1: Lista original
    lista_original = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    print("\n🧪 Teste 1: Lista Original")
    exibir_estatisticas(lista_original)

    # Teste 2: Lista com números decimais
    lista_decimais = [10.5, 20.3, 15.7, 8.9, 12.1]
    print("🧪 Teste 2: Lista com Decimais")
    exibir_estatisticas(lista_decimais)

    # Teste 3: Lista pequena
    lista_pequena = [42]
    print("🧪 Teste 3: Lista com Um Elemento")
    exibir_estatisticas(lista_pequena)

    # Teste 4: Lista negativa
    lista_negativa = [-5, -2, -8, -1, -3]
    print("🧪 Teste 4: Lista com Números Negativos")
    exibir_estatisticas(lista_negativa)

    # Teste 5: Casos de erro
    print("🧪 Teste 5: Casos de Erro")
    print("- Lista vazia:")
    exibir_estatisticas([])

    print("- Tipo inválido:")
    try:
        exibir_estatisticas("não é lista")
    except TypeError as e:
        print(f"❌ Erro esperado: {e}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    executar_testes()