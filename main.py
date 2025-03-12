# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game():
    pygame.init()
    pygame.font.init
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def draw_text(screen, text, font_size, color, x, y, font_name, italic=False, bold=False, rotation=0):
    if font_name:
        font = pygame.font.Font(font_name, font_size)
    else:
        font = pygame.font.Font(None, font_size)
    
    font.set_bold(bold)
    font.set_italic(italic)
    
    text_surface = font.render(text, True, color)

    if rotation != 0:
        text_surface = pygame.transform.rotate(text_surface, rotation)

    text_rect = text_surface.get_rect(center=(x,y))
    screen.blit(text_surface, text_rect.topleft)
        
def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here
    running = True
    while running:
        running = handle_events()
        screen.fill(config.GREEN) # Use color from config

        draw_text(screen, 'Hello', 50, config.CYAN, 300, 200, 'c:\Font\PlaywriteHU-VariableFont_wght.ttf', italic=True)
        draw_text(screen, 'YO!', 70, config.BLACK, 300, 400, None, bold=True, rotation=40)
        draw_text(screen, 'Whats GOOD', 90, config.PURPLE, 600, 300, 'c:\Font\BigShouldersInline-VariableFont_opsz,wght.ttf', italic=True, bold=True, rotation=180 )

        pygame.display.flip()

        # Limit the frame rate to the specified frames per second
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



