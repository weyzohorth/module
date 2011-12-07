from mod_gl import *

class Camera:
	events = (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION)
	hand = (pygame.cursors.compile((
		"       XX       ",
		"   XX X..XXX    ",
		"  X..XX..X..X   ",
		"  X..XX..X..X X ",
		"   X..X..X..XX.X",
		"   X..X..X..X..X",
		" XX X.......X..X",
		"X..XX..........X",
		"X...X.........X ",
		" X............X ",
		"  X...........X ",
		"  X..........X  ",
		"   X.........X  ",
		"    X.......X   ",
		"     X......X   ",
		"     X......X   ")),
	pygame.cursors.compile((
		"                ",
		"                ",
		"                ",
		"                ",
		"    XX XX XX    ",
		"   X..X..X..XX  ",
		"   X........X.X ",
		"    X.........X ",
		"   XX.........X ",
		"  X...........X ",
		"  X...........X ",
		"  X..........X  ",
		"   X.........X  ",
		"    X.......X   ",
		"     X......X   ",
		"     X......X   ")))
	appuie = False
	aY = 0
	aZ = 0
	distance = 2
	motion_sensivity = 0.3
	scroll_sensivity = 2

	def __init__(__, x=0, y=0, z=10, obj=None):
		pygame.mouse.set_cursor((16, 16), (0, 0), __.hand[0][0], __.hand[0][1])
		__.x, __.y, __.z = x, y, z
		__.obj = obj

	def draw(__):
		if not __.obj: gluLookAt(__.x + __.distance, __.y, __.z, 0, 0, 0, 0, 0, 1)
		else: gluLookAt(__.x + __.distance, __.y, __.z, __.obj.x, __.obj.y, __.obj.z, 0, 0, 1)
		glRotated(__.aY, 0, 1, 0)
		glRotated(__.aZ, 0, 0, 1)

	def event(__, event):
		if event.type == pygame.MOUSEMOTION and __.appuie:
			__.aY += event.rel[1] * __.motion_sensivity
			__.aZ += event.rel[0] * __.motion_sensivity
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				__.appuie = True
				pygame.mouse.set_cursor((16, 16), (0, 0), __.hand[__.appuie][0], __.hand[__.appuie][1])
			elif event.button == 5: __.distance += __.scroll_sensivity
			elif event.button == 4: __.distance -= __.scroll_sensivity
		elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			__.appuie = False
			pygame.mouse.set_cursor((16, 16), (0, 0), __.hand[__.appuie][0], __.hand[__.appuie][1])


class Camera_FreeFly:
	events = (pygame.KEYDOWN, pygame.KEYUP,
			pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP,
			pygame.MOUSEMOTION)
	motion_sensivity = 0.02
	k_q = k_z = k_s = k_d = False

	def __init__(__, coords, target=(0, 0, 0), speed=5, aH=0, aV=0):
		__.x, __.y, __.z = coords
		__.tx, __.ty, __.tz = target
		__.speed = speed
		__.aH, __.aV = aH, aV
		pygame.mouse.set_visible(False)

	def draw(__):
		if __.k_q: __.set_xy(__.aH - 90)
		elif __.k_d: __.set_xy(__.aH + 90)
		if __.k_z: __.set_xy(__.aH)
		elif __.k_s: __.set_xy(__.aH + 180)
		gluLookAt(__.x, __.y, __.z, __.x+cos(__.aH*pi/180), __.y-sin(__.aH*pi/180), __.z-sin(__.aV*pi/180), 0, 0, 1)
		if pygame.mouse.get_focused(): pygame.mouse.set_pos(pygame.display.Info().current_w/2, pygame.display.Info().current_h/2)

	def set_xy(__, angle):
		__.x +=cos(angle * pi / 180) * __.speed
		__.y -= sin(angle * pi / 180) * __.speed

	def set_z(__):
		__.z -= sin(aV * pi / 180) * __.speed


	def event(__, event):
		if event.type == pygame.MOUSEMOTION and pygame.mouse.get_focused():
			__.aH += ((event.pos[0]-pygame.display.Info().current_w/2) * __.motion_sensivity) % 360
			__.aV += (event.pos[1]-pygame.display.Info().current_h/2)* __.motion_sensivity
			if __.aV > 90: __.aV = 90
			elif __.aV < -90: __.aV = -90

		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 4: __.z += 5
			elif event.button == 5: __.z -= 5
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				__.k_q = True
				__.k_d = False
			elif event.key == pygame.K_z:
				__.k_z = True
				__.k_s = False
			elif event.key == pygame.K_s:
				__.k_s = True
				__.k_z = False
			elif event.key == pygame.K_d:
				__.k_d = True
				__.k_q = False

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_q: __.k_q = False
			elif event.key == pygame.K_z: __.k_z = False
			elif event.key == pygame.K_s: __.k_s = False
			elif event.key == pygame.K_d: __.k_d = False
