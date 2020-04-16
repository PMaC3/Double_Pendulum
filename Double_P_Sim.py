import pygame as py

def dist(point_1,point_2,lenght):
	x = point_1[0] - point_2[0]
	y = point_1[1] - point_2[1]
	if lenght > (x ** 2 + y ** 2) ** (1/2):
		return True
	return False

py.init()
SCREEN_WIDTH = int(1000)
SCREEN_HIEGHT = int(700)
OFFSET = int(25)
FONT = py.font.SysFont("momospace",35)
BUTTON_WIDTH = int(100)
BUTTON_HIEGHT = int(50)
SLIDER_LENGHT = int(200)
SLIDER_HIEGHT = int(5)
CIRCLE_SIZE = int(10)

screen = py.display.set_mode([SCREEN_WIDTH, SCREEN_HIEGHT])


button_colour = (0,100,200)
circle_colour = (0,150,150)

quit = False

L1 = 1
L2 = 1
M1 = 1
M2 = 1
THETA1 = 45
THEATA2 = 90
slider_x1 = int(2 * OFFSET + BUTTON_WIDTH)
slider_x2 = int(4 * OFFSET + BUTTON_WIDTH + SLIDER_LENGHT)
slider_x3 = int(6 * OFFSET + BUTTON_WIDTH + 2 * SLIDER_LENGHT)
slider_y1 = int(SCREEN_HIEGHT - OFFSET + CIRCLE_SIZE / 2 - BUTTON_HIEGHT)
slider_y2 = int(SCREEN_HIEGHT - OFFSET - CIRCLE_SIZE / 2)
circle_x1 = slider_x1 + int(SLIDER_LENGHT/2)
circle_x2 = slider_x2 + int(SLIDER_LENGHT/2)
circle_x3 = slider_x3 + int(SLIDER_LENGHT/2)
circle_x4 = slider_x1 + int(SLIDER_LENGHT/2)
circle_x5 = slider_x2 + int(SLIDER_LENGHT/2)
circle_x6 = slider_x3 + int(SLIDER_LENGHT/2)
circle_y1 = int(SCREEN_HIEGHT - OFFSET + CIRCLE_SIZE - BUTTON_HIEGHT - 2)
circle_y2 = int(SCREEN_HIEGHT - OFFSET - 2)
sim_x = int(OFFSET)
sim_y = int(SCREEN_HIEGHT - BUTTON_HIEGHT - OFFSET)
init_x = int(7 * OFFSET + BUTTON_WIDTH + 3 * SLIDER_LENGHT)
init_y = int(SCREEN_HIEGHT - BUTTON_HIEGHT - OFFSET)

sim_button = py.draw.rect(screen,button_colour,(sim_x,sim_y,BUTTON_WIDTH,BUTTON_HIEGHT))
slide_1 = py.draw.rect(screen,button_colour,(slider_x1,slider_y1,SLIDER_LENGHT,SLIDER_HIEGHT))
slide_2 = py.draw.rect(screen,button_colour,(slider_x1,slider_y2,SLIDER_LENGHT,SLIDER_HIEGHT))
slide_3 = py.draw.rect(screen,button_colour,(slider_x2,slider_y1,SLIDER_LENGHT,SLIDER_HIEGHT))
slide_4 = py.draw.rect(screen,button_colour,(slider_x2,slider_y2,SLIDER_LENGHT,SLIDER_HIEGHT))
slide_5 = py.draw.rect(screen,button_colour,(slider_x3,slider_y1,SLIDER_LENGHT,SLIDER_HIEGHT))
slide_6 = py.draw.rect(screen,button_colour,(slider_x3,slider_y2,SLIDER_LENGHT,SLIDER_HIEGHT))
init_button = py.draw.rect(screen,button_colour,(init_x,init_y,BUTTON_WIDTH,BUTTON_HIEGHT))
circle_1 = py.draw.circle(screen,circle_colour,(circle_x1,circle_y1),CIRCLE_SIZE)
circle_2 = py.draw.circle(screen,circle_colour,(circle_x2,circle_y1),CIRCLE_SIZE)
circle_3 = py.draw.circle(screen,circle_colour,(circle_x3,circle_y1),CIRCLE_SIZE)
circle_4 = py.draw.circle(screen,circle_colour,(circle_x4,circle_y2),CIRCLE_SIZE)
circle_5 = py.draw.circle(screen,circle_colour,(circle_x5,circle_y2),CIRCLE_SIZE)
circle_6 = py.draw.circle(screen,circle_colour,(circle_x6,circle_y2),CIRCLE_SIZE)

while not quit:

	# Close Button Click?
	print(py.mouse.get_focused())
	for event in py.event.get():
		if event.type == py.QUIT:
			quit = True
			break

		if py.mouse.get_pressed()[0]:
			pressed = True
			mouse_position = py.mouse.get_pos()
			while pressed:
				if mouse_position[0] > sim_x and mouse_position[1] > sim_y and mouse_position[0] > (sim_x + BUTTON_WIDTH) and mouse_position[1] > (sim_y + BUTTON_HIEGHT):
					# start sim = True
					pass
				elif dist(mouse_position,(circle_x1,circle_y1),CIRCLE_SIZE):
					if py.mouse.get_focused() == 1:
						mouse_x = py.mouse.get_pos()[0]
					if mouse_x < slider_x1:
						circle_x1 = slider_x1
					elif mouse_x > slider_x1 + SLIDER_LENGHT:
						circle_x1 = slider_x1 + SLIDER_LENGHT
					else:
						circle_x1 = mouse_x
					if py.mouse.get_pressed()[0] == 1:
						pressed = False
				
				elif dist(mouse_position,(circle_x2,circle_y1),CIRCLE_SIZE):
					if py.mouse.get_focused() == 1:
						mouse_x = py.mouse.get_pos()[0]
					if mouse_x < slider_x2:
						circle_x2 = slider_x2
					elif mouse_x > slider_x2 + SLIDER_LENGHT:
						circle_x2 = slider_x2 + SLIDER_LENGHT
					else:
						circle_x2 = mouse_x
					if py.mouse.get_pressed()[0] == 1:
						pressed = False
				
				elif dist(mouse_position,(circle_x3,circle_y1),CIRCLE_SIZE):
					if py.mouse.get_focused() == 1:
						mouse_x = py.mouse.get_pos()[0]
					if mouse_x < slider_x3:
						circle_x3 = slider_x3
					elif mouse_x > slider_x3 + SLIDER_LENGHT:
						circle_x3 = slider_x3 + SLIDER_LENGHT
					else:
						circle_x3 = mouse_x
					if py.mouse.get_pressed()[0] == 1:
						pressed = False
				
				elif dist(mouse_position,(circle_x4,circle_y2),CIRCLE_SIZE):
					if py.mouse.get_focused() == 1:
						mouse_x = py.mouse.get_pos()[0]
					if mouse_x < slider_x1:
						circle_x4 = slider_x1
					elif mouse_x > slider_x1 + SLIDER_LENGHT:
						circle_x4 = slider_x1 + SLIDER_LENGHT
					else:
						circle_x4 = mouse_x
					if py.mouse.get_pressed()[0] == 1:
						pressed = False
				
				elif dist(mouse_position,(circle_x5,circle_y2),CIRCLE_SIZE):
					if py.mouse.get_focused() == 1:
						mouse_x = py.mouse.get_pos()[0]
					if mouse_x < slider_x2:
						circle_x5 = slider_x2
					elif mouse_x > slider_x2 + SLIDER_LENGHT:
						circle_x5 = slider_x2 + SLIDER_LENGHT
					else:
						circle_x5 = mouse_x
					if py.mouse.get_pressed()[0] == 1:
						pressed = False
				
				elif dist(mouse_position,(circle_x6,circle_y2),CIRCLE_SIZE):
					if py.mouse.get_focused() == 1:
						mouse_x = py.mouse.get_pos()[0]
					if mouse_x < slider_x3:
						circle_x6 = slider_x3
					elif mouse_x > slider_x3 + SLIDER_LENGHT:
						circle_x6 = slider_x3 + SLIDER_LENGHT
					else:
						circle_x6 = mouse_x
					if py.mouse.get_pressed()[0] == 1:
						pressed = False
				else:
					pressed = False




			

	screen.fill((255,255,255))
	sim_button = py.draw.rect(screen,button_colour,(sim_x,sim_y,BUTTON_WIDTH,BUTTON_HIEGHT))
	slide_1 = py.draw.rect(screen,button_colour,(slider_x1,slider_y1,SLIDER_LENGHT,SLIDER_HIEGHT))
	slide_2 = py.draw.rect(screen,button_colour,(slider_x1,slider_y2,SLIDER_LENGHT,SLIDER_HIEGHT))
	slide_3 = py.draw.rect(screen,button_colour,(slider_x2,slider_y1,SLIDER_LENGHT,SLIDER_HIEGHT))
	slide_4 = py.draw.rect(screen,button_colour,(slider_x2,slider_y2,SLIDER_LENGHT,SLIDER_HIEGHT))
	slide_5 = py.draw.rect(screen,button_colour,(slider_x3,slider_y1,SLIDER_LENGHT,SLIDER_HIEGHT))
	slide_6 = py.draw.rect(screen,button_colour,(slider_x3,slider_y2,SLIDER_LENGHT,SLIDER_HIEGHT))
	init_button = py.draw.rect(screen,button_colour,(init_x,init_y,BUTTON_WIDTH,BUTTON_HIEGHT))
	circle_1 = py.draw.circle(screen,circle_colour,(circle_x1,circle_y1),CIRCLE_SIZE)
	circle_2 = py.draw.circle(screen,circle_colour,(circle_x2,circle_y1),CIRCLE_SIZE)
	circle_3 = py.draw.circle(screen,circle_colour,(circle_x3,circle_y1),CIRCLE_SIZE)
	circle_4 = py.draw.circle(screen,circle_colour,(circle_x4,circle_y2),CIRCLE_SIZE)
	circle_5 = py.draw.circle(screen,circle_colour,(circle_x5,circle_y2),CIRCLE_SIZE)
	circle_6 = py.draw.circle(screen,circle_colour,(circle_x6,circle_y2),CIRCLE_SIZE)

	py.display.flip()
