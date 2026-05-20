import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT

def start_and_stop_display():
    """
    Display a start/stop menu before a level begins.
    Returns True if the player clicks Start.
    Returns False if the player clicks Stop or closes the window.
    """
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Maze Game Menu")

    black = (0, 0, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)

    start_button = pygame.Rect(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 70, 100, 50)
    stop_button = pygame.Rect(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 + 10, 100, 50)

    font = pygame.font.Font(None, 36)

    while True:
        screen.fill(black)

        pygame.draw.rect(screen, green, start_button)
        pygame.draw.rect(screen, red, stop_button)

        start_text = font.render("Start", True, (0, 0, 0))
        stop_text = font.render("Stop", True, (0, 0, 0))

        screen.blit(start_text, (start_button.x + 22, start_button.y + 12))
        screen.blit(stop_text, (stop_button.x + 25, stop_button.y + 12))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    print("Level selected!")
                    return True

                if stop_button.collidepoint(event.pos):
                    print("Stop button clicked!")
                    return False

        pygame.display.update()