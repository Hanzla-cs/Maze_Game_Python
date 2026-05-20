import sys
import pygame
from collision import pixel_collision
from menu import start_and_stop_display
from config import asset_path, WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR
def level1():
    """
    The player navigates through a simple maze to escape, avoiding walls and the door.
    """
    if not start_and_stop_display():
        return False

    pygame.init()

    # Load original map image
    original_map = pygame.image.load(asset_path("maps", "level_1_map.png")).convert_alpha()
    original_width, original_height = original_map.get_size()

    # Scale map to fill the full game window
    map_image = pygame.transform.smoothscale(original_map, (WINDOW_WIDTH, WINDOW_HEIGHT))

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Maze Game")

    # Collision version of the scaled map
    collision_map = map_image.copy()
    collision_map.set_colorkey((255, 255, 255))
    map_mask = pygame.mask.from_surface(collision_map)

    map_rect = map_image.get_rect(topleft=(0, 0))

    def scale_point(point):
        x, y = point
        return (
            int(x * WINDOW_WIDTH / original_width),
            int(y * WINDOW_HEIGHT / original_height)
        )

    player_image = pygame.image.load(asset_path("sprites", "player.png")).convert_alpha()
    door_image = pygame.image.load(asset_path("sprites", "door.png")).convert_alpha()
    winner_flag = pygame.image.load(asset_path("sprites", "winner_flag.png")).convert_alpha()

    player = pygame.transform.smoothscale(player_image, (60, 60))
    player_rect = player.get_rect()

    # Safe spawn point inside the Level 1 map path.
    LEVEL_1_START_ON_MAP = (60, 170)
    player_rect.center = scale_point(LEVEL_1_START_ON_MAP)
    pygame.mouse.set_pos(player_rect.center)

    player_mask = pygame.mask.from_surface(player)

    door = pygame.transform.smoothscale(door_image, (125, 125))
    door_rect = door.get_rect(center=scale_point((408, 158)))
    door_mask = pygame.mask.from_surface(door)

    winner_flag = pygame.transform.smoothscale(winner_flag, (135, 100))
    flag_rect = winner_flag.get_rect(center=scale_point((560, 170)))
    flag_mask = pygame.mask.from_surface(winner_flag)
    clock = pygame.time.Clock()
    message_font= pygame.font.SysFont('monospace',26)
    key_found = False
    is_alive = True
    running = True

    pygame.event.clear()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Position the player at the mouse location
        position = pygame.mouse.get_pos()
        player_rect.center = position

        # Collision detection
        if pixel_collision(player_mask, player_rect, map_mask, map_rect):
            print("Colliding with walls!")

            label = message_font.render("You Lost level 1", True, (255, 255, 0))
            screen.blit(label, (20, 20))
            return False
        elif not key_found and pixel_collision(player_mask, player_rect, door_mask, door_rect):
            print('Colliding with door!')

            label = message_font.render("You Lost level 1", True, (255, 255, 0))
            screen.blit(label, (20, 20))
            return False
        elif not key_found and pixel_collision(player_mask,player_rect,flag_mask,flag_rect):

            label = message_font.render("You Won Level 1!", True, (255, 255, 0))
            screen.blit(label, (20, 20))
            return True
        # Draw objects on the screen
        screen.blit(map_image, map_rect)
        screen.blit(door, door_rect)
        screen.blit(player, player_rect)
        screen.blit(winner_flag,flag_rect)

        pygame.display.update()
        clock.tick(25)


    pygame.quit()
    sys.exit()


