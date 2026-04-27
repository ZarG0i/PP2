import pygame
import random

from persistence import save_score

class RacerGame:

    def __init__(self,screen,settings):

        self.screen=screen
        self.settings=settings

        self.width=400
        self.height=600

        self.font=pygame.font.SysFont("Arial",20)

        self.load_assets()

        self.reset()


    def load_assets(self):

        self.player_img=pygame.image.load(
            "C:/Users/ZANGAR/Desktop/PP2/TSIS/TSIS3/assets/Designer.png"
        ).convert_alpha()

        self.player_img=pygame.transform.scale(
            self.player_img,(50,80)
        )

        self.enemy_img=pygame.image.load(
            "C:/Users/ZANGAR/Desktop/PP2/TSIS/TSIS3/assets/enemy.png"
        ).convert_alpha()

        self.enemy_img=pygame.transform.scale(
            self.enemy_img,(50,80)
        )

        self.enemy_img=pygame.transform.rotate(
            self.enemy_img,180
        )

        self.road=pygame.image.load(
            "C:/Users/ZANGAR/Desktop/PP2/TSIS/TSIS3/assets/roadPP.png"
        ).convert()

        self.road=pygame.transform.scale(
            self.road,(400,600)
        )


    def reset(self):

        self.player=self.player_img.get_rect()
        self.player.x=180
        self.player.y=500

        self.enemy=self.enemy_img.get_rect()
        self.enemy.x=random.randint(40,350)
        self.enemy.y=-100

        self.speed=5
        self.score=0
        self.distance=0
        self.game_over=False

        self.coins=[]

        for _ in range(5):
            self.spawn_coin()

        self.road_y1=0
        self.road_y2=-600


    def spawn_coin(self):

        value=random.randint(1,3)
        radius=[8,12,16][value-1]

        self.coins.append({
            "rect":pygame.Rect(
                random.randint(40,350),
                random.randint(-600,0),
                radius*2,
                radius*2
            ),
            "value":value,
            "radius":radius
        })


    def handle_event(self,event):
        pass


    def update_draw(self):

        if self.game_over:
            return "gameover"

        keys=pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.x-=5

        if keys[pygame.K_RIGHT]:
            self.player.x+=5


        self.road_y1+=self.speed
        self.road_y2+=self.speed

        if self.road_y1>=600:
            self.road_y1=-600

        if self.road_y2>=600:
            self.road_y2=-600


        self.enemy.y+=self.speed

        if self.enemy.y>600:
            self.enemy.y=-100
            self.enemy.x=random.randint(40,350)


        if self.player.colliderect(self.enemy):
            save_score("Player",self.score,self.distance)
            self.game_over=True


        for c in self.coins:

            c["rect"].y+=self.speed

            if c["rect"].y>600:
                c["rect"].y=random.randint(-600,0)

            if self.player.colliderect(c["rect"]):
                self.score+=c["value"]
                c["rect"].y=random.randint(-600,0)


        self.distance+=0.2*self.speed

        self.draw()

        return None


    def draw(self):

        self.screen.blit(self.road,(0,self.road_y1))
        self.screen.blit(self.road,(0,self.road_y2))

        self.screen.blit(self.player_img,self.player)
        self.screen.blit(self.enemy_img,self.enemy)

        for c in self.coins:

            color=[
                (255,255,0),
                (255,165,0),
                (255,0,255)
            ][c["value"]-1]

            pygame.draw.circle(
                self.screen,
                color,
                c["rect"].center,
                c["radius"]
            )

        t1=self.font.render(
            f"Coins:{self.score}",
            True,(0,0,0)
        )

        t2=self.font.render(
            f"Distance:{int(self.distance)}",
            True,(0,0,0)
        )

        self.screen.blit(t1,(10,10))
        self.screen.blit(t2,(10,35))