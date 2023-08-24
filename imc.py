# Função para calcular o IMC
def calcular_imc(peso, altura):
    altura_metros = altura / 100  # Convertendo altura de centímetros para metros
    imc = peso / (altura_metros ** 2)
    return imc

# Solicita ao usuário que insira peso e altura
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em cm: "))

# Calcula o IMC
imc = calcular_imc(peso, altura)

# Exibe o resultado
print("Seu IMC é: {:.2f}".format(imc))

# Interpretando o IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Seu peso está normal.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está obeso.")