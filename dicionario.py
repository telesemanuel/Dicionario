# dicionario
usuario = {}

# Adicionar Chave
usuario["Nome"] = input("Informe o nome do usuário: ")

usuario["CPF"] = input("Informe o CPF do usuário: ")

usuario["RG"] = input("Informe o RG do usuário: ")

usuario["Data de Nascimento"] = input("Informe a data de nascimento do usuário (dd/mm/aaaa): ")

usuario["Sexo"] = input("Informe o sexo do usuário: ")

usuario["Signo"] = input("Informe o signo do usuário: ")

usuario["Mãe"] = input("Informe o nome da mãe do usuário: ")

usuario["Pai"] = input("Informe o nome do pai do usuário: ")

usuario["E-Mail"] = input("Informe o e-mail do usuário: ")

usuario["CEP"] = input("Informe o CEP do usuário: ")

usuario["Endereço"] = input("Informe o endereço do usuário: ")

usuario["Número"] = input("Informe o número do endereço do usuário: ")

usuario["Bairro"] = input("Informe o bairro do usuário: ")

usuario["Cidade"] = input("Informe a cidade do usuário: ")

usuario["Estado"] = input("Informe o estado do usuário: ")

usuario["Celular"] = input("Informe o celular do usuário: ")

usuario["Altura"] = input("Informe a altura do usuário (em cm): ")

usuario["Peso"] = input("Informe o peso do usuário (em kg): ")

usuario["Cor Favorita"] = input("Informe a cor favorita do usuário: ")


for chave in usuario:
    print(f"{chave}: {usuario.get(chave)}")


    