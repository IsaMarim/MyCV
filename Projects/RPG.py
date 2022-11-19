#Autores: Caroline Taus, Isabela Marim, Nathalia Papst, Rebecca Mello

print("\nO jogo a seguir é baseado em escolhas que geram consequencias. A falha na resolução dos enigmas resulta na perda de pontos. Letras maiúsculas/minúsculas e acentos não fazem diferença nas respostas. Boa sorte!")

import random
gold = 150
erro = 0

nome = input("\nInsira seu nome: ") 

print("\n    Olá",nome+"! O ano é 3527, seu planeta natal foi destruído há séculos, e a humanidade já colonizou dezenas de novos planetas.") 

print("\n    Há algumas horas uma mensagem de Vinx Rangarth III foi transmitida para todo o universo. Nela foi revelado que sua falecida avó deixou como herança um valor inestimável que deve ser encontrado a partir da resolução de enigmas. O herdeiro garante que o primeiro a encontrar o tesouro receberá 50% dos ganhos.")

print("\n    Você como um famoso(a) caçador(a) de relíquias acredita que tem grandes chances de desvendar as pistas antes dos outros competidores.")

print("\033[1;93m")
print("\n---------------------")
print("   Gold = ", gold)
print("---------------------")
print("\033[0;0m")

print("\nVocê resolve ler a carta deixada pela avó de Rangarth")

print(" \n _________________________________________")
print("|                                         |")
print("|  Meu querido Vinx,                      |")
print("|                                         |")
print("|    Como é do seu conhecimento, meu      |")
print("|  maior sonho sempre foi que você se     |") 
print("|  tornasse um grande explorador das      |")
print("|  galáxias assim como seu falecido avô.  |") 
print("|  Para incentivá-lo deixei sua herança   |")
print("|  escondida em uma coletânea de enigmas  |") 
print("|  que após ser resolvida o levará ao     |") 
print("|  planeta em que o tesouro reside.       |") 
print("|  A primeira pista está no meu           |")
print("|  restaurante favorito, que tem o nome   |")
print("|  inspirado no restaurante do filme que  |")
print("|  sempre víamos quando você era criança, |") 
print("|  Toy Story.                             |")
print("|                     Com amor, sua Avó   |")
print("|_________________________________________|")

rest = input("\nDescubra o nome do restaurante: ") 

while (rest.lower() != "pizza planet"):
  gold = gold -10
  erro = erro + 1
  print("\033[1;93m")
  print("\n---------------------")
  print("   Gold = ", gold)
  print("---------------------")
  print("\033[0;0m")
  rest=input("\nTente novamente: ")

if rest.lower() == "pizza planet":
  print("\nCorreto! Você viaja até o planeta Terabithia onde o restaurante \033[0;32mPizza Planet\033[0;0m reside.")

print("\nVocê se aproxima da garçonete e ela pergunta qual é seu pedido, você:"
  "\n\n1. Pergunta onde você pode encontrar a próxima pista."
  "\n2. Pede um drink e depois pergunta. (-5 gold)"
  "\n3. Pede um drink e um lanche e depois pergunta. (-10 gold)")
  
a = int(input("\nDigite o número da sua escolha: "))

if a == 2: 
  gold = gold -5
  print("\033[1;93m")
  print("\n---------------------")
  print("   Gold = ", gold)
  print("---------------------")
  print("\033[0;0m")
if a == 3: 
  gold = gold -10
  print("\033[1;93m")
  print("\n---------------------")
  print("   Gold = ", gold)
  print("---------------------")
  print("\033[0;0m")


print("\nUm dado d20 será rolado para um teste de persuasão")
dado = random.randrange(1, 21)
print("Você tirou:", dado)

if a == 2:
  dado = dado+2

if a == 3:
  dado = dado+5

if dado >=17:
  print("\nA garçonete lhe entrega um papel.")
else:
  gold = gold-20
  print("\nA garçonete diz que a informação custará 20 gold. Você, com pressa de desvendar o caso, paga o valor. Ela lhe entrega um papel.")
  print("\033[1;93m")
  print("\n---------------------")
  print("   Gold = ", gold)
  print("---------------------")
  print("\033[0;0m")

print("\nNo papel está escrito:")

print("\n _________________________________________________")
print("|                                                 |")
print("|  -•••  ••  -•••  •-••  ••  ---  -  •  -•-•  •-  |")
print("|_________________________________________________|")

print("\n\nVocê percebe que a mensagem está codificada em código morse. Tendo a tabela de conversão, decodifique o texto.")

print("\n _______________________________")
print("|                               |")
print("| A = •-    B = -•••   C = -•-• |")
print("| D = -••   E = •      F = ••-• |")
print("| G = --•   H = ••••   I = ••   |")
print("| J = •---  K = -•-    L = •-•• |")
print("| M = --    N = -•     O = ---  |")
print("| P = •--•  Q = --•-   R = •-•  |")
print("| S = •••   T = -      U = ••-  |")
print("| V = •••-  W = •--    X = -••- |")
print("| Y = -•--  Z = --••            |")
print("|_______________________________|")

palavra = input("\nInsira aqui o texto: ") 


while (palavra.lower() != "biblioteca"):
  gold = gold -10
  erro = erro + 1
  print("\033[1;93m")
  print("\n---------------------")
  print("   Gold = ", gold)
  print("---------------------")
  print("\033[0;0m")
  palavra = input("\nTente novamente: ")

if palavra.lower() == "biblioteca":
  print("\nCorreto! Você já sabe sua próxima parada.")

print("\nVocê viaja até a \033[0;32mBiblioteca\033[0;0m central do universo, que guarda todos os livros e documentos já publicados na história e mostra a mensagem decodificada à bibliotecária robô, ela diz que sua próxima pista está em uma página do livro 'O Guia do Mochileiro das Galáxias'.")

print("\nPara descobrir em qual página abrir pense em um número o qual o dobro do seu antecessor, menos 3 é igual a 79:")
print("\na) 40")
print("b) 41")
print("c) 52")
print("d) 42")
d = (input("\nInsira a letra da resposta: "))

while (d.lower() != "d"):
  gold = gold -10
  erro = erro + 1
  print("\033[1;93m")
  print("\n---------------------")
  print("   Gold = ", gold)
  print("---------------------")
  print("\033[0;0m")
  d=input("\nTente novamente: ")

if d.lower() == "d":
  print("\nCorreto! Você já sabe que deve procurar na página \033[;32m42\033[0;0m.")

print("\nPara descobrir a palavra chave, resolva a equação do segundo grau abaixo sabendo que os resultados serão as coordenadas da palavra:")
print("\nX**2 - 9X + 8 = 0")

res1 = int(input("\nInsira o resultado da maior raiz: "))
res2 = int(input("Insira o resultado da menor raiz: "))

while (res1 != 8 and res2 != 1):
  gold = gold -10
  erro = erro + 1
  print("\033[1;93m")
  print("\n---------------------")
  print("   Gold = ", gold)
  print("---------------------")
  print("\033[0;0m")
  res1 = int(input("\nTente novamente (maior raiz): "))
  res2 = int(input("Tente novamente (menor raiz): "))

if (res1 == 8 and res2 == 1):
  print("\nCorreto! Você descobriu a linha e o número da palavra.")

print("\nVocê abre o livro na página 42, vai até a oitava linha e vê que a primeira palavra é \033[0;32mDeserto\033[0;0m. O planeta G34 é conhecido por seus intermináveis desertos e você acredita esse ser seu próximo destino.")

print("\nNesse planeta existe uma pirâmide guardada por uma esfinge. Para conseguir entrar, é preciso desvendar o seguinte enigma:")

print("\n ___________________________________")
print("|                                   |")
print("| O que é tão frágil que se quebra  |")
print("|       só de dizer seu nome?       |")
print("|___________________________________|")

enig = input("\nDigite a resposta: ")

while (enig.lower() != "silêncio") and (enig.lower() != "silencio"):
  gold = gold -10
  erro = erro + 1
  print("\033[1;93m")
  print("\n---------------------")
  print("   Gold = ", gold)
  print("---------------------")
  print("\033[0;0m")
  enig = input("\nTente novamente: ")

if (enig.lower() == "silêncio") or (enig.lower() == "silencio"): 
  print("\nAcertou! A palavra é \033[0;32mSilêncio\033[0;0m.")

print("\nA esfinge se move, abrindo uma passagem para entrar na pirâmide.")

print ("\nDentro da pirâmide, você se depara com um cofre com o tesouro de Vinx. No cofre há uma mensagem dizendo:")

print("\nA senha para abrir o cofre é a concatenação das letras iniciais em ordem alfabética de todas as palavras das pistas anteriormente encontradas seguida pelo número encontrado em uma das pistas.")

senha=input("\nInsira a senha: ")

while senha.lower() !='bdpps42':
  gold = gold -10
  erro = erro + 1
  print("\033[1;93m")
  print("\n---------------------")
  print("   Gold = ", gold)
  print("---------------------")
  print("\033[0;0m")
  senha=input("Tente novamente: ")

if senha.lower()=='bdpps42':
  print("\nParabéns",nome+"! Você encontrou o tesouro!") 

print("\n\nSua quantidade total de erros no jogo é de:", erro)

print("\nTabela de níveis:")
print(" ___________")
print("|           |")
print("|  Supremo  |")
print("|   Ótimo   |")
print("|    Bom    |")
print("|  Mediano  |")
print("|   Ruim    |")
print("|___________|")

if gold >= 130:
  print("\nSeu nível é: Supremo!")
elif gold >= 110 and gold < 130:
  print("\nSeu nível é: Ótimo!")
elif gold >= 90 and gold < 110:
  print("\nSeu nível é: Bom!")
elif gold >= 70 and gold < 90:
  print("\nSeu nível é: Mediano")
elif gold < 70:
  print("\nSeu nível é: Ruim, que pena!")