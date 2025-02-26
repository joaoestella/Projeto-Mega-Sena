import requests
import json

# URL da API com os resultados da Mega-Sena
url = "https://loteriascaixa-api.herokuapp.com/api/megasena"

# Enviar requisição para o servidor
response = requests.get(url)

# Verifica se a resposta foi bem-sucedida
if response.status_code == 200:
    dados_json = response.json()

    # Se a API retornar uma lista de concursos, percorremos todos
    if isinstance(dados_json, list):
        concursos_filtrados = []

        # Inverter a leitura da API
        dados_json.reverse()

        # For par adicionar objetos no dicionario
        for concurso in dados_json:
            concurso_filtrado = {
                "concurso": concurso.get("concurso"),  # Evita erro caso a chave não exista
                "data": concurso.get("data"), # Retorna a data do concurso
                "dezenas": concurso.get("dezenas", []),  # Retorna uma lista vazia se não houver dezenas
                "acumulou": concurso.get("acumulou", False),  # Assume False se não houver essa chave
                "ganhadores": concurso.get("ganhadores", [])  # Se não houver ganhadores, retorna lista vazia
            }
            concursos_filtrados.append(concurso_filtrado)

        # Salvar todos os concursos em um arquivo JSON
        nome_do_arquivo = 'mega-sena-todos-concursos.json'
        with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(concursos_filtrados, arquivo, indent=4, ensure_ascii=False)

        print(f"Dados salvos com sucesso em {nome_do_arquivo}")

    else:
        print("A API não retornou uma lista de concursos. Verifique a resposta.")

else:
    print(f'Erro {response.status_code}')
