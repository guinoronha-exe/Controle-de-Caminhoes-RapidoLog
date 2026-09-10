import Caminhoes

def cadastro(listaEmail, listaSenha, i):
    print("="*30)
    nome_Usuario = input("Digite seu nome: ")
    while True:
        email_Cadastro = input("Digite o e-mail para cadastro: ").lower()
        if "@" in email_Cadastro:
            parte = email_Cadastro.split("@")
            if len(parte) == 2:
                usuario = parte[0]
                dominio = parte[1]
                if "." in dominio:
                    if dominio in ["gmail.com", "hotmail.com", "outlook.com"]:
                        print("Provedor validado\n")
                        break
                    else:
                        print("Provedor desconhecido")
                        continue
                else:
                    print("Sem ponto")
                    continue
            else:
                print("o E-mail está incorreto")
                continue
        else:
            print("Não possuí (@)")
            continue
        
    p = verificaCadastro(email_Cadastro, listaEmail, listaSenha, i) 

    if p == 0:

        senha_Cadastro = input("Digite a senha para cadastro: ")
        conf_Senha = input("Confirme a senha digitada: ")
        while senha_Cadastro != conf_Senha:
            print("\nA senha digitado está incorreto, digite novamente.")
            senha_Cadastro = input("Digite a senha para cadastro: ")
            conf_Senha = input("Confirme a senha digitada: ")
        if senha_Cadastro == conf_Senha:
            print("Senha confirmada\n")

        return nome_Usuario, email_Cadastro, senha_Cadastro

    else:
        print("Email já cadastrado")
        return


def verificaCadastro(email_Entrada, listaEmail, listaSenha, i):
    
    p = 0
    k = 0
    while k != i:
        
        if email_Entrada == listaEmail[k]:
            p = 1
            break
        k += 1
    
    return p



def entrada(listaEmail, listaSenha, i):
    
    email_Entrada = input("\nDigite seu Email: ")
    senha_Entrada = input("Digite sua Senha: ")
    
    p = 0
    k = 0
    while k != i:
        
        if email_Entrada == listaEmail[k] and senha_Entrada == listaSenha[k]:
            
            print("Parabéns você está logado")
            p = 2
            break
        k += 1
    
    return p


def caminhoes():

    while True:

        print("\n1. Visualizar caminhões disponiveis")
        print("2. Enviar caminhão para transporte")
        print("3. Retornar caminhão para Ala")
        print("4. Mudar caminhão de Ala")
        print("5. Retornar ao menu de Login")
        opc = int(input("Escolha uma opção: "))

        if opc == 1:
            Caminhoes.visualizar()

        elif opc == 2:
            Caminhoes.enviar()

        elif opc == 3:
            Caminhoes.retornar()

        elif opc == 4:
            Caminhoes.mudar()
            
        elif opc == 5:
            break
            