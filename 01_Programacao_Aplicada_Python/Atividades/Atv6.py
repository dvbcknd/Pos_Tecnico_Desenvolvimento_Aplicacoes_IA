import json


# ATV 01: -----------------------------------------
pergunta = input("Digite sua pergunta: ").lower()

if "horas" in pergunta:
    resposta = "Basta olhar no canto inferior direito da sua tela!"
elif "nome" in pergunta:
    resposta = "Meu nome é PyIA"
elif "clima" in pergunta or "tempo" in pergunta:
    resposta = "O dia está ótimo para estudar Python!"
else:
    resposta = "Desculpe, ainda não sei responder a essa pergunta."

print(resposta)


#ATV 02: -----------------------------------------
palavra = input("Digite uma palavra para análise de sentimento: ").lower().strip()

positivos = ["bom", "ótimo", "feliz", "excelente", "agradecido", "gostar", "parabéns", "gostei"]
negativos = ["ruim", "péssimo", "triste", "horrível", "insatisfeito", "reclamar", "ódio", "odiei"]

if palavra in positivos:
    sentimento = "Positivo"
elif palavra in negativos:
    sentimento = "Negativo"
else:
    sentimento = "Neutro"

print(f"O sentimento da palavra '{palavra}' é: {sentimento}")


#ATV 03: -----------------------------------------
genero = input("Qual o seu genero favorito? É ação, comédia ou terror? ").strip().lower()

if genero == "ação":
   print("Recomendação: Mad Max: Estrada da Fúria.")
elif genero == "comédia":
   print("Recomendação: Se Beber, Não Case!")
elif genero == "terror":
   print("Recomendação: Invocação do Mal.")
else:
   print("Gênero não reconhecido. Por favor, escolha entre ação, comédia ou terror.")



#ATV 04:  -----------------------------------------
dados_pergunta = {
    "usuario": "aluno_senai",
    "pergunta": "Qual a importância de aprender sobre APIs e JSON?",
    "idioma": "pt-br",
    "modelo_ia": "gpt-4"
}

json_formatado = json.dumps(dados_pergunta, indent=4, ensure_ascii=False)
print(json_formatado)


#ATV 05: -----------------------------------------
pergunta = input("Digite sua pergunta: ")

with open("historico_ia.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{pergunta}\n")
print("Sua pergunta foi salva com sucesso no histórico!")


#ATV 06: -----------------------------------------
pergunta = input("Faça uma pergunta: ").lower().strip()

if pergunta == "oi":
    print("Olá!")
elif pergunta == "como você funciona?":
    print("Utilizo programação e IA.")
else:
    print("Não compreendi.")


#ATV 07: -----------------------------------------
entrada = ""

while entrada.lower() != "sair":
    entrada = input("Digite sua pergunta (ou 'sair' para encerrar): ")

print("Programa encerrado.")


#ATV 08: -----------------------------------------
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print(f"Média: {media:.2f}")

if media >= 8:
    print("Excelente desempenho")
elif media >= 5:
    print("Bom desempenho")
else:
    print("Desempenho insuficiente")
