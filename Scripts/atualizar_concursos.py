import requests
import json
import os

# Nome do arquivo onde os concursos serão salvos
nome_do_arquivo = 'mega-sena-todos-concursos.json'

# URL da API com os resultados da Mega-Sena
url = "https://loteriascaixa-api.herokuapp.com/api/megasena"

# Enviar requisição para o servidor
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()

    # Se a API retornar uma lista de concursos, processamos
    if isinstance(dados_json, list):
        # Inverter a lista para ter os mais antigos primeiro
        dados_json.reverse()

        # Carregar os concursos já salvos, se o arquivo existir
        if os.path.exists(nome_do_arquivo):
            with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
                concursos_salvos = json.load(arquivo)
        else:
            concursos_salvos = []

        # Verificar qual foi o último concurso salvo
        concursos_existentes = {c["concurso"] for c in concursos_salvos}
        novos_concursos = []

        for concurso in dados_json:
            numero_concurso = concurso.get("concurso")
            if numero_concurso not in concursos_existentes:
                concurso_filtrado = {
                    "concurso": numero_concurso,
                    "data": concurso.get("data"),
                    "dezenas": concurso.get("dezenas", []),
                    "acumulou": concurso.get("acumulou", False),
                    "ganhadores": concurso.get("ganhadores", [])
                }
                novos_concursos.append(concurso_filtrado)

        # Se houver concursos novos, adicionar ao arquivo
        if novos_concursos:
            concursos_salvos.extend(novos_concursos)

            # Salvar novamente os concursos ordenados
            with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(concursos_salvos, arquivo, indent=4, ensure_ascii=False)

            print(f"{len(novos_concursos)} novos concursos adicionados!")
        else:
            print("Nenhum concurso novo encontrado.")
    else:
        print("A API não retornou uma lista de concursos.")
else:
    print(f'Erro {response.status_code}')