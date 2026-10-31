email = input("Digite seu e-mail: ")

if email.find("@") != -1:
    print("O e-mail possui @")
else:
    print("O e-mail não possui @")

# quantidade de caracteres
print("Quantidade de caracteres:", len(email))

# a posição do caractere @
print("A posição do caractere @ é:", email.find("@"))