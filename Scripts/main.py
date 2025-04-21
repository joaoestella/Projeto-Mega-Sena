# Importa a função responsável por verificar se os números gerados já saíram
from checagem_acertos import verificar_se_numeros_ja_sairam
# Importa a função que gera o jogo da Mega-Sena
from gerador_de_jogos import simulacao_real_mega_sena

# Função para perguntar ao usuário uma lista de números separados por vírgula
# Retorna uma lista com os números fornecidos, ou uma lista vazia se nenhum número for informado
def perguntar_lista_numeros(texto):
    # Solicita a entrada do usuário com a mensagem fornecida
    entrada = input(texto).strip()
    
    # Se o usuário não informar nada, retorna uma lista vazia
    if not entrada:
        return []
    
    # Caso o usuário forneça números separados por vírgula, converte cada um para um inteiro e retorna a lista
    return [int(num) for num in entrada.split(",") if num.strip().isdigit()]

# Laço principal que mantém o programa em execução até o usuário escolher sair
while True:
    # Exibe as opções disponíveis para o usuário
    print('[1] Gerar jogo \n[2] Verificar jogo manualmente \n[3] Sair')
    
    # Solicita a escolha do usuário
    escolha = int(input('Digite a escolha: '))

    # Se a escolha for gerar um jogo
    if escolha == 1:
        # Solicita ao usuário quantos números ele deseja no jogo (entre 6 e 15)
        quantidade = int(input("Quantos números deseja no jogo (6 a 15)? "))
        
        # Solicita ao usuário os números fixos que ele deseja incluir no jogo
        fixos = perguntar_lista_numeros("Digite os números fixos separados por vírgula (ou pressione Enter para nenhum): ")
        
        # Solicita ao usuário os números que ele deseja excluir do jogo
        excluir = perguntar_lista_numeros("Digite os números que deseja excluir separados por vírgula (ou pressione Enter para nenhum): ")

        # Chama a função para gerar o jogo com as preferências do usuário e verifica se esses números já saíram em algum concurso
        jogo = simulacao_real_mega_sena(quantidade=quantidade, fixos=fixos, excluir=excluir)
        verificar_se_numeros_ja_sairam(jogo)

    # Se a escolha for verificar um jogo manualmente
    elif escolha == 2:
        # Solicita ao usuário os números do jogo que ele deseja verificar
        numeros_manualmente = perguntar_lista_numeros("Digite os números do seu jogo separados por vírgula: ")
        
        # Verifica se esses números já saíram em algum concurso
        verificar_se_numeros_ja_sairam(numeros_manualmente)

    # Se a escolha for sair
    elif escolha == 3:
        print("Saindo...")  # Exibe uma mensagem de despedida
        break  # Encerra o laço e sai do programa

    # Se a escolha for inválida (não 1, 2 ou 3)
    else:
        print("Escolha inválida. Tente novamente.")  # Informa que a escolha foi inválida e solicita nova entrada
