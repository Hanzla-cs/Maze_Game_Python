import sys
import pygame
from collision import pixel_collision
from menu import start_and_stop_display
from config import asset_path, WINDOW_WIDTH, WINDOW_HEIGHT


def level2():
    """
    The player navigates through a simple maze to escape, avoiding walls and the door.
    """
    start_and_stop_display()
    # Initializing pygame
    pygame.init()

    # Load assets
    # Load original Level 2 map
    original_map = pygame.image.load(asset_path("maps", "level 2 map.png")).convert_alpha()
    original_width, original_height = original_map.get_size()

    # Scale map to the same fixed window size used by the menu and Level 1
    map_image = pygame.transform.smoothscale(original_map, (WINDOW_WIDTH, WINDOW_HEIGHT))

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Maze Game")

    # Separate collision map: white path becomes transparent, black walls stay solid
    collision_map = pygame.transform.scale(original_map, (WINDOW_WIDTH, WINDOW_HEIGHT))
    collision_map.set_colorkey((255, 255, 255))
    map_mask = pygame.mask.from_surface(collision_map)

    map_rect = map_image.get_rect(topleft=(0, 0))

    def scale_point(point):
        x, y = point
        return (
            int(x * WINDOW_WIDTH / original_width),
            int(y * WINDOW_HEIGHT / original_height)
        )

    # Load images for the game.
    player_image = pygame.image.load(asset_path("sprites", "player.png")).convert_alpha()
    soldier1_image = pygame.image.load(asset_path("enemies", "soldier1.png")).convert_alpha()
    soldier2_image = pygame.image.load(asset_path("enemies", "soldier2.png")).convert_alpha()
    soldier3_image = pygame.image.load(asset_path("enemies", "soldier3.png")).convert_alpha()
    soldier4_image = pygame.image.load(asset_path("enemies", "bo3_soldier.png")).convert_alpha()
    soldier5_image = pygame.image.load(asset_path("enemies", "bo3_soldier2.png")).convert_alpha()
    winner_flag = pygame.image.load(asset_path("sprites", "winner_flag.png")).convert_alpha()

    player = pygame.transform.smoothscale(player_image, (28, 28))
    player_rect = player.get_rect()

    # Safe Level 2 spawn point inside the white path.
    LEVEL_2_START_ON_MAP = (437, 290)
    player_rect.center = scale_point(LEVEL_2_START_ON_MAP)
    pygame.mouse.set_pos(player_rect.center)

    player_mask = pygame.mask.from_surface(player)


    soldier1 = pygame.transform.smoothscale(soldier1_image, (75, 75))
    soldier1_rect = soldier1.get_rect(center=scale_point((200, 400)))
    soldier1_mask = pygame.mask.from_surface(soldier1)

    soldier2 = pygame.transform.smoothscale(soldier2_image, (75,75))
    soldier2_rect = soldier2.get_rect(center=scale_point((570, 535)))
    soldier2_mask = pygame.mask.from_surface((soldier2))

    soldier3 = pygame.transform.smoothscale(soldier3_image, (75, 75))
    soldier3_rect = soldier3.get_rect(center=scale_point((750, 150)))
    soldier3_mask = pygame.mask.from_surface((soldier3))

    soldier4 = pygame.transform.smoothscale(soldier4_image, (75, 75))
    soldier4_rect = soldier4.get_rect(center=scale_point((950, 270)))
    soldier4_mask = pygame.mask.from_surface((soldier4))

    soldier5 = pygame.transform.smoothscale(soldier5_image, ( 75, 75))
    soldier5_rect = soldier5.get_rect(center=scale_point((900, 490)))
    soldier5_mask = pygame.mask.from_surface((soldier5))

    winner_flag = pygame.transform.smoothscale(winner_flag, (70, 70))
    flag_rect = winner_flag.get_rect(center=scale_point((1100, 600)))
    flag_mask = pygame.mask.from_surface(winner_flag)

    clock = pygame.time.Clock()
    message_font = pygame.font.SysFont('monospace', 26)
    key_found = False
    # is_alive = True
    running = True
    mouse_control_started = False

    pygame.event.clear()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEMOTION:
                mouse_control_started = True

                # Keep player at safe spawn until the user actually moves the mouse.
        if mouse_control_started:
           position = pygame.mouse.get_pos()
           player_rect.center = position

        # Collision detection
        if pixel_collision(player_mask, player_rect, map_mask, map_rect):
            print("Colliding with walls!")
            label = message_font.render("You Lost level 2", True, (255, 255, 0))
            screen.blit(label, (20, 20))
            return False

        # This is collision detection for the pumpkin.
        elif not key_found and pixel_collision(player_mask, player_rect, soldier1_mask, soldier1_rect):
            print('Colliding with soldier1')

            label = message_font.render("You Lost level 2", True, (255, 255, 0))
            screen.blit(label, (20, 20))
            return False

        # this is collision detection fot the bat.
        elif not key_found and pixel_collision(player_mask, player_rect, soldier2_mask, soldier2_rect):
            print("Colliding with soldier2")
            label = message_font.render("Game Over", True, (255, 255, 0))
            screen.blit(label, (20, 20))
            return False

        # This is collision detection for the mummy.
        elif not key_found and pixel_collision(player_mask, player_rect, soldier3_mask, soldier3_rect):
            print("Colliding with soldier3")
            label = message_font.render("Game Over", True, (255, 255, 0))
            screen.blit(label, (20, 20))
            return False

        # This is collision detection for the skeleton.
        elif not key_found and pixel_collision(player_mask, player_rect, soldier4_mask, soldier4_rect):
            print("Colliding with soldier4.")

            label = message_font.render("Game over", True, (255, 255,0))
            screen.blit(label, (20, 20))
            return False

        # This is collision detection for the witch.
        elif not key_found and pixel_collision(player_mask, player_rect, soldier5_mask, soldier5_rect):
            print("Colliding with soldier5.")

            label = message_font.render("Game over", True, (255, 255,0))
            screen.blit(label, (20, 20))
            return False
        elif not key_found and pixel_collision(player_mask, player_rect, flag_mask, flag_rect):

            label = message_font.render("You Won Level 2!", True, (255, 255, 0))
            screen.blit(label, (20, 20))
            return True
            # Draw objects on the screen
        screen.blit(map_image, map_rect)
        screen.blit(soldier1, soldier1_rect)
        screen.blit(soldier2, soldier2_rect)
        screen.blit(soldier3, soldier3_rect)
        screen.blit(soldier4, soldier4_rect)
        screen.blit(soldier5, soldier5_rect)
        screen.blit(player, player_rect)
        screen.blit(winner_flag, flag_rect)

        pygame.display.update()
        clock.tick(25)

    pygame.quit()
    sys.exit()


