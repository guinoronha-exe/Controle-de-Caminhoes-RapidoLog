caminhao = [10, 10, 10, 10]



def visualizar():
    
    j = len(caminhao)
    print(j)
    for i in range(j):
        print(caminhao[i], "Caminhões na Ala", i + 1)

def enviar():
  
  while True:
  
    mandar = int(input("Quantos caminhões deseja enviar: "))
    ala = int(input("Da Ala 1, 2, 3 ou 4: "))

    if caminhao[ala - 1] - mandar < 0:

        print("Não há caminhões suficiente")

    else:
        if ala == 1:
            caminhao[0] = caminhao[0] - mandar
            break

        elif ala == 2:
            caminhao[1] = caminhao[1] - mandar
            break

        elif ala == 3:
            caminhao[2] = caminhao[2] - mandar
            break

        elif ala == 4:
            caminhao[3] = caminhao[3] - mandar
            break

        else:
            print("Ala inválida")


def retornar():
    
    while True:
  
        voltar = int(input("Quantos caminhões irão voltar: "))
        ala = int(input("Para a Ala 1, 2, 3 ou 4: "))

        if ala == 1:

            if voltar + caminhao[0] > 10:
                print("A Ala não suporta está quantidade (maximo 10)", caminhao[0] - 10)
            
            else:
                caminhao[0] = caminhao[0] + voltar
                break

        elif ala == 2:
            if voltar + caminhao[1] > 10:
                print("A Ala não suporta está quantidade (maximo 10)", caminhao[1] - 10)
            
            else:
                caminhao[1] = caminhao[1] + voltar
                break


        elif ala == 3:
           
            if voltar + caminhao[2] > 10:
                print("A Ala não suporta está quantidade (maximo 10)", caminhao[2] - 10)
            
            else:
                caminhao[2] = caminhao[2] - voltar
                break

        elif ala == 4:
           
            if voltar + caminhao[3] > 10:
                print("A Ala não suporta está quantidade (maximo 10)", caminhao[3] - 10)
            
            else:
                caminhao[3] = caminhao[3] - voltar
                break

        else:
            print("Ala inválida")

def mudar():
    
    while True:
        
        transferir = int(input("Quantos caminhões serão tranferidos: "))
        ala1 = int(input("Da Ala: "))
        ala2 = int(input("Para a Ala: "))

        if caminhao[ala1] - transferir < 0:
            print("Não há caminhões disponiveis")

        elif caminhao[ala2] + transferir > 10:
            print("A ala", ala2,"já esta cheia")
        
        else:
            caminhao[ala1] = caminhao[ala1] - transferir

            caminhao[ala2] = caminhao[ala2] + transferir