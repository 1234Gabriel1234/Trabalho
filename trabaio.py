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



     if escolha == 2
