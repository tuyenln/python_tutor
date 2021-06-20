import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("My game")
running = True
GREEN = (0, 200, 0)
RED = (255,0,0)
BLACK = (0,0,0)
clock = pygame.time.Clock()


rect_x = 50
rect_y = 50

background = GREEN

font_size = 50
font = pygame.font.SysFont('sans', font_size)
text = font.render("Random", True, BLACK)

while running:
	clock.tick(60)
	screen.fill(background)

	mouse_x, mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen, RED, (rect_x, rect_y, 50, 50))

	screen.blit(text, (50,50))

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				if (rect_x < mouse_x) and (mouse_x < rect_x + 50) and  (rect_y < mouse_y) and (mouse_y < rect_y + 50):
					background = (randint(0,255), randint(0,255), randint(0,255))
				else:
					background = GREEN

		if event.type == pygame.QUIT:
			running = False




	pygame.display.flip()

pygame.quit()