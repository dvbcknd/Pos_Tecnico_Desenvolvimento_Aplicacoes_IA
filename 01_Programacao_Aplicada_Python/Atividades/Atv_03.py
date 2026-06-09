

# Atividade 01: 
# Solicita o gênero ao usuário
genero = input("Escolha um gênero de filme (ação, comédia ou terror): ").strip().lower()

# Estrutura condicional para recomendação
if genero == "ação":
   print("Recomendação: Mad Max: Estrada da Fúria.")
elif genero == "comédia":
   print("Recomendação: Se Beber, Não Case!")
elif genero == "terror":
   print("Recomendação: Invocação do Mal.")
else:
   print("Gênero não reconhecido. Por favor, escolha entre ação, comédia ou terror.")


# Atividade 02:
# 1. Solicita ao usuário que digite uma palavra
palavra = input("Digite uma palavra para análise: ").lower().strip()

# 2. Classificação
if palavra in ["bom", "ótimo", "excelente", "maravilhoso", "gostei", "adorei", "muito bom"]:
   print("Classificação: Positivo")
elif palavra in ["ruim", "péssimo", "horrível", "odiado", "fraco", "não gostei"]:
   print("Classificação: Negativo")
else:
   print("Classificação: Neutro")



# Atividade 03:
# 1. Definindo dados pré-cadastrados (exemplo)
usuario_correto = "admin"
senha_correta = "1234"

# 1. Solicite usuário e senha
usuario_input = input("Digite o usuário: ")
senha_input = input("Digite a senha: ")

# 2. Verifique se os dados estão corretos
if usuario_input == usuario_correto and senha_input == senha_correta:
   # 3.1. Exiba: "Acesso permitido"
   print("Acesso permitido")
else:
   # 3.2. Exiba: "Acesso negado"
   print("Acesso negado")



# Atividade 04:
# 1. Receber 5 notas
notas = []
for i in range(1, 6):
   nota = float(input(f"Digite a nota {i}: "))
   notas.append(nota)

# 2. Calcular a média
media = sum(notas) / len(notas)

# 3. Classificar o aluno (considerando média 7.0 para aprovação)
if media >= 7.0:
   situacao = "Aprovado"
else:
   situacao = "Reprovado"

print(f"\nMédia: {media:.2f}")
print(f"Situação: {situacao}")


# Atividade 05:
while True:
   mensagem = input("Você: ").lower()

   if mensagem == "oi":
       print("Chatbot: Olá! Como posso ajudar?")
   elif mensagem == "tchau":
       print("Chatbot: Encerrando o programa... Até logo!")
       break
   else:
       print("Chatbot: Não entendi sua mensagem")


# Atividade 06:
# Lista de palavras consideradas positivas
palavras_positivas = ["bom", "ótimo", "excelente", "maravilhoso", "gostei", "legal", "massa"]
contador = 0
print("Digite palavras (ou 'sair' para encerrar):")

while True:
   palavra = input("> ").lower()
  
   if palavra == 'sair':
       break
  
   if palavra in palavras_positivas:
       contador += 1
print(f"\nTotal de palavras positivas encontradas: {contador}")


# Atividade 07:
# 1. Solicita a idade do usuário
idade = int(input("Digite a sua idade: "))

# 2. Utilize if/else para verificar o acesso
if idade >= 18:
   # 2.1 Permitir acesso se idade >= 18
   print("Acesso permitido.")
else:
   # 2.2 Negar acesso caso contrário
   print("Acesso negado.")
