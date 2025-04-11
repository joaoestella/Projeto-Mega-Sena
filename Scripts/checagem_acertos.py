# Importa a função responsável por gerar uma aposta aleatória de 6 dezenas
from gerador_de_jogos import simulacao_real_mega_sena
import json

# Função que verifica se os números gerados já saíram juntos em algum concurso da Mega-Sena
# Compara a aposta gerada com os resultados históricos contidos no arquivo JSON
# Caso haja 4, 5 ou 6 dezenas em comum com algum concurso anterior, informa o acerto e os detalhes
def verificar_se_numeros_ja_sairam(numeros_gerados):
    try:
        with open("mega-sena-todos-concursos.json", "r", encoding="utf-8") as arquivo:
            concursos = json.load(arquivo)

        # Converte os números gerados para strings com dois dígitos
        numeros_gerados_str = {str(num).zfill(2) for num in numeros_gerados}
        dezenas_gerada = set(numeros_gerados_str)

        # Percorre todos os concursos e verifica se houve interseção significativa (quadra, quina ou sena)
        for concurso in concursos:
            dezenas_concurso = set(concurso["dezenas"])
            intersecao = dezenas_concurso & dezenas_gerada
            tamanho = len(intersecao)

            match tamanho:
                case 4:
                    print(f'🎯 Acertou a QUADRA!\nNúmeros Gerados: {sorted(numeros_gerados)}\n'
                          f'Acertos: {sorted(intersecao)}\nConcurso: {concurso["concurso"]} - {concurso["data"]}\n')
                case 5:
                    print(f'🔥 Acertou a QUINA!\nNúmeros Gerados: {sorted(numeros_gerados)}\n'
                          f'Acertos: {sorted(intersecao)}\nConcurso: {concurso["concurso"]} - {concurso["data"]}\n')
                case 6:
                    print(f'🏆 ACERTOU A SENA!!!\nNúmeros Gerados: {sorted(numeros_gerados)}\n'
                          f'Acertos: {sorted(intersecao)}\nConcurso: {concurso["concurso"]} - {concurso["data"]}\n')

    except FileNotFoundError:
        print("❌ Erro: Arquivo mega-sena-todos-concursos.json não encontrado.")
    except json.JSONDecodeError:
        print("❌ Erro: Problema ao ler o arquivo JSON.")

# Função que gera uma nova aposta e chama a verificação no histórico de concursos
def gerar_e_verificar_jogo():
    numeros_gerados = simulacao_real_mega_sena()
    verificar_se_numeros_ja_sairam(numeros_gerados)

# Executa a função principal ao rodar o script
gerar_e_verificar_jogo()
