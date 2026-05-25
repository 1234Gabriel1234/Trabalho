import os
from enum import Enum

class TipoDeAtivos (Enum):
    Notebook = 1
    Servidor = 2
    Roteador = 3
    Software = 4

arquivo = "registros.txt"
proximo_id = 1

while True:
    #MENU
    print ("\n==== SISTEMA DE ATIVOS ====")
    print ("1- Cadastrar ativo")
    print ("2- Buscar ativo")
    print ("3- Atualizar ativo")
    print ("4- Deletar ativo")
    print ("5- Sair do programa")

    try:
     
     escolha = int(input("Selecione uma opção  ")) 

     if escolha == 5:
      print ("Saindo....")
      break
     



     #cadastro
     if escolha == 1:
       print ("\n Tipos de ativos")
       print ("1- Notebook\n 2- Servidor\n 3- Roteador\n 4- Software")

       tipo_escolhido = int(input("Selecione o tipo do ativo  "))
       tipo_ativo = TipoDeAtivos(tipo_escolhido)

       id_ativo = proximo_id                                                    #gerador de id
       proximo_id += 1

       marca_ativo = input("Digite a marca do ativo  ")
       responsavel_ativo = input("Digite o responsável pelo ativo  ")
       setor_ativo = input("Digite o setor  ")

       #Salva no txt com ; pra dividir os dados
       with open (arquivo, "a", encoding = "utf-8") as f:
         f.write(f"{id_ativo};{tipo_ativo.name};{marca_ativo};{responsavel_ativo};{setor_ativo}\n")
          #POSIÇÕES    0             1                2                 3                4





     #Buscar
     elif escolha == 2:
       if not os.path.exists(arquivo):
         print ("Não existe ativos cadastrados ainda")      #Verifica .txt ja foi criado

       else:
         qual_id = int(input("Digite o ID do ativo  "))
         with open (arquivo, "r", encoding = "utf-8") as f:
           for linha in f:
             dados = linha.strip().split(";")
             dados [0]                                      #pega o primeiro dado da lista (ID)

             if dados[0]  == qual_id:                           #compara se é igual ao input
               print (linha)
               break
             
             else:
               print ("Este ID não existe !")




     #atualizar
     elif escolha == 3:
         if not os.path.exists(arquivo):
          print ("Não existe ativos cadastrados ainda")      #Verifica .txt ja foi criado

         else:
          update_ativo = int(input("Digite o ID do ativo que gostaria de atualizar  "))       #guarda o id digitado
          with open (arquivo, "r", encoding="utf-8") as f:
            for linha in f:
              dados = linha.strip().split(";")
              dados [0]          

              if not dados == update_ativo:                   #se ID não bater, para
               print ("O ID digitado não corresponde")       #|||||||||||||||||||||
              else:                                           #Se bater, continua com o update
               print (f"Status atual do ativo  {linha}")        
               update_qual = int(input ("Qual categoria deseja alterar ?\n 1- Tipo do ativo\n 2- Marca do ativo\n 3- Responsável do ativo\n 4- Setor do ativo\n  "))
              
              #Update tipo
               if update_qual == 1:                    #Tipo ta em enum, ent preciso de um int aq, diferente dos outros q é input
                print ("\n Tipos de ativos")
                print ("1- Notebook\n 2- Servidor\n 3- Roteador\n 4- Software")        #lista os tipos disponíveis
 
               tipo_escolhido2 = int(input("Digite o número de qual tipo de ativo deseja alterar  "))
               tipo_ativo2 = TipoDeAtivos (tipo_escolhido2)             #Salva de acordo com a tabela enum

               with open (arquivo, "w", encoding="utf-8") as f:
                 f.write [1(tipo_ativo2.name)]   # <VERIFICAR SE ISSO TA ESCRITO CERTO DPS
  

              #Update marca
               if update_qual == 2:
                marca_update = input("Digite por qual marca deseja alterar o ativo  ")
                dados [2] = marca_update
                nova_linha = ";".join(dados)

              #Update responsável
               if update_qual == 3:
                responsavel_update = input("Digite por qual responsável deseja alterar o ativo  ")
                dados [3] = responsavel_update
                nova_linha = ";".join(dados)

              #Update setor
               if update_qual == 4:
                setor_update = input("Digite por qual setor deseja alterar o ativo  ")
                dados [4] = setor_update
                nova_linha = ";".join(dados)

              #Opção invalida
               else:
                print ("Selecione uma opção válida !")




     elif escolha == 4:
       

       #FAZER MENSAGEM DE '....COM SUCESSO NO FINAL DE CADA FUNÇÃO
       #CAPS NAS MAINS
       #O UPDATE TA ERRADO, TEM Q ARRUMAR O FINAL DE CADA IF DO UPDATE


       

