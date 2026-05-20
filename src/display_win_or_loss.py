import  pygame


def display_win_screen():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Win Screen')

    # Setting colors
    black = (0, 0, 0)
    green = (0, 255, 0)

    # Dimensions for the loss display rectangle
    loss_display = pygame.Rect(250, 200, 300, 100)

    # Game loop
    run = True
    while run:
        # Fill the background color
        screen.fill(black)

        # Draw the rectangle
        pygame.draw.rect(screen, green, loss_display)

        # Render the text
        font = pygame.font.Font(None, 36)
        start_text = font.render('You are a Champion!', True, (0, 0, 0))

        # Center the text in the rectangle
        text_rect = start_text.get_rect(center=loss_display.center)
        screen.blit(start_text, text_rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
               return False

        # Update the display
        pygame.display.update()

    pygame.quit()

def display_loss_screen():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Loss Screen')

    # Setting colors
    black = (0, 0, 0)
    red = (255, 0, 0)

    # Dimensions for the loss display rectangle
    loss_display = pygame.Rect(250, 200, 300, 100)

    # Game loop
    run = True
    while run:
        # Fill the background color
        screen.fill(black)

        # Draw the rectangle
        pygame.draw.rect(screen, red, loss_display)

        # Render the text
        font = pygame.font.Font(None, 36)
        start_text = font.render('You Lost!', True, (0, 0, 0))

        # Center the text in the rectangle
        text_rect = start_text.get_rect(center=loss_display.center)
        screen.blit(start_text, text_rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

                # Update the display
        pygame.display.update()

    pygame.quit()
