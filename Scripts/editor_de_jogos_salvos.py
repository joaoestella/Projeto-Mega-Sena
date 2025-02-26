import os 
import json
from gerador_de_jogos import simulacao_real_mega_sena

# Função que carrega e verifica os arquivos gerados anteriomente no arquivo "jogos_salvo.json"
def carregar_jogos_gerados():
    if os.path.exists("jogos_salvo.json"):
        with open ("jogos_salvo.json", "r", encoding= 'utf-8' ) as arquivo:
            jogos = json.load(arquivo)
    else:
        jogos = []

    return jogos

# Função que salva o jogo gerado no arquivo "jogos_salvo.json"
def salvar_jogo_gerado():
    salvar_jogo = simulacao_real_mega_sena()
    jogos_salvo = carregar_jogos_gerados()

    numero_jogo = len(jogos_salvo) + 1

    jogos_salvo.append({f'Jogo {numero_jogo}': salvar_jogo})

    with open("jogos_salvo.json", "w", encoding='utf-8') as arquivo:
        json.dump(jogos_salvo, arquivo, indent=4, ensure_ascii=False)

# Função para limpar o arquivo "jogos_salvos.json"
def limpar_jogos_gerados():
    with open("jogos_salvo.json", 'w', encoding = 'utf-8') as arquivos:
        pass

