import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *
from shot import *
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
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    AsteroidField.containers=(updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player=Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    field=AsteroidField()
    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for object in updatable:
            object.update(dt)
        screen.fill(BLACK)
        for shot in shots_group:
            shot.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        if keys[pygame.K_SPACE]:
            if(player.timer <= 0):  
                new_shot = player.shoot()
                shots_group.add(new_shot)
                player.timer = PLAYER_SHOOT_COOLDOWN
        for ast in asteroids:
            for s_shoot in shots_group:
                if ast.is_colided(s_shoot):
                    ast.kill()
                    s_shoot.kill()
        
        for ast in asteroids:
            if ast.is_colided(player):
                print("Game over!")
                exit()
        for shot in shots_group:
            shot.draw(screen)
        pygame.display.flip()
        dt=clock.tick(60)/1000




























if __name__ == "__main__":
    main()