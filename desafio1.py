mensagem = input("Digite uma mensagem: ")

print("Quantidade de caracteres:", len(mensagem))

posicao = mensagem.find("erro")

if posicao != -1:
    print("A palavra erro foi encontrada na posição:", posicao)
else:
    print("A palavra erro não foi encontrada")
