import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, COLOR_WHITE, MENU_OPTION


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf =  pygame.image.load('./asset/pacmanmenu.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self, ):
        pygame.mixer_music.load('./asset/intermission.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(text_size=15, text="Aluna - Jamily RU:4569121",text_color=COLOR_WHITE, text_center_post= ((WIN_WIDTH / 2), 550))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_ORANGE, text_center_post= ((WIN_WIDTH / 2), 250 + 30 * i))

            pygame.display.flip()

        # check for all events
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End Pygame


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_post: tuple):
        text_font: Font = pygame. font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text,  True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_post)
        self.window.blit(source=text_surf, dest=text_rect)