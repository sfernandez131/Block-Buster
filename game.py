import pygame as pg
import random as rnd
import time
import pyautogui

pg.init()
clk = pg.time.Clock()

effect = pg.mixer.Sound('sound96.wav')
winEffect = pg.mixer.Sound('sound100.wav')

screenW, screenH = pyautogui.size()

mainScrn = pg.display.set_mode((screenW, screenH))
sc = 0

def main(score):
	playerX = 80
	playerY = 150
	speed = 40
	
	hasTouched = False
	rect2 = pg.Rect(rnd.randint(40, screenW - 100), rnd.randint(40, screenH - 100), 100, 100)
	
	running = True
	while (running):
		clk.tick(60)
		
		mainScrn.fill(0)
		
		scoreDisp(score)
		
		rect1 = pg.Rect(playerX, playerY, 100, 100)
		
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False
	
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					running = False
				if event.key == pg.K_w:
					effect.play()
					playerY -= speed
				if event.key == pg.K_s:
					effect.play()
					playerY += speed
				if event.key == pg.K_a:
					effect.play()
					playerX -= speed
				if event.key == pg.K_d:
					effect.play()
					playerX += speed

		pg.draw.rect(mainScrn, (255, 0, 0), rect1)
		pg.draw.rect(mainScrn, (0, 255, 0), rect2)
		pg.draw.rect(mainScrn, (0, 0, 255), mainScrn.get_rect(), 3)
		
		if rect1.colliderect(rect2):
			hasTouched = True
		
		if hasTouched:
			winEffect.play()
			score += 1
			mainScrn.fill(0)
			gameOverFont = pg.font.Font('freesansbold.ttf', 72)
			gameOverSurf = gameOverFont.render('WIN', True, (255, 255, 200))
			gameOverRect = gameOverSurf.get_rect()
			gameOverRect.midtop = mainScrn.get_rect().center
			mainScrn.blit(gameOverSurf, gameOverRect)
			pg.display.flip()
			time.sleep(2)
			main(score)
	
		pg.display.flip()
	pg.quit()


def scoreDisp(score):
	scoreFont = pg.font.Font('freesansbold.ttf', 72)
	gameOverSurf = scoreFont.render("SCORE: " + str(score), True, (255, 255, 255))
	gameOverRect = gameOverSurf.get_rect()
	gameOverRect.topleft = (40, 30)
	mainScrn.blit(gameOverSurf, gameOverRect)
		
main(sc)