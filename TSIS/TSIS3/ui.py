import pygame


def draw_button(screen,text,x,y,w,h):

    font = pygame.font.SysFont("Arial",28)

    rect = pygame.Rect(x,y,w,h)

    pygame.draw.rect(
        screen,
        (180,180,180),
        rect,
        border_radius=8
    )

    label = font.render(text,True,(0,0,0))

    screen.blit(
        label,
        (x+15,y+8)
    )

    return rect


def draw_center_text(screen,text,y,size):

    font = pygame.font.SysFont("Arial",size)

    img = font.render(
        text,
        True,
        (0,0,0)
    )

    rect = img.get_rect(
        center=(200,y)
    )

    screen.blit(img,rect)