import pygame
from pygame import Surface, Rect, image
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, COLOR_WHITE, MENU_OPTION


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf =  pygame.image.load('./asset/menusnake.jpg')
        self.surf = pygame.transform.scale(self.surf, (500, 300))
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/intermission1.wav')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.fill((179, 188, 7))
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=15, text="Aluna - Jamily RU:4569121",text_color=COLOR_WHITE, text_center_post= ((WIN_WIDTH / 2), 550))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_WHITE, text_center_post=((WIN_WIDTH / 2), 290 + 30 * i))
                else:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_ORANGE, text_center_post= ((WIN_WIDTH / 2), 290 + 30 * i))

         # check for all events
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End Pygame
                  if event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_DOWN:# DOWN KEY

                          if menu_option < len(MENU_OPTION) - 1:
                              menu_option += 1
                          else:
                              menu_option = 0
                      if event.key == pygame.K_UP:  #UP KEY
                          if menu_option > 0:
                              menu_option -= 1
                          else:
                              menu_option = len(MENU_OPTION) -1
                      if event.key == pygame.K_RETURN:  # ENTER
                          return MENU_OPTION[menu_option]

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_post: tuple):
        text_font: Font = pygame. font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text,  True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_post)
        self.window.blit(source=text_surf, dest=text_rect)