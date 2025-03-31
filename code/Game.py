import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Jogo da Cobrinha")

    def run(self):
        while True:
            # Exibe o menu e aguarda o retorno da escolha do menu


            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0]]:
                # Se a opção escolhida for a de iniciar o jogo, cria o nível e inicia o jogo
                level = Level(self.window, 'Level1')
                level.jogo()  # Chama o método de jogo da classe Level
            elif menu_return == MENU_OPTION[3]:
                # Se a opção for "Sair", fecha o jogo
                pygame.quit()
                quit()
            else:
                # Caso haja outras opções, pode adicionar mais lógica aqui
                pass







