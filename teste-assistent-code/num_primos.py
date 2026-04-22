def eh_primo(numero):
    """
    Verifica se um número é primo.
    
    Args:
        numero (int): O número a ser verificado
        
    Returns:
        bool: True se o número é primo, False caso contrário
    """
    # Números menores que 2 não são primos
    if numero < 2:
        return False
    
    # 2 é o único número par primo
    if numero == 2:
        return True
    
    # Números pares não são primos
    if numero % 2 == 0:
        return False
    
    # Verifica divisibilidade apenas até a raiz quadrada do número
    # Se um número tem um divisor maior que sua raiz, também terá um menor
    i = 3
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 2  # Só verifica números ímpares
    
    return True


# Exemplos de uso
if __name__ == "__main__":
    # Testando a função
    numeros_teste = [2, 3, 4, 5, 10, 17, 20, 29, 100, 97]
    
    for num in numeros_teste:
        resultado = "primo" if eh_primo(num) else "não primo"
        print(f"{num} é {resultado}")
