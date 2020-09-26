import sys
import pygame as pg


class AlienInvasion:
    def __init__(self):
        screen_dim = (1200, 800)

        pg.init()
        self.screen = pg.display.set_mode(screen_dim)
        self.screen_rect = self.screen.get_rect()
        self.bg_color = (255, 255, 255)
        screen_center = self.screen_rect.right
        pg.display.set_caption("Alien Invasion")

    def run_game(self):

        ship = pg.image.load('images/ship.bmp')
        ship_rect = ship.get_rect()
        ship_rect.midbottom = self.screen_rect.midbottom

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        ship_rect.x += 10
                    elif event.key == pg.K_LEFT:
                        ship_rect.x -= 10
                    elif event.key == pg.K_SPACE:
                        ship.fire_bullet()
                    elif event.key == pg.K_q:
                        sys.exit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_RIGHT:
                        ship.moving_right = False

                self.screen.fill(self.bg_color)
                bullet_rect = pg.Rect(100, 100, 3, 15)
                color = (100, 100, 100)
                pg.draw.rect(self.screen, color, bullet_rect)
                self.screen.blit(ship, ship_rect)
                pg.display.flip()

    def blitme(self):
        """Draw ship at current location."""
        self.screen.blit(self.image, self.rect)
