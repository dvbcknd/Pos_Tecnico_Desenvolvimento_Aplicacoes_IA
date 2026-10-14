
#Atv1 
nome = input("Qual é o seu nome? ")
idade = input("Qual a sua idade? ")
cidade = input("Qual a sua cidade? ")

print(f"O seu nome é {nome}, sua idade é {idade} e você mora em {cidade}")
print("\n\n")
#####################

#Atv 2
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"Selecione as seguintes opções de conta:")
opcao = int(input("1 = Somar | 2 = Subtrair | 3 = Multiplicar | 4 = Dividir: "))

match opcao:
    case 1:
        print(f"A soma de {num1} + {num2} = {num1 + num2}")
    case 2:
        print(f"A subtração de {num1} - {num2} = {num1 - num2}")
    case 3:
        print(f"A multiplicação de {num1} * {num2} = {num1 * num2}")
    case 4:
        print(f"A divisão de {num1} / {num2} = {num1 / num2}")
    case _:
       print("A opção selecionada é inválida.")
print("\n\n")
#####################

#Atv3
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"\nAluno: {nome}")
print(f"Média: {media:.1f}")
print(f"Situação Final: {situacao}")
#####################

#Atv4
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O primeiro número ({num1}) é maior.")
elif num2 > num1:
    print(f"O segundo número ({num2}) é maior.")
else:
    print("Os dois números são iguais.")
#####################


#Atv5
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
#####################


#Atv6
try:
    idade = int(input("Digite a sua idade: "))

    if idade < 0:
        print("Idade inválida.")
    elif idade < 12:
        print("Classificação: Criança")
    elif idade <= 17:
        print("Classificação: Adolescente")
    elif idade <= 59:
        print("Classificação: Adulto")
    else:
        print("Classificação: Idoso")

except ValueError:
    print("Por favor, digite um número inteiro válido.")
#####################


#Atv07
usuario_cadastrado = "admin"
senha_cadastrada = "1234"

usuario_input = input("Digite o seu usuário: ")
senha_input = input("Digite a sua senha: ")

if usuario_input == usuario_cadastrado and senha_input == senha_cadastrada:
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos.")
#####################


#Atv08
print("Menu:")
print("1 - Opção Um")
print("2 - Opção Dois")
print("3 - Opção Três")

opcao = int(input("Escolha uma opção: "))

match opcao:
    case 1:
        print("Você escolheu a Opção Um.")
    case 2:
        print("Você escolheu a Opção Dois.")
    case 3:
        print("Você escolheu a Opção Três.")
    case _:
        print("Opção inválida!")
#####################


#Atv09
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Digite o número da operação desejada (1-4): ")

match opcao:
    case "1":
        resultado = num1 + num2
        print(f"\nResultado da Soma: {resultado}")
    case "2":
        resultado = num1 - num2
        print(f"\nResultado da Subtração: {resultado}")
    case "3":
        resultado = num1 * num2
        print(f"\nResultado da Multiplicação: {resultado}")
    case "4":
        # Validação para evitar a divisão por zero
        if num2 != 0:
            resultado = num1 / num2
            print(f"\nResultado da Divisão: {resultado}")
        else:
            print("\nErro: Não é possível dividir por zero.")
    case _:
        print("\nOpção inválida! Por favor, escolha um número de 1 a 4.")
#####################


#Atv10
valor_original = float(input("Digite o valor da compra (R$): "))

if valor_original <= 100:
    porcentagem_desconto = 0
elif valor_original <= 500:
    porcentagem_desconto = 10
else:
    porcentagem_desconto = 20

desconto = valor_original * (porcentagem_desconto / 100)
valor_final = valor_original - desconto

print(f"\n--- Resumo do Desconto ---")
print(f"Valor original: R$ {valor_original:.2f}")
print(f"Desconto ({porcentagem_desconto}%): R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
#####################



#Atv11 - Sistema escolar
opcao = 0

while opcao != 4:
    print("\n===== SISTEMA ESCOLAR =====")
    print("1 - Calcular média")
    print("2 - Verificar aprovação")
    print("3 - Verificar maior nota")
    print("4 - Sair")
    
    opcao = int(input("\nEscolha uma opção (1-4): "))
    
    match opcao:
        case 1:
            print("\n--- Calcular Média ---")
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))
            media = (nota1 + nota2) / 2
            print(f"A média aritmética é: {media:.2f}") 
        case 2:
            print("\n--- Verificar Aprovação ---")
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))
            media = (nota1 + nota2) / 2
            
            # Critério padrão: aprovado se média for maior ou igual a 7.0
            if media >= 7.0:
                print(f"Média: {media:.2f} -> Aluno APROVADO!")
            elif media >= 5.0:
                print(f"Média: {media:.2f} -> Aluno em RECUPERAÇÃO!")
            else:
                print(f"Média: {media:.2f} -> Aluno REPROVADO!")      
        case 3:
            print("\n--- Verificar Maior Nota ---")
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))
            
            if nota1 > nota2:
                print(f"A maior nota é a primeira: {nota1:.2f}")
            elif nota2 > nota1:
                print(f"A maior nota é a segunda: {nota2:.2f}")
            else:
                print("As duas notas são iguais!")            
        case 4:
            print("\nEncerrando o sistema. Até logo!")
        case _:
            print("\nOpção inválida! Por favor, escolha um número de 1 a 4.")
#####################