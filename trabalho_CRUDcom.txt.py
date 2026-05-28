import os
from enum import Enum

class TipoDeAtivos (Enum):
    Notebook = 1
    Servidor = 2
    Roteador = 3
    Software = 4

arquivo = "registros.txt"

#Gerador de ID 
if os.path.exists(arquivo):
 with open (arquivo, "r", encoding= "utf-8") as f:
  linhas = f.readlines()

 if len(linhas) > 0:
   
   ultima_linha = linhas [-1]
   ultimo_id = int(ultima_linha.split(";")[0])
   proximo_id = ultimo_id + 1
   

 else:
   proximo_id = 1


else:
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
     



     #CADASTRO
     elif escolha == 1:
       print ("\n Tipos de ativos")
       print (" 1- Notebook\n 2- Servidor\n 3- Roteador\n 4- Software")

       tipo_escolhido = int(input("Selecione o tipo do ativo  "))
       tipo_ativo = TipoDeAtivos(tipo_escolhido)

       id_ativo = proximo_id          #usando o gerador de id 
       

       marca_ativo = input("Digite a marca do ativo  ")
       responsavel_ativo = input("Digite o responsável pelo ativo  ")
       setor_ativo = input("Digite o setor  ")

       #Salva no txt com ; pra dividir os dados
       with open (arquivo, "a", encoding = "utf-8") as f:
         f.write(f"{id_ativo};{tipo_ativo.name};{marca_ativo};{responsavel_ativo};{setor_ativo}\n")
          #POSIÇÕES    0             1                2                 3                4
         
       proximo_id += 1
       
       print (f"Ativo cadastrado com sucesso!  {id_ativo};{tipo_ativo.name};{marca_ativo};{responsavel_ativo};{setor_ativo}")
       print (f"O ID de seu ativo é '{id_ativo}', utilize ele para ter acesso ao ativo mais tarde !")




     #BUSCAR
     elif escolha == 2:
       if not os.path.exists(arquivo):
         print ("Não existe ativos cadastrados ainda")     #Verifica .txt ja foi criado

       else:
         buscar_com_qual = int(input("Deseja buscar usando ID ou Nome do responsável ?\n\n1- Buscar por ID  2- Buscar por Nome"))   #Modo de busca

         if buscar_com_qual == 1:
          qual_id = int(input("Digite o ID do ativo  "))
          encontrado2 = False

          with open (arquivo, "r", encoding = "utf-8") as f:
            for linha in f:
              dados = linha.strip().split(";")

              if dados[0]  == str(qual_id):         #compara se é igual ao input (str pq o int no .txt se lê str)
                encontrado2 = True
                print (linha)
                break
                
             
          if not encontrado2:
           print ("ID não encontrado")

         elif buscar_com_qual == 2:
           qual_nomee = input("Digite o nome do responsável pelo ativo  ").lower()
           encontrado2 = False

           with open (arquivo, "r", encoding = "utf-8") as f:
             for linha in f:
               dados = linha.strip().split(";")

               if dados[3].lower() == qual_nomee:         #compara se é igual ao input
                 encontrado2 = True
                 print (linha)
             if not encontrado2:
              print ("Nome não encontrado !")

         else:
           print("Opção inválida !!")
           
     
     



     #ATUALIZAR
     elif escolha == 3:
         if not os.path.exists(arquivo):
          print ("Não existe ativos cadastrados ainda")      #Verifica .txt ja foi criado

         else:
          update_ativo = int(input("Digite o ID do ativo que gostaria de atualizar  "))       #guarda o id digitado

          linhas_atualizadas = []     #Variaveis pra usar mais tarde
          encontrado = False

          with open (arquivo, "r", encoding="utf-8") as f:
            for linha in f:
              dados = linha.strip().split(";")


              if dados [0] == str(update_ativo):             #se ID bater, continua (str pq o int no .txt se lê str)
               encontrado = True  
               print (f"Status atual do ativo  {linha}")   

               update_qual = int(input ("Qual categoria deseja alterar ?\n 1- Tipo do ativo\n 2- Marca do ativo\n 3- Responsável do ativo\n 4- Setor do ativo\n  "))

               #Update tipo
               if update_qual == 1:                    #Tipo ta em enum, ent preciso de um int aq, diferente dos outros q é input
                print ("\n Tipos de ativos")
                print ("1- Notebook\n 2- Servidor\n 3- Roteador\n 4- Software")        #lista os tipos disponíveis
 
                tipo_escolhido2 = int(input("Digite o número de qual tipo de ativo deseja alterar  "))
                tipo_ativo2 = TipoDeAtivos (tipo_escolhido2)             #Salva de acordo com a tabela enum

                dados [1] = tipo_ativo2.name


               #Update marca
               elif update_qual == 2:
                marca_update = input("Digite por qual marca deseja alterar o ativo  ")
                dados [2] = marca_update
                

               #Update responsável
               elif update_qual == 3:
                responsavel_update = input("Digite por qual responsável deseja alterar o ativo  ")
                dados [3] = responsavel_update

               #Update setor
               elif update_qual == 4:
                setor_update = input("Digite por qual setor deseja alterar o ativo  ")
                dados [4] = setor_update


               #Opção invalida
               else:                
                print ("Selecione uma opção válida !")


              #criando as variaveis para usar no w (dentro do for)
              nova_linha = ";".join(dados)
              linhas_atualizadas.append(nova_linha + "\n")


         #salvando os dados coletados fora do for pra n apagar tudo
          with open (arquivo, "w", encoding="utf-8") as f:
             f.writelines(linhas_atualizadas)

        
          # usando o encontrado true aq, para pop mensagem de sucesso pegando todos os if 
          if encontrado:
              print ("Ativo atualizado com sucesso !")
          else:
             print ("ID não encontrado !")






     #DELETAR
     elif escolha == 4:             
       if not os.path.exists(arquivo):     
        print ("Nenhum ativo cadastrado até o momento !")  
        encontrado3 = False

       else:  
        selecione_id = int(input("Digite o ID do ativo que deseja excluir"))
        linhas_restantes = []     #Variaveis pra usar mais tarde
        encontrado3 = False

        with open (arquivo, "r", encoding="utf-8") as garchomp:
            for linha in garchomp:
              dados = linha.strip().split(";")

         
              if dados [0] == str(selecione_id):             #se ID bater, continua (str pq o int no .txt se lê str)
                  encontrado3 = True  
                  certeza_delete = int(input(f"Tem certeza que deseja excluir o ativo cadastrado ?\n{linha}\n\n 1- SIM   2-NÃO"))

                  if certeza_delete == 1:
                    print ("Ativo Deletado com sucesso !")
                    
                    continue    #continue pra igonarar a linha apagada e so reescrever o resto
                  else:
                    print ("Exclusão cancelada !")
              linhas_restantes.append(linha)
                 
         # reescreve o arquivo
        with open(arquivo, "w", encoding="utf-8") as v:

            v.writelines(linhas_restantes)

        if not encontrado3:

            print("ID não encontrado!")
        
     
     else:
       print ("Selecione uma opção válida !")

     #tratamento de erro
    except ValueError:
      print ("Selecione apenas números !")
         

       #FAZER MENSAGEM DE '....COM SUCESSO NO FINAL DE CADA FUNÇÃO
       #tem q criar cadastro pras vulnerabilidades, varias vul pro msm ativo
      #tratar inputs vazios
      #as vul tem q ter categoria e nivel de risco
