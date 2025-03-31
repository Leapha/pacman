import random

import pygame
import self

from .Const import COLORS, TILE_SIZE, tamanho, COLOR_BLACK, COLOR_WHITE, COLOR_ORANGE

largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Configurações da cobra
tamanho = 10
velocidade = 15

class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name

    def desenhar_cobra(self, cobra):
        for segmento in cobra:
            pygame.draw.rect(self.window, (0, 255, 0), [segmento[0], segmento[1], 10, 10])

    def criar_comida(self, cobra):
        """Cria comida em uma posição aleatória que não colida com a cobra"""
        comida_x = random.randrange(10, largura - 10, 10)
        comida_y = random.randrange(10, altura - 10, 10)

        # Garante que a comida não colida com a cobra
        while (comida_x, comida_y) in cobra:
            comida_x = random.randrange(10, largura - 10, 10)
            comida_y = random.randrange(10, altura - 10, 10)

        return comida_x, comida_y

    def verificar_colisao_com_comida(self, x, y, comida_x, comida_y):
        """Verifica se a cobra colidiu com a comida"""
        return x == comida_x and y == comida_y

    def verificar_colisao_com_cobra(self, x, y, cobra):
        """Verifica colisão com a própria cobra"""
        return (x, y) in cobra

    def jogo(self):
        fim_jogo = False
        largura, altura = 600, 400
        x, y = largura // 2, altura // 2
        velocidade_x, velocidade_y = 0, 0
        cobra = [[x, y]]
        comprimento = 1

        tempo_criacao_comida = pygame.time.get_ticks()
        mida_x, comida_y = self.criar_comida()
        comida_x = random.randrange(0, largura - 10, 10)
        comida_y = random.randrange(0, altura - 10, 10)

        clock = pygame.time.Clock()

        while not fim_jogo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_jogo = True
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT and velocidade_x == 0:
                        velocidade_x, velocidade_y = -10, 0
                    elif evento.key == pygame.K_RIGHT and velocidade_x == 0:
                        velocidade_x, velocidade_y = 10, 0
                    elif evento.key == pygame.K_UP and velocidade_y == 0:
                        velocidade_x, velocidade_y = 0, -10
                    elif evento.key == pygame.K_DOWN and velocidade_y == 0:
                        velocidade_x, velocidade_y = 0, 10

            x += velocidade_x
            y += velocidade_y
            cobra.append([x, y])

            if x == comida_x and y == comida_y:
                comprimento += 1
                comida_x = random.randrange(0, largura - 10, 10)
                comida_y = random.randrange(0, altura - 10, 10)
            else:
                cobra.pop(0)

            if x < 0 or x >= largura or y < 0 or y >= altura or [x, y] in cobra[:-1]:
                continuar = self.game_over()
                if continuar:
                    self.jogo()
                else:
                    return

                # Cria nova comida a cada 10 segundos
            if pygame.time.get_ticks() - tempo_criacao_comida >= 10000:  # 10000 ms = 10 segundos
                comida_x, comida_y = self.criar_comida()  # Cria nova comida
                tempo_criacao_comida = pygame.time.get_ticks()  # Atualiza o tempo de criação da comida

            self.window.fill((179, 188, 7))
            self.desenhar_cobra(cobra)
            pygame.draw.rect(self.window, (255, 0, 0), [comida_x, comida_y, 10, 10])
            pygame.display.update()


            clock.tick(15)

    def game_over(self,):
        """Exibe a tela de Game Over com opções 'Sim' e 'Não'."""
        fonte = pygame.font.Font(None, 36)
        game_over_text = fonte.render("Game Over! Deseja continuar?", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(largura // 2 - 60, altura // 2 + 20))

        opcoes = ["Sim", "Não"]
        opcao_selecionada = 0  # 0 = Sim, 1 = Não

        while True:
            self.window.fill((179, 188, 7))  # Fundo preto
            self.window.blit(game_over_text, game_over_rect)

            for i, opcao in enumerate(opcoes):
                cor = (COLOR_WHITE) if i == opcao_selecionada else (COLOR_ORANGE)  # Branco para selecionado, cinza para não selecionado
                texto = fonte.render(opcao, True, cor)
                texto_rect = texto.get_rect(center=(largura // 2 - 60, altura // 1.5 + i * 50))
                self.window.blit(texto, texto_rect)

            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_DOWN:
                        opcao_selecionada = (opcao_selecionada + 1) % 2  # Alterna entre 0 e 1
                    elif evento.key == pygame.K_UP:
                        opcao_selecionada = (opcao_selecionada - 1) % 2  # Alterna entre 0 e 1
                    elif evento.key == pygame.K_RETURN:
                        return opcao_selecionada == 0
        pygame.quit()
