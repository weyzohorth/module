class Roue:
	metal = load_texture("textures/metal.jpg")
	def __init__(__, coords, diam_int=90, diam_ext=100, largeur=50, angles=(0, 0, 0), echelle=(1, 1, 1), siege=10, vitesse_angulaire=5):
		__.rotation = 0
		__.v = vitesse_angulaire
		__.x, __.y, __.z = coords
		__.aX, __.aY, __.aZ = angles
		__.eX, __.eY, __.eZ = echelle
		__.d_int, __.d_ext = diam_int, diam_ext
		__.largeur = largeur
		__.siege = siege

	def draw(__):
		glPushMatrix()
		glEnable(GL_TEXTURE_2D)

		glTranslated(__.x, __.y, __.z)
		glRotated(__.aX, 1, 0, 0)
		glRotated(__.aY, 0, 1, 0)
		glRotated(__.aZ, 0, 0, 1)

		glScalef(__.eX, __.eY, __.eZ)
		glRotated(__.rotation, 0, 0, 1)

		angle = 360./__.siege
		for i in range(__.siege):
			glPushMatrix()

			glRotatef(angle * i, 0, 0, 1)

			glTranslatef(__.d_int*0.8, 0, __.largeur/2.)
			glRotatef(-angle * i, 0, 0, 1)
			glRotated(-__.rotation, 0, 0, 1)
			glRotated(-90, 1, 0, 0)
			temp = __.largeur/10.
			glScalef(temp, temp, temp)
			glCallList(__.Siege.liste)

			glPopMatrix()

		quadric = gluNewQuadric()
		gluQuadricDrawStyle(quadric, GLU_FILL)
		gluQuadricTexture(quadric, GL_TRUE)

		glBindTexture(GL_TEXTURE_2D, __.metal)
		gluCylinder(quadric, __.d_int, __.d_int, __.largeur, 20, 1)

		glBindTexture(GL_TEXTURE_2D, __.metal)
		gluCylinder(quadric, __.d_ext, __.d_ext, __.largeur, 20, 1)

		glBindTexture(GL_TEXTURE_2D, __.metal)
		gluDisk(quadric, __.d_int, __.d_ext, 20, 1)

		glTranslated(0, 0, __.largeur)
		glBindTexture(GL_TEXTURE_2D, __.metal)
		gluDisk(quadric, __.d_int, __.d_ext, 20, 1)

		glPopMatrix()
		glDisable(GL_TEXTURE_2D)
		gluDeleteQuadric(quadric)

		__.rotation += __.v

	class Siege:
		liste = glGenLists(1001)
		glNewList(liste, GL_COMPILE)
		draw_rect((5, 5, 0), (-5, 5, 0), (-5, -5, 0), (5, -5, 0))
		draw_rect((5, 5, 0), (5, 2, 0), (5, 2, 2), (5, 5, 2))
		draw_rect((5, -5, 0), (5, -2, 0), (5, -2, 2), (5, -5, 2))
		draw_rect((-5, 5, 0), (-5, 2, 0), (-5, 2, 2), (-5, 5, 2))
		draw_rect((-5, -5, 0), (-5, -2, 0), (-5, -2, 2), (-5, -5, 2))

		draw_rect((5, 5, 0), (2, 5, 0), (2, 5, 2), (5, 5, 2))
		draw_rect((-5, 5, 0), (-2, 5, 0), (-2, 5, 2), (-5, 5, 2))
		draw_rect((5, -5, 0), (2, -5, 0), (2, -5, 2), (5, -5, 2))
		draw_rect((-5, -5, 0), (-2, -5, 0), (-2, -5, 2), (-5, -5, 2))
		glEndList()
