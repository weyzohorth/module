from mod_gl import *
from mod_math import DISTANCE_3D, DIRECTION_3D, radian, cos, sin
from random import randint

class Roquette:
	top = load_texture("textures/rocket_textures/rocket_top.jpg")
	middle = load_texture("textures/rocket_textures/rocket_middle.jpg")
	bottom = load_texture("textures/rocket_textures/rocket_bottom.jpg")
	motor = load_texture("textures/rocket_textures/rocket_motor.jpg")
	liste = glGenLists(1002)

	def __init__(__, coords, angles=(0, 0, 90), speed=(0, 0, 1), echelle=(1, 1, 1)):
		__.x, __.y, __.z = coords
		__.aX, __.aY, __.aZ = angles
		__.eX, __.eY, __.eZ = echelle
		__.set_speed(speed)
		__.trans = 0

	def set_speed(__, speeds):
		__.aH, __.aV = DIRECTION_3D(0, 0, 0, speeds[0], speeds[1], speeds[2])
		__.speed = DISTANCE_3D(0, 0, 0, speeds[0], speeds[1], speeds[2])

	def get_size(__, echelle):
		return echelle[0],  echelle[1], echelle[2] * 1.3#2.9

	def get_coords_motor(__):
		temp = cos(radian(__.aV))
		return (__.x - cos(radian(__.aH)) * temp * __.eX,
				__.y + sin(radian(__.aH)) * temp * __.eY,
				__.z + sin(radian(__.aV)) * 1.3 * __.eZ)

	def draw(__):
		glEnable(GL_TEXTURE_2D)
		glPushMatrix()

		glTranslated(__.x, __.y, __.z)
		glRotated(__.aX, 1, 0, 0)
		glRotated(__.aY, 0, 1, 0)
		glRotated(__.aZ, 0, 0, 1)
		rotate_HV(__.aH, __.aV)

		glScalef(__.eX, __.eY, __.eZ)

		quadric = gluNewQuadric()
		gluQuadricDrawStyle(quadric, GLU_FILL)
		gluQuadricTexture(quadric, GL_TRUE)

		glBindTexture(GL_TEXTURE_2D, __.top)
		gluCylinder(quadric, 0.5, 0, 1.6, 20, 1)

		glTranslated(0, 0, -1.05)
		glBindTexture(GL_TEXTURE_2D, __.middle)
		gluCylinder(quadric, 0.15, 0.5, 1.05, 20, 1)

		glTranslated(0, 0, -0.25)
		glBindTexture(GL_TEXTURE_2D, __.bottom)
		gluCylinder(quadric, 0.3, 0.15, 0.25, 20, 1)

		glBindTexture(GL_TEXTURE_2D, __.motor)
		gluDisk(quadric, 0, 0.3, 20, 1)

		gluDeleteQuadric(quadric)

		glPopMatrix()
		glDisable(GL_TEXTURE_2D)

		vx, vy, vz = __.get_vector_speed()
		__.x += vx
		__.y += vy
		__.z += vz

	def get_vector_speed(__):
		temp = cos(radian(__.aV)) * __.speed
		vx = cos(radian(__.aH)) * temp
		if -1.0e-5 < vx < 1.0e-5: vx = 0
		vy =	-sin(radian(__.aH)) * temp
		if -1.0e-5 < vy < 1.0e-5: vy = 0
		vz = -sin(radian(__.aV)) * __.speed
		if -1.0e-5 < vz < 1.0e-5: vz = 0
		return vx, vy, vz

class Roquette_artifice(Roquette):
	son_fusee = pygame.mixer.Sound("textures/rocket_textures/fusee.ogg")
	son_boom = pygame.mixer.Sound("textures/rocket_textures/boom.ogg")

	def __init__(__, coords, angles=(0, 0, 90), speed=(0, 0, 1), echelle=(1, 1, 1), life=50,
				couleur_moteur_min=(255, 0, 0), couleur_moteur_max=(255, 255, 0),
				couleur_artifice_min=(240, 0, 240), couleur_artifice_max=(255, 0, 255), lim_x=(), lim_y=(), lim_z=()):
		Roquette.__init__(__, coords, angles, speed, echelle)
		__.couleurs_moteur = [list(couleur_moteur_min), list(couleur_moteur_max)]
		__.couleurs_artifice = [list(couleur_artifice_min), list(couleur_artifice_max)]
		temp = (__.x, __.y, __.z)
		vx, vy, vz = __.get_vector_speed()
		__.gen = Gen_particules(200, True, coords_min=temp, coords_max=temp,
					speed_min=[-vx*10, -vy*10, -vz*10],
					speed_max=[(bool(vx<0)*2-1)*10*bool(vx), (bool(vy<0)*2-1)*10*bool(vy), (bool(vz<0)*2-1)*10*bool(vz)],
					couleur_min=__.couleurs_moteur[0], couleur_max=__.couleurs_moteur[1],
					perte_min=1, perte_max=10, taille_min=1, taille_max=7, lim_x=lim_x, lim_y=lim_y, lim_z=lim_z)
		__.lim_x = lim_x
		__.lim_y = lim_y
		__.lim_z = lim_z
		__.life=life
		__.activ = True
		__.son_fusee.play()

	def draw(__):
		if __.activ:
			if __.life > 0:
				Roquette.draw(__)
				x, y, z = __.get_vector_speed()
				__.gen.set_speed([-x*10, -y*10, -z*10], [(randint(0, 1)*2-1)*10, (randint(0, 1)*2-1)*10, (randint(0, 1)*2-1)*10])
				temp = __.get_coords_motor()
				__.gen.set_coords(temp, temp)
				__.gen.draw()
				__.life -= 1
			elif not __.life:
				__.son_boom.play()
				__.life -= 1
				temp = __.get_coords_motor()
				__.gen.set_coords(temp, temp)
				__.gen.regenere = False
				__.gen.draw()
				temp = [__.x, __.y, __.z]
				__.gen2 = Gen_particules(200, False, temp, temp,
						couleur_min=__.couleurs_artifice[0], couleur_max=__.couleurs_artifice[1],
						alpha_min=200, perte_min=1, perte_max=2,
						taille_min=10, taille_max=20, gravite_min=(0, 0, -1), gravite_max=(0, 0, -2),
						lim_x=__.lim_x, lim_y=__.lim_y, lim_z=__.lim_z)
			else:
				if __.gen.particules: __.gen.draw()
				if __.gen2.particules: __.gen2.draw()
				elif not __.gen.particules: __.activ = False

	def reinit_gen(__):
		temp = __.get_coords_motor()
		__.gen.set_coords(temp, temp)
		__.gen.reinit_particules()
		__.gen.regenere = True
