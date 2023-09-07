import pygame

conf = {
    'bg_color': (0, 0, 0),
    'grid_color': (255, 255, 255),
    'restart_button_color': (80, 80, 80),
    'set_caption': 'Jogo da Velha',
    'width': 600,
    'height': 700
}

pygame.init()

pygame.display.set_caption(conf['set_caption'])

altura, largura = conf['height'], conf['width']
tela = pygame.display.set_mode((largura, altura))
def inicia_tela():
    tela.fill(conf['grid_color'])

tamanho_quadrado = largura/3

def desenha_tabuleiro(windows):
    for i in {1, 2}:
        pygame.draw.line(windows, conf['bg_color'], (tamanho_quadrado*i, 0), (tamanho_quadrado*i, tamanho_quadrado*3), 3)
        pygame.draw.line(windows, conf['bg_color'], (0, tamanho_quadrado*i), (tamanho_quadrado*3, tamanho_quadrado*i), 3)

def desenha_na_tela(tabuleiro):
    i = 0
    for linha in tabuleiro:
        j = 0
        for coluna in linha:
            player = coluna if coluna != 'n' else ' '
            fonte = pygame.font.SysFont('Helvetica', 120)
            texto = fonte.render(player, True, conf['bg_color'])
            x = i * tamanho_quadrado
            y = j * tamanho_quadrado
            tela.blit(texto, (x + 70, y + 30))
            j += 1
        i += 1

def desenha_botao_reiniciar(windows):
    altura_do_botao = conf['height'] - (tamanho_quadrado*3)
    altura_do_tabuleiro = tamanho_quadrado*3
    pygame.draw.rect(windows, conf['restart_button_color'], [0, altura_do_tabuleiro, conf['width'], altura_do_botao])
    y = tamanho_quadrado * 3
    fonte = pygame.font.SysFont('Helvetica', 60)
    texto = fonte.render('Reiniciar', True, conf['bg_color'])
    tela.blit(texto, [205, altura_do_tabuleiro+10])

def marca_grid(tabuleiro, caractere, i, j):
    if (i < 3 and j < 3) and tabuleiro[i][j] == 'n':
        print(i, j)
        tabuleiro[i][j] = caractere
        return True
    return False

def diagonal_principal(tabuleiro):
    return [tabuleiro[i][i] for i in range(3)]

def diagonal_secundaria(tabuleiro):
    return [tabuleiro[i][2-i] for i in range(3)]

def coluna(tabuleiro, index):
    return [tabuleiro[n][index] for n in range(3)]

def linha(tabuleiro, index):
    return tabuleiro[index]

def checa(list_elem):
    set_elem = set(list_elem)
    if 'n' not in set_elem and len(set(set_elem)) == 1:
        return True
    return False

def eh_vencedor(tabuleiro):
    for i in range(3):
        if checa(linha(tabuleiro, i)) or checa(coluna(tabuleiro, i)):
            return True

    if checa(diagonal_principal(tabuleiro)) or checa(diagonal_secundaria(tabuleiro)):
        return True
    return False

def eh_velha(tabuleiro):
    for linha in tabuleiro:
        for elemento in linha:
            if elemento == 'n':
                return False
    return True


def roda_partida():
    grid = [
        ['n', 'n', 'n'],
        ['n', 'n', 'n'],
        ['n', 'n', 'n'],
    ]
    inicia_tela()
    end_game = False
    player = 'x'

    while not end_game:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end_game = True
            elif evento.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                i = int(pos[0] / tamanho_quadrado)
                j = int(pos[1] / tamanho_quadrado)
                if marca_grid(grid, player, i, j):
                    desenha_na_tela(grid)
                    if eh_vencedor(grid) or eh_velha(grid):
                        end_game = True
                    if player == 'x':
                        player = 'o'
                    elif player == 'o':
                        player = 'x'
                else:
                    continue

        desenha_tabuleiro(tela)
        desenha_botao_reiniciar(tela)
        pygame.display.update()

def main():
    roda_partida()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return
            elif evento.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[1] > 600:
                    roda_partida()

main()
