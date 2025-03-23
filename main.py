import pygame

print('Setup Stert')
pygame.init()
window = pygame.display.set_mode(size = (900,700))
print('Setup End')

print('Setup Start')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close Window
            quit() # End Pygame