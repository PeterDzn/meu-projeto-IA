"""Módulo para verificação de números primos com implementação otimizada."""

from typing import List, Tuple


def eh_primo(numero: int) -> bool:
    """
    Verifica se um número inteiro é primo.
    
    Utiliza otimização de verificação até a raiz quadrada do número,
    testando apenas divisores ímpares para melhor performance.
    
    Args:
        numero: O número inteiro a ser verificado.
        
    Returns:
        True se o número é primo, False caso contrário.
        
    Raises:
        TypeError: Se o argumento não for um inteiro.
        
    Examples:
        >>> eh_primo(2)
        True
        >>> eh_primo(17)
        True
        >>> eh_primo(10)
        False
    """
    if not isinstance(numero, int):
        raise TypeError(f"Esperado int, obtido {type(numero).__name__}")
    
    if numero < 2:
        return False
    
    if numero == 2:
        return True
    
    if numero % 2 == 0:
        return False
    
    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2
    
    return True


def filtrar_primos(numeros: List[int]) -> List[int]:
    """
    Filtra números primos de uma lista.
    
    Args:
        numeros: Lista de números inteiros a filtrar.
        
    Returns:
        Lista contendo apenas os números primos.
        
    Examples:
        >>> filtrar_primos([2, 3, 4, 5])
        [2, 3, 5]
    """
    return [num for num in numeros if eh_primo(num)]


def contar_primos(inicio: int, fim: int) -> int:
    """
    Conta quantos números primos existem em um intervalo.
    
    Args:
        inicio: Número inicial do intervalo (inclusivo).
        fim: Número final do intervalo (inclusivo).
        
    Returns:
        Quantidade de primos no intervalo.
        
    Examples:
        >>> contar_primos(10, 20)
        4
    """
    return sum(1 for num in range(inicio, fim + 1) if eh_primo(num))


def obter_lista_primos(inicio: int, fim: int) -> List[int]:
    """
    Obtém lista de números primos em um intervalo.
    
    Args:
        inicio: Número inicial do intervalo (inclusivo).
        fim: Número final do intervalo (inclusivo).
        
    Returns:
        Lista de números primos encontrados.
        
    Examples:
        >>> obter_lista_primos(10, 20)
        [11, 13, 17, 19]
    """
    return [num for num in range(inicio, fim + 1) if eh_primo(num)]


def exibir_resultado_teste(numero: int) -> None:
    """Exibe o resultado da verificação de um número."""
    try:
        eh_prime = eh_primo(numero)
        status = "primo" if eh_prime else "não primo"
        print(f"{numero:4d} → {status}")
    except TypeError as e:
        print(f"Erro ao testar {numero}: {e}")


def executar_testes() -> None:
    """Executa testes com diferentes números e intervalos."""
    print("=" * 50)
    print("VERIFICAÇÃO DE NÚMEROS PRIMOS")
    print("=" * 50)
    
    numeros_teste = [2, 3, 4, 5, 10, 17, 20, 29, 100, 97]
    
    print("\n📊 Teste Individual:")
    print("-" * 50)
    for numero in numeros_teste:
        exibir_resultado_teste(numero)
    
    print("\n🔍 Primos no intervalo [2, 30]:")
    print("-" * 50)
    primos = obter_lista_primos(2, 30)
    print(f"Primos encontrados: {primos}")
    print(f"Total: {len(primos)} números primos")
    
    print("\n📈 Estatísticas:")
    print("-" * 50)
    intervalo_inicio, intervalo_fim = 2, 100
    total = contar_primos(intervalo_inicio, intervalo_fim)
    print(f"Primos entre {intervalo_inicio} e {intervalo_fim}: {total}")
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    executar_testes()
