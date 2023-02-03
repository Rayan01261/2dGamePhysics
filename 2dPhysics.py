import pygame


#inicializar o pygame

pygame.init()

#desenhar a tela 
screen = pygame.display.set_mode((800 , 600))

#colocar o titulo da janela
pygame.display.set_caption("test")

#definir a cor do background
background_color = (255,255,255)

#definir sprite
sprite_image = pygame.image.load("sprite.png")
sprite_image2 = pygame.image.load("block.png")

#definir o jogador
sprite_rect = sprite_image.get_rect()
sprite_rect2 = sprite_image2.get_rect()


#definir gravidade e velocidade

sprite_rect.x = 100
sprite_rect.y = 100

sprite_rect2.x = 100
sprite_rect2.y = 504
velocity_x= 0
velocity_y= 0


gravidade = 2

#definir clock do jogo(que decide o framerate)
clock = pygame.time.Clock()


#loop do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    #preencher a tela com a cor do background
    screen.fill(background_color)

    #pegar o framerate em milisegundos
    dt = clock.tick(60)/100

    #definir gravidade
    velocity_y += gravidade * dt

    if (sprite_rect.x == sprite_rect2.x and sprite_rect.y == sprite_rect2.y or sprite_rect.y>=410):
        
        print("nao ta colidindo")
    else:
        sprite_rect.x += velocity_x * dt 
        sprite_rect.y += velocity_y * dt

    

    screen.blit(sprite_image,sprite_rect)
    screen.blit(sprite_image2,sprite_rect2)
    print(sprite_rect.y)
    print(sprite_rect2.y)
    #atualizar o display a cada checagem
    pygame.display.update()


pygame.quit()