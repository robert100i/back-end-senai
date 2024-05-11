def imprimirTabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' | '.join(linha))
        print("-" * 9)

def verificarVitoria(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    
    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    
    return False

def jogoDaVelha():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogadores = ['X', 'O']
    jogadorAtual = 0

    print('Bem vindo ao jogo da velha')
    imprimirTabuleiro(tabuleiro)

    for _ in range(9):
        linha = int(input(f'Jogador {jogadores[jogadorAtual]}, digite a linha (0-2): '))
        coluna = int(input(f'Jogador {jogadores[jogadorAtual]}, digite a coluna (0-2): '))

        if tabuleiro[linha][coluna] != " ":
            print('Posição ocupada. Tente novamente.')
            continue

        tabuleiro[linha][coluna] = jogadores[jogadorAtual]
        imprimirTabuleiro(tabuleiro)

        if verificarVitoria(tabuleiro, jogadores[jogadorAtual]):
            print(f"Parabéns! Jogador {jogadores[jogadorAtual]} venceu!")
            break

        jogadorAtual = (jogadorAtual + 1) % 2

    else:
        print("Empate!")

if __name__ == '__main__':
    jogoDaVelha()