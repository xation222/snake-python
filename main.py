# configutações iniciais
import pygame
import random

pygame.init()

# criando tela
pygame.display.set_caption('Snake, the GAME')
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# parametros da cobra
tamanho_quadrado = 20
velocidade_jogo = 15


def gerarComida():
    x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
    return x, y


def desenharComida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho,
                                   tamanho])  # aqui somente é usado tamanho duas vezes, pq o objeto em questão é um quadrado, logo a altura e a largura são iguais


def desenharCobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branco, [pixel[0], pixel[1], tamanho, tamanho])


def desenharPontuacao(pontos):
    fonts = pygame.font.SysFont('Helvetica', 35)
    texto = fonts.render(f"Pontos: {pontos}", True, vermelho)
    tela.blit(texto, [1, 1])


def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y


def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerarComida()

    while not fim_jogo:
        tela.fill(preto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # atualizando posição
        x += velocidade_x
        y += velocidade_y
        pixels.append([x, y])  # criando movimentação visual
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        desenharCobra(tamanho_quadrado, pixels)
        desenharComida(tamanho_quadrado, comida_x, comida_y)
        desenharPontuacao(tamanho_cobra - 1)
        for pixel in pixels[:-1]:  # caso bate em si mesmo
            if pixel == ([x, y]):
                fim_jogo = True
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerarComida()
        pygame.display.update()
        relogio.tick(velocidade_jogo)


rodar_jogo()
