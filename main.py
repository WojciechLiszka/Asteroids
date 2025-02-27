import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *
BLACK = (0, 0, 0)
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock =pygame.time.Clock()
    
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids= pygame.sprite.Group()
    AsteroidField.containers=(updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player=Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    field=AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for object in updatable:
            object.update(dt)
        screen.fill(BLACK)
        for sprite in drawable:
            sprite.draw(screen)
        for ast in asteroids:
            if ast.is_colided(player):
                print("Game over!")
                exit()
        pygame.display.flip()
        dt=clock.tick(60)/1000




























if __name__ == "__main__":
    main()