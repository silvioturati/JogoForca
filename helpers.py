import random
from config import ARQUIVO_PALAVRAS, TENTATIVAS_ADCIONAIS


def sortear_palavra():
    """
    Função para randomicamente selecionar uma palavra do arquivo texto
    :return: uma palavra aleatória
    """
    with open(ARQUIVO_PALAVRAS) as obj:         # abre o arquvio
        palavras = obj.read().splitlines()      # lê o arquivo e tira os espaços vazios de final de linha
    return random.choice(palavras)              # usa a função random para escolher uma palavra aleatóriamente


def verificar_letra_informada(palavra, suas_tentativas, tentativa):
    """
    Verifica se a letra dada está correta
    :param palavra: gerada com base no arquivo texto de palavras secretas
    :param suas_tentativas: lista com todas as tentativas
    :param tentativa: letra inserida nesta jogada
    :return: retorna um status
    """
    status = ''  # O status precisa ser zerado toda vez que a função for chamada
    acertos = 0  # os acertos também precisa zerar toda vez

    # percorre cada letra da palavra comparando a letra da palavra com a letra da lista de tentativas
    for letra in palavra:
        if letra.lower() in suas_tentativas:    # se a letra atual da palavra está na lista imprime a letra
            status += letra
        else:
            status += '*'                       # se não está na lista de tentativas, então imprime *

        if letra.lower() == tentativa.lower():  # conta quantas veses acertou a çetra em determinado chute
            acertos += 1

    print(f" - Acertou {acertos} letra(s) '{tentativa}'")
    return status


def total_tentativas(palavra):
    """
    define a quantiade de tantivas de acordo com a palavra escolhida
    :param palavra: gerada aleatóriamente
    :return: quantidade de tentativas
    """
    chances = len(palavra)
    return chances + TENTATIVAS_ADCIONAIS


def jogo(palavra):
    """
    Função principal do jogo
    :param palavra: palavra gerada aleatoriamente a partir do arquivo de palavras
    :return: resultados
    """
    chute = 0                                        # variavel que incrementa conforme o usuario chuta uma letra
    suas_tentativas = []                             # lista de letras que já foram chutadas
    chances = total_tentativas(palavra)              # usa a função total_tentivas para definir a quantidade de tentivas
    total_chances = chances                          # guarda o total inicial de chances

    print(f"- Total de chances: {chances}")
    while chute < total_chances:                      # verifica se o usuario já não usou todas as tentativas
        letra_tentativa = input("\nDigite sua letra: ")
        chances -= 1                                  # decrementa a quantidade de chances para avisar o usuario

        if letra_tentativa in suas_tentativas:        # a letra já foi informada ou advinhada?
            print(f"ATENÇÃO: Você já digitou essa letra")
            pass
        elif len(letra_tentativa) == 1:               # o usuario só pode digitar uma letra apenas
            suas_tentativas.append(letra_tentativa)   # adcionando as letras na lista de letras chutadas
            resultado = verificar_letra_informada(palavra, suas_tentativas, letra_tentativa)
            if resultado == palavra:
                print(f"\nParabéns, você venceu. A palavra é: {palavra}")
                break
            else:
                print(f" - {' '.join(resultado)}")
        else:
            print(f"Entrada incorreta, informe apenas 1 letra!")

        print(f" - Tentivas restantes: {chances}")      # mostra quantas tentivas restantes
        chute += 1                                      # incrementa a quantidade de chutes
    if chute == total_chances:
        print(f"\nSuas tentativas acabaram. A palavra secreta é: {palavra}.")
