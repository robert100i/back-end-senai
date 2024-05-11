import random

def escolherPalavra():
    palavras = ['python', 'programação', 'desenvolvimento', 'computador', 'algoritmo', 'openai']
    return random.choice(palavras)

def jogarForca():
    palavra = escolherPalavra()
    letrasCorretas = []
    letrasErradas = []
    tentativas = 6

    while True:
        palavraEscondida = ''.join([letra if letra in letrasCorretas else '_' for letra in palavra])
        print('\nPalavra: ', palavraEscondida)
        print('Letras usadas: ', ', '.join(letrasCorretas))
        print('Tentativas Restantes ', tentativas)
        
        if palavraEscondida == palavra:
            print('\nParabéns! Você venceu!')
            break

        
        if tentativas == 0:
            print('\n Gamer over! A palavra era: ', palavra)
            break

        letra = input('\n Digite uma letra: ').lower()

        if len(letra) != 1 or not letra.isalpha():
            print('Por favor, digite apenas uma letra.')
            continue
        
        if letra in letrasCorretas or letra in letrasErradas:
            print('Você já tentou essa letra. Tente outra.')
            continue

        if letra in palavra:
            print('Letra correta!')
            letrasCorretas.append(letra)
        else:
            print('Letra errada!')
            letrasErradas.append(letra)
            tentativas -= 1

if __name__ == '__main__':
    print ('Bem vindo ao jogo da forca!')
    jogarForca()