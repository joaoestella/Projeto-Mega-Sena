import struct
import os

def simulacao_real_mega_sena(quantidade=6, fixos=None, excluir=None):
    # Verifica se a quantidade de números está dentro do limite permitido
    if not (6 <= quantidade <= 15):
        return "Erro: A quantidade de números deve estar entre 6 e 15."

    # Garante que as variáveis fixos e excluir sejam conjuntos (ou listas vazias se não forem passados)
    fixos = set(fixos or [])
    excluir = set(excluir or [])

    # Verifica se a quantidade de números fixos não excede a quantidade total do jogo
    if len(fixos) > quantidade:
        return "Erro: A quantidade de números fixos não pode ser maior que a quantidade total do jogo."

    # Inicializa o conjunto de números com os números fixos
    numeros = set(fixos)

    # Gera aleatoriamente os demais números até atingir a quantidade desejada
    while len(numeros) < quantidade:
        num = struct.unpack('I', os.urandom(4))[0]  # Gera um número inteiro aleatório
        num = (num % 60) + 1  # Limita o número entre 1 e 60 (intervalo da Mega-Sena)

        # Adiciona o número se ele não for repetido e não estiver na lista de exclusão
        if num not in numeros and num not in excluir:
            numeros.add(num)

    # Retorna os números ordenados em uma lista
    return sorted(numeros)