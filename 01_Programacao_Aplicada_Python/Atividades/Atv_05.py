import requests
import json

# ATV 01:
def buscar_contacao():
    moeda = "USD-BRL"
    url = f"https://economia.awesomeapi.com.br/last/{moeda}"

    try:
        response = requests.get(url)
        dados = response.json()

        # b) Consulte a cotação do dólar
        # c) Exiba apenas o valor atual da moeda
        cotacao_dolar = dados["USDBRL"]["bid"]
        print(f"O valor atual da moeda é: R${cotacao_dolar}\n")
    except Exception as e:
        print(f"Erro ao consultar a API: {e}")

buscar_contacao()


# ATV 02:
def api_gitHub():
    user = input("Digite o user que você quer buscar: ")
    url = f"https://api.github.com/users/{user}"

    try:
        response = requests.get(url)
        if response.status_code == 404:
            raise ValueError("Erro ao buscar usuário, verifique se está correto.")
        
        dados = response.json()
        print(f"Os dados encontrados são:\n")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")
        print("\n")
    except Exception as err:
        print(f"Erro ao buscar API: {err}")


api_gitHub()


# ATV 03:
ia_dados = {
    "pergunta": "O que é JSON?",
    "resposta": "JSON (JavaScript Object Notation) é um formato leve de troca de dados."
}

# Convertendo os dados para JSON (string)
resultado_json = json.dumps(ia_dados, indent=4, ensure_ascii=False)
print(resultado_json)

#ATV 04:
def buscar_pais():
    pais = input("Digite o nome do país que deseja buscar: ")
    url = f"https://restcountries.com/v3.1/name/{pais}"

    try:
        response = requests.get(url)
        if response.status_code == 404:
            raise ValueError("Verifique se o nome do país está correto.")
        
        dados = response.json()[0]

        #Pega dados da Capital
        capital = dados["capital"][0]

        #Pega dados da População
        populacao = dados["population"]
        populacao_formatada = f"{populacao:,}".replace(",", ".")

        #Pega dados do nome
        nome = dados["name"]['nativeName']['por']['common']
        
        print(f"O país selecionado foi o {nome}, a capital é {capital} e a população atual é de {populacao_formatada}")
    except Exception as err:
        print(f"Erro ao buscar API: {err}")


buscar_pais()


#ATV 05:
dados = { "nome": "Marcela Luz", "idade": 21 }
print(f"O nome é {dados["nome"]}, e a idade é {dados["idade"]}")




#ATV 06:
def salvar_dados():
    user = input("Digite o user que você quer buscar: ")
    url = f"https://api.github.com/users/{user}"

    try:
        response = requests.get(url)
        if response.status_code == 404:
           raise ValueError("Erro ao buscar usuário, verifique se está correto.")
        
        dados = response.json()
        with open("dados_api.json", "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print(f"Os dados foram salvos com sucesso no arquivo dados_api.json")
    except Exception as err:
        print(f"Erro ao buscar API: {err}")

salvar_dados()


#ATV 07:
pergunta = input("Digite uma pergunta para a IA: ")
dados = {
    "pergunta": pergunta,
    "resposta": "Desculpe, nossos sistemas então fora do ar no momento. Volte mais tarde."
}

json_formatado = json.dumps(dados, indent=4, ensure_ascii=False)
print(json_formatado)