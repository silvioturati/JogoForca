"""
Jogo da forca. Para alterar as palavras, edite o arquivo palavras.txt com as palavras para o jogo
"""

from helpers import sortear_palavra, jogo

if __name__ == '__main__':
    palavra = sortear_palavra()

    # Imprime a palavra escondida com *
    print("\n--------- Jogo da Forca ---------")
    print("\nPalavra é: ")
    for letra in palavra:
        print("*", end=" ")

    # Calculando tamanho da palavra
    tamanho_palavra = len(palavra)
    print(f"\n - A palavra tem {tamanho_palavra} letras")

    jogo(palavra)
