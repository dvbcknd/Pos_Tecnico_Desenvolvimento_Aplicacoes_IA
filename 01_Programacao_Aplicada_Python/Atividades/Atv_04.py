#Atividade 01 --------------------------------
nome = input("Digite o nome de usuário: ")

#Abre (ou cria) o arquivo chamado usuarios.txt, "a" de append, adiciona o texto sem apagar o que existe
with open("usuarios.txt",  "a") as arquivo:
    #Salva o nome digitado dentro do arquivo
    arquivo.write(nome + "\n")

print("Nome salvo com sucesso em usuarios.txt!")
#--------------------------------

#Atividade 02 ------------------------------------
mensagem = input("Escreva uma mensagem: ")

with open("chatbot.txt", "a") as arquivo:
    arquivo.write(mensagem + "\n")
#------------------------------------------------

#Atividade 03 -----------------------------------
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

with open("notas.txt", "a") as arquivo:
    arquivo.write(f"A primeira nota é: {nota1}\n")
    arquivo.write(f"A segunda nota é: {nota2}\n")
#------------------------------------------------

#Atividade 04 -------------------------------------
try:
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print("O conteúdo do arquivo é o:")
        print(f"    {conteudo}")

except FileNotFoundError:
    print("Error: Não foi possível ler o arquivo")
#--------------------------------------------------

#Atividade 05 -------------------------------------
nomeUsuario = input("Digite o nome do usuário, por favor: ")
#Foi usuado o mesmo arquivo usuarios.txt para mostrar que escreve sem apagar o que existe.
with open("usuarios.txt", "a") as arquivo:
    arquivo.write(f"O nome do usuário digitado é o: {nomeUsuario}\n")
# -------------------------------------------------

#Atividade 06 -------------------------------------
respostaUsuario = input("Qual é a sua resposta? ")

with open("respostas.txt", "a") as arquivo:
    arquivo.write(f"A resposta do usuário foi:\n    {respostaUsuario}")

print("A responta do usuário foi salva com sucesso!")
#--------------------------------------------------


#Atividade 07 -------------------------------------
# Abre o arquivo 'tarefas.txt' em modo de escrita ('w')
with open('tarefas.txt', 'w') as arquivo:
    for i in range(3):
        tarefa = input(f"Digite a tarefa {i+1}: ")
        arquivo.write(f"{tarefa}\n")

print("Tarefas salvas com sucesso em tarefas.txt!")
#--------------------------------------------------

#Atividade 08 -------------------------------------
palavra = input("Digite uma palavra (bom, ótimo, ruim ou péssimo): ").strip().lower()

# Define as categorias de sentimentos
positivos = ["bom", "ótimo"]
negativos = ["ruim", "péssimo"]

#Verifica se ela representa sentimento positivo ou negativo
if palavra in positivos:
    resultado = f"A palavra '{palavra}' tem sentimento Positivo."
elif palavra in negativos:
    resultado = f"A palavra '{palavra}' tem sentimento Negativo."
else:
    resultado = f"A palavra '{palavra}' não foi reconhecida no sistema."

# Exibe o resultado no console
print(resultado)

#Salva o resultado da análise em um arquivo chamado sentimentos.txt
with open("sentimentos.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{resultado}\n")

print("\nResultado salvo com sucesso em 'sentimentos.txt'!")
#--------------------------------------------------


#Atividade 09 -------------------------------------
genero = input("Qual é o seu gênero de filme favorito (ação, comédia, drama)? ").lower()

#Utilize if/else para recomendar um filme
if genero == "ação":
    recomendacao = "Recomendação: Filme 'Mad Max: Estrada da Fúria'"
elif genero == "comédia":
    recomendacao = "Recomendação: Filme 'Minha Mãe é uma Peça'"
elif genero == "drama":
    recomendacao = "Recomendação: Filme 'O Shawshank Redemption'"
else:
    recomendacao = "Recomendação: Filme 'Inception' (Gênero não mapeado)"

print(recomendacao)

#Salve a recomendação em um arquivo chamado recomendacoes.txt
with open("recomendacoes.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{recomendacao}\n")

print("Recomendação salva em 'recomendacoes.txt'.")
#--------------------------------------------------
