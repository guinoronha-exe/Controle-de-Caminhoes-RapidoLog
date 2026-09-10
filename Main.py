import Entrada

listaNome = []
listaEmail = []
listaSenha = []

print("="*5, "Transportadora RápidoLog LTDA", "="*5)
while True:
    print("Cadastro: opção 1")
    print("Entrar: opção 2")
    print("Sair: opção 3")
    print("Escolha uma das opções acima", "\n"+"="*30)

    opcao = int(input("Digite uma das opções: "))

    if opcao == 1:
        i = len(listaEmail)
        resultado = Entrada.cadastro(listaEmail, listaSenha, i)

        if resultado == None:
            print("Tente Novamente \n"+"="*30)

        else:
            nome, email, senha = resultado
            listaNome.append(nome)
            listaEmail.append(email)
            listaSenha.append(senha)
            print("\nUsuário cadastrado com sucesso", "\n"+"="*30)      

    elif opcao == 2:
       
        i = len(listaEmail)
        p = Entrada.entrada(listaEmail, listaSenha, i)
        
        if p == 0:
            print("Algo deu errado, tente novamente")

        else:
            Entrada.caminhoes()

  
    
    elif opcao == 3:
        print("Obrigado pela preferência na RápidoLog!")
        break

    else:
        print("Opção invalida")