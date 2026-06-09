
# Questão 1: 
# Solicita os dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Calcula a soma
soma = num1 + num2

# Exibe o resultado
print(f"A soma dos números é: {soma}")

# Questão 2:
numero = int(input("Digite um número: "))

if numero % 2 == 0:
   print("O número é par")
else:
   print("O número é ímpar")


# Questão 3:
# Solicita as três notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média aritmética
media = (nota1 + nota2 + nota3) / 3

# Exibe o resultado
print(f"A média do aluno é: {media:.2f}")


# Questão 5:
# Solicita a nota do aluno
nota = float(input("Digite a nota do aluno: "))

# Estrutura condicional para verificar o desempenho
if nota >= 9.0:
   print("Desempenho excelente!")
elif nota >= 7.0:
   print("Desempenho bom!")
elif nota >= 5.0:
   print("Desempenho razoável!")
else:
   print("Desempenho insuficiente!")


# Questão 6:
# Solicita a nota ou número ao usuário
numero = float(input("Digite um número: "))

# Verifica as condições
if numero > 0:
   print("O número é positivo.")
elif numero < 0:
   print("O número é negativo.")
else:
   print("O número é zero.")


# Questão 7: 
# Pede o número ao usuário
numero = int(input("Digite um número para ver a tabuada: "))
print(f"\nTabuada de {numero}:")

# Loop de 1 a 10
for i in range(1, 11):
   resultado = numero * i
   print(f"{numero} x {i} = {resultado}")
