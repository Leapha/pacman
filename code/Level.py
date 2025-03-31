import random
import pygame
from .Const import  COLOR_WHITE, COLOR_ORANGE

tamanho = 10
largura = 500
altura =  60
tela = pygame.display.set_mode((largura, altura))
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)



# Configurações da cobra
velocidade = 15


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name

    def desenhar_cobra(self, cobra):
        for segmento in cobra:
            pygame.draw.rect(self.window, (0, 255, 0), [segmento[0], segmento[1], 10, 10])

    @staticmethod
    def gerar_comida( self, cobra, largura, altura, tamanho):
        """Gera uma posição válida para a comida sem sobrepor a cobra."""
        while True:
            comida_x = random.randrange(0, largura - tamanho, tamanho)
            comida_y = random.randrange(0, altura - tamanho, tamanho)

            # Verifica se a comida está dentro da cobra
            if [comida_x, comida_y] not in cobra:
                return comida_x, comida_y

    def jogo(self):
        fim_jogo = False
        largura, altura = 500, 600
        x, y = largura // 2, altura // 2
        velocidade_x, velocidade_y = 0, 0
        cobra = [[x, y]]
        comprimento = 1


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

            # Verifica se comeu a comida
            if x == comida_x and y == comida_y:
                comida_x = random.randrange(0, largura - tamanho, tamanho)
                comida_y = random.randrange(0, altura - tamanho, tamanho)
            else:
                cobra.pop(0)

            # Verifica colisão com as bordas e consigo mesma
            if x < 0 or x >= largura or y < 0 or y >= altura or [x, y] in cobra[:-1]:
                continuar = self.game_over()
                if continuar:
                    self.jogo()
                else:
                    return

            # Atualiza a tela
            self.window.fill((179, 188, 7))
            self.desenhar_cobra(cobra)
            pygame.draw.rect(self.window, (255, 0, 0), [comida_x, comida_y, 10, 10])
            pygame.display.update()


            clock.tick(15)

    def game_over(self,):
        """Exibe a tela de Game Over com opções 'Sim' e 'Não'."""
        fonte = pygame.font.Font(None, 36)
        game_over_text = fonte.render("Game Over! Deseja continuar?", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(largura // 2 , altura // 2 - 50))

        opcoes = ["Sim", "Não"]
        opcao_selecionada = 0  # 0 = Sim, 1 = Não

        while True:
            self.window.fill((179, 188, 7))  # Fundo verde
            self.window.blit(game_over_text, game_over_rect)

            for i, opcao in enumerate(opcoes):
                cor = (COLOR_WHITE) if i == opcao_selecionada else (COLOR_ORANGE)  # Branco para selecionado, cinza para não selecionado
                texto = fonte.render(opcao, True, cor)
                texto_rect = texto.get_rect(center=(largura // 2 , altura // 2 + i * 50))
                self.window.blit(texto, texto_rect)

            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_DOWN:
                        opcao_selecionada = (opcao_selecionada + 1) % 2  # Alternate entre 0 e 1
                    elif evento.key == pygame.K_UP:
                        opcao_selecionada = (opcao_selecionada - 1) % 2  # Alternate entre 0 e 1
                    elif evento.key == pygame.K_RETURN:
                        return opcao_selecionada == 0

