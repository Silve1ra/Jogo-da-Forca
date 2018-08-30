#!/usr/bin/python
# -*- coding: utf-8 -*-
#

"""
    Jogo da Forca em python.
    Para executar basta acessar o diretorio em que o arquivo main.py esta localizado e executar no terminal o seguinte codigo:
    python main.py
    

    Name: main.py
    Autor: Felipe Silveira Brito Borges ( eng.fe.silveira@gmail.com )
"""

FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def main():
    """
    Funcao para executar o jogo
    """

    print("Bem vindo ao Jogo da Forca!!")
    palavra = input("Digite a palavra secreta: ")
    for x in range(999):
        print()

    tentativas = [] #vetor para guardar as letras das tentativas
    acertos = [] #vetor para ir salvando as letras de acertos
    erros = 0

    global FORCAIMG

    global jogando
    jogando = True

    while jogando:
        palavraSecreta = ""

        for letra in palavra:
            palavraSecreta += letra if letra in acertos else "_ "

        print(palavraSecreta)

        if palavraSecreta == palavra:
            print("Você acertou!")
            break
        
        tentativa = input("\nDigite alguma letra: ")

        if tentativa in tentativas:
            print("Você já tentou essa letra!")
            continue
        else:
            tentativas += tentativa
            if tentativa in palavra:
                acertos += tentativa
            else:
                erros += 1
                print("Você errou!")
        
        print(FORCAIMG[erros]+'\n')
        if erros == 6:
            print("Enforcado!")
            break

if __name__ == "__main__":
    main()