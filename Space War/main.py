import pygame
import time
import random
pygame.font.init()

HIGHT,WIDTH = 800,1000
WIN = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Zubair")

BG =pygame.transform.scale(pygame.image.load("space.png"),(WIDTH,HIGHT))
PLAYER_WIDHT = 40
PLAYER_HIGHT = 60
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HIGHT = 20
STAR_VEL = 3
FONT = pygame.font.SysFont("Times",30)



def draw(player,elapsed_time,stars):
    WIN.blit(BG,(0,0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1 , "white")
    WIN.blit(time_text,(10,10))


    pygame.draw.rect(WIN,"red",player)


    for star in stars:
        pygame.draw.rect(WIN, "White", star)

    pygame.display.update()
def main():
    run = True

    player = pygame.Rect(900 , HIGHT - PLAYER_HIGHT,PLAYER_WIDHT,PLAYER_HIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False
    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0,WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HIGHT ,STAR_WIDTH,STAR_HIGHT)
                stars.append(star)
            star_add_increment = max(200,star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL        
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL


        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!",1,"White")
            WIN.blit(lost_text,(WIDTH/2 - lost_text.get_width()/2, HIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player,elapsed_time,stars)
    pygame.quit()
if __name__ == "__main__":
    main()