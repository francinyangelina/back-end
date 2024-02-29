import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Evite a queda!")

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Variáveis da bolinha
ball_radius = 20
ball_x = width // 2
ball_y = 50
ball_speed = 5
# Loop principal do jogo
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
       pygame.quit()
       sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ball_x > 0:
       ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x < width - ball_radius * 2:
       ball_x += ball_speed

    ball_y += ball_speed

    # Verifica se a bolinha atingiu o chão    
    if ball_y > height - ball_radius:
       ball_y = 50

    # Limpa a tela    
    screen.fill(white)

    # Desenha a bolinha
    pygame.draw.circle(screen, red, (ball_x, int(ball_y)), ball_radius)

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de atualização    
    pygame.time.Clock().tick(30)