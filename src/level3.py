import sys
import pygame
from collision import pixel_collision
from menu import start_and_stop_display
from config import asset_path, WINDOW_WIDTH, WINDOW_HEIGHT


def level3():
    """
    The player navigates through Level 3, avoiding guards, dragon, fence, and walls.
    """
    if not start_and_stop_display():
        return False

    pygame.init()

    original_map = pygame.image.load(asset_path("maps", "map for level 3.png")).convert_alpha()
    original_width, original_height = original_map.get_size()

    map_image = pygame.transform.smoothscale(original_map, (WINDOW_WIDTH, WINDOW_HEIGHT))

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Maze Game")

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

    player_image = pygame.image.load(asset_path("sprites", "player.png")).convert_alpha()
    guard_image = pygame.image.load(asset_path("enemies", "level_3_guards.png")).convert_alpha()
    winner_flag_image = pygame.image.load(asset_path("sprites", "winner_flag.png")).convert_alpha()
    dragon_image = pygame.image.load(asset_path("enemies", "dragon_level_3.png")).convert_alpha()
    fence_image = pygame.image.load(asset_path("enemies", "fence_level_3.png")).convert_alpha()

    # Player: top-left start lane
    player = pygame.transform.smoothscale(player_image, (30, 30))
    player_rect = player.get_rect()

    LEVEL_3_START_ON_MAP = (50, 160)
    player_rect.center = scale_point(LEVEL_3_START_ON_MAP)
    pygame.mouse.set_pos(player_rect.center)

    player_mask = pygame.mask.from_surface(player)

    # Guard 1: top-middle corridor
    guard_1 = pygame.transform.smoothscale(guard_image, (80, 80))
    guard_rect_1 = guard_1.get_rect(center=scale_point((395, 165)))
    guard_mask_1 = pygame.mask.from_surface(guard_1)

    # Guard 2: left vertical corridor
    guard_2 = pygame.transform.smoothscale(guard_image, (80, 80))
    guard_rect_2 = guard_2.get_rect(center=scale_point((95, 230)))
    guard_mask_2 = pygame.mask.from_surface(guard_2)

    # Dragon: large central obstacle, acting like a roundabout
    dragon = pygame.transform.smoothscale(dragon_image, (190, 165))
    dragon_rect = dragon.get_rect(center=scale_point((455, 345)))
    dragon_mask = pygame.mask.from_surface(dragon)

    # Fence: blocks the horizontal approach in front of the dragon
    # but does NOT stretch into the left vertical corridor.
    fence = pygame.transform.smoothscale(fence_image, (215, 70))
    fence_rect = fence.get_rect(center=scale_point((420, 385)))
    fence_mask = pygame.mask.from_surface(fence)

    # Winning flag: placed inside the bottom-right winning corridor
    winner_flag = pygame.transform.smoothscale(winner_flag_image, (125, 95))
    flag_rect = winner_flag.get_rect(center=scale_point((720, 410)))
    flag_mask = pygame.mask.from_surface(winner_flag)

    # Guard 3: upper-right loop
    guard_3 = pygame.transform.smoothscale(guard_image, (80, 80))
    guard_rect_3 = guard_3.get_rect(center=scale_point((690, 220)))
    guard_mask_3 = pygame.mask.from_surface(guard_3)

    clock = pygame.time.Clock()
    message_font = pygame.font.SysFont("monospace", 26)
    key_found = False

    running = True
    mouse_control_started = False
    pygame.event.clear()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEMOTION:
                mouse_control_started = True

        if mouse_control_started:
            position = pygame.mouse.get_pos()
            player_rect.center = position

        if pixel_collision(player_mask, player_rect, map_mask, map_rect):
            print("Colliding with walls!")
            label = message_font.render("You Lost level 3", True, (255, 255, 0))
            screen.blit(label, (20, 20))
            pygame.display.update()
            return False

        elif not key_found and pixel_collision(player_mask, player_rect, guard_mask_1, guard_rect_1):
            print("Colliding with guard 1!")
            label = message_font.render("You Lost level 3", True, (255, 255, 0))
            screen.blit(label, (20, 20))
            pygame.display.update()
            return False

        elif not key_found and pixel_collision(player_mask, player_rect, guard_mask_2, guard_rect_2):
            print("Colliding with guard 2!")
            label = message_font.render("You Lost level 3", True, (255, 255, 0))
            screen.blit(label, (20, 20))
            pygame.display.update()
            return False

        elif not key_found and pixel_collision(player_mask, player_rect, dragon_mask, dragon_rect):
            print("Eaten by the dragon")
            label = message_font.render("You Lost level 3", True, (255, 255, 0))
            screen.blit(label, (20, 20))
            pygame.display.update()
            return False

        elif not key_found and pixel_collision(player_mask, player_rect, fence_mask, fence_rect):
            print("Blocked by the fence")
            label = message_font.render("You Lost level 3", True, (255, 255, 0))
            screen.blit(label, (20, 20))
            pygame.display.update()
            return False

        elif not key_found and pixel_collision(player_mask, player_rect, guard_mask_3, guard_rect_3):
            print("Collided with guard 3")
            label = message_font.render("You Lost level 3", True, (255, 255, 0))
            screen.blit(label, (20, 20))
            pygame.display.update()
            return False

        elif not key_found and pixel_collision(player_mask, player_rect, flag_mask, flag_rect):
            print("You won Level 3!")
            label = message_font.render("You Won Level 3!", True, (255, 255, 0))
            screen.blit(label, (20, 20))
            pygame.display.update()
            return True

        screen.blit(map_image, map_rect)
        screen.blit(guard_1, guard_rect_1)
        screen.blit(guard_2, guard_rect_2)
        screen.blit(dragon, dragon_rect)
        screen.blit(fence, fence_rect)
        screen.blit(guard_3, guard_rect_3)
        screen.blit(winner_flag, flag_rect)
        screen.blit(player, player_rect)

        pygame.display.update()
        clock.tick(25)

    pygame.quit()
    sys.exit()