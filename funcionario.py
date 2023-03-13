import json


# Criando a função add que será responsavel por receber os dados dos funcionários e inserir no db que no caso será armazenado em json
def add_data():
    # Recebe por os dados do funcionario
    nome = input("Nome do Funcionario: ")
    idade = input("Idade do Funcionario: ")
    cargo = input("Cargo que ocupa: ")

    # Insere como está no bando de dados json
    inserirFuncionario = {
        "Nome do Funcionario: ": nome,
        "Idade Do Funcionario": idade,
        "Cargo que ocupa: ": cargo
    }

    with open("funcionario.json", "r") as getdata:
        data = json.load(getdata)  # Convertendo Json em Python

        data[nome] = inserirFuncionario

        with open("funcionario.json", "w") as save:
            json.dump(data, save)  # Convertendo Python para Json
            print("Funcionario adicionado com sucesso!!!")


def view_data():

    with open("funcionario.json", "r") as view:
        data = json.load(view)

        for i, m in data.items():
            print("\n =-=-=-=-=-=-=-=--=-=-=-=-=-=-=")
            for x, n in m.items():
                print(x, n)


def delete_data():

    nome = input("Entre com o nome do funcionario: ")

    with open("funcionario.json", "r") as getdata:
        data = json.load(getdata)

        if nome in data:
            data.pop(nome)
            with open("funcionario.json", "w") as delete:
                data1 = json.dump(data, delete)
                print("Apagado com sucesso")


def update_data():
    nome = input("Entre com o nome do funcionario: ")

    with open("funcionario.json", "r") as getdata:
        data = json.load(getdata)

        if nome in data:
            nome = input("Edite o nome: ")
            idade = input("Edite a idade: ")
            cargo = input("Edite o cargo ocupado: ")

            atualizarFuncionario = {
                "Nome do Funcionario: ": nome,
                "Idade Do Funcionario": idade,
                "Cargo que ocupa: ": cargo
            }

            data[nome] = atualizarFuncionario
            with open("funcinario.json", "w") as update:
                json.dump(data, update)
                print("Alterações feitas com sucesso!")


def main():
    print("\n1. Inserir Funcionario:")
    print("\n2. Visualizar Funcionarios:")
    print("\n3. Delete Funcionario:")
    print("\n4. Editar Funcionario:")
    print("\n5. Sair:\n")

    escolha = int(input("Faça sua escolha:"))

    if escolha == 1:
        add_data()
    elif escolha == 2:
        view_data()
    elif escolha == 3:
        delete_data()
    elif escolha == 4:
        update_data()
    elif escolha == 5:
        quit()
    else:
        print("ERRO")


main()
