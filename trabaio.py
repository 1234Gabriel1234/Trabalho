import os
from enum import Enum

class TipoDeAtivos (Enum):
    Notebook = 1
    Servidor = 2
    Roteador = 3
    Software = 4

arquivo = "registros.txt"

while True:
    print ("\n==== SISTEMA DE ATIVOS ====")
    print ("1- Cadastrar ativo")
    print ("2- Buscar ativo")
    print ("3- Atualizar ativo")
    print ("4- Deletar ativo")
    print ("5- Sair do programa")
    escolha = int(input("Selecione uma opção  "))

    if escolha == 5:
     print ("Saindo....")
     break
        
    if escolha == 1:
       id_ativo = int(input("Digite o ID do ativo  "))
       tipo_ativo = input("Digite o tipo do ativo  ")  #mudar isso aq pra enum
       marca_ativo = input("Digite a marca do ativo  ")
       responsavel_ativo = input("Digite o responsável pelo ativo  ")
       setor_ativo = input("Digite o setor  ")

  
