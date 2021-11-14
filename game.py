import pygame as pg
import random as rnd
import time
import pyautogui

pg.init()
clk = pg.time.Clock()

effect = pg.mixer.Sound('sound96.wav')
winEffect = pg.mixer.Sound('sound100.wav')

screenW, screenH = pyautogui.size()

mainScrn = pg.display.set_mode((screenW, screenH - 140))
sc = 0

def main(score):
	playerX = 80
	playerY = 150
	speed = 40
	tm = 10

	hasTouched = False
	rect2 = pg.Rect(rnd.randint(40, screenW - 100), rnd.randint(40, screenH - 100), 100, 100)

	moveAgain = 0
	tick = 0

	playerMove = [False, False, False, False]
	running = True
	while (running):
		moveAgain += 1
		tick += 1
		clk.tick(60)
		mainScrn.fill(0)

		timerDisp(tm)
		if tick >= 60:
			tm -= 1
			if tm <= 0:
				tick = 0
				tm = 10
				main(score)

		scoreDisp(score)

		rect1 = pg.Rect(playerX, playerY, 100, 100)

		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					running = False
				if event.key == pg.K_w:
					playerMove[0] = True
				if event.key == pg.K_s:
					playerMove[1] = True
				if event.key == pg.K_a:
					playerMove[2] = True
				if event.key == pg.K_d:
					playerMove[3] = True
     
			if event.type == pg.KEYUP:
				if event.key == pg.K_w:
					playerMove[0] = False
				if event.key == pg.K_s:
					playerMove[1] = False
				if event.key == pg.K_a:
					playerMove[2] = False
				if event.key == pg.K_d:
					playerMove[3] = False


			if playerMove[0]:
				#effect.play()
				playerY -= speed
			if playerMove[1]:
				#effect.play()
				playerY += speed
			if playerMove[2]:
				#effect.play()
				playerX -= speed
			if playerMove[3]:
				#effect.play()
				playerX += speed

		# Move block 2 every 3 cycles.
		if moveAgain >= 180:
			moveAgain = 0
			rect2 = pg.Rect(rnd.randint(40, screenW - 100), rnd.randint(40, screenH - 200), 100, 100)

		pg.draw.rect(mainScrn, (255, 0, 0), rect1)
		pg.draw.rect(mainScrn, (0, 255, 0), rect2)
		pg.draw.rect(mainScrn, (0, 0, 255), mainScrn.get_rect(), 30)

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
	scoreSurf = scoreFont.render("SCORE: " + str(score), True, (255, 255, 255))
	scoreRect = scoreSurf.get_rect()
	scoreRect.topleft = (40, 30)
	mainScrn.blit(scoreSurf, scoreRect)
 
def timerDisp(tmr):
	timerFont = pg.font.Font('freesansbold.ttf', 72)
	timerSurf = timerFont.render("TIMER: " + str(tmr), True, (255, 255, 255))
	timerRect = timerSurf.get_rect()
	timerRect.topright = (screenW - 150, 30)
	mainScrn.blit(timerSurf, timerRect)

main(sc)