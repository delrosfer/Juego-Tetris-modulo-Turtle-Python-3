import turtle
import time
import random

ventana = turtle.Screen()
ventana.title("Creando Tetris con Turtle")
ventana.bgcolor("lightgreen")
ventana.setup(width=600, height=800)
ventana.tracer(0)

delay = 0.05

class Shape():
	def __init__(self):
		self.x = 5
		self.y = 0
		self.color = random.randint(1, 10)

		#bloque de figuras
		square = [[1, 1],
				  [1,1]]

		horizontal_line = [[1,1,1,1]]

		vertical_line = [[1],
				         [1],
				         [1],
				         [1]]

		left_l = [[1,0,0,0],
				  [1,1,1,1]]

		right_l = [[0,0,0,1],
				   [1,1,1,1]]

		left_s = [[1,1,0],
				  [0,1,1]]

		right_s = [[0,1,1],
			  	   [1,1,0]]

		t = [[0,1,0],
		     [1,1,1]]

		t_normal = [[1,1,1],
		            [0,1,0]]

		shapes = [square, horizontal_line, vertical_line, left_l, right_l, left_s, right_s, t, t_normal]

		#elegir una figura aleatoria cada vez
		self.shape = random.choice(shapes)

		self.height = len(self.shape)
		self.width = len(self.shape[0])

		#print(self.height, self.width)

	def move_left(self, grid):
		if self.x > 0:
			if grid[self.y][self.x -1] == 0:
				self.erase_shape(grid)
				self.x -= 1

	def move_right(self, grid):
		if self.x < 12 - self.width:
			if grid[self.y][self.x + self.width] == 0:
				self.erase_shape(grid)
				self.x += 1

	def draw_shape(self, grid):
		for y in range(self.height):
			for x in range(self.width):
				if(self.shape[y][x]==1):
					grid [self.y + y][self.x + x] = self.color

	def erase_shape(self, grid):
		for y in range(self.height):
			for x in range(self.width):
				if(self.shape[y][x]==1):
					grid [self.y + y][self.x + x] = 0

	def can_move(self, grid):
		result = True
		for x in range(self.width):
			#checar si el bottom is a 1
			if(self.shape[self.height-1][x] == 1 ):
				if(grid[self.y + self.height][self.x + x] != 0):
					return False

		return result

	def rotate(self, grid):
		#primero borrar la figura
		self.erase_shape(grid)
		rotated_shape = []
		for x in range(len(self.shape[0])):
			new_row = []
			for y in range(len(self.shape)-1, -1, -1):
				new_row.append(self.shape[y][x])
			rotated_shape.append(new_row)

		right_side = self.x + len(rotated_shape[0])
		if right_side < len(grid[0]):

			self.shape = rotated_shape
			#actualizar antura y anchura
			self.height = len(self.shape)
			self.width = len(self.shape[0])

grid = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print(len(grid))

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)


def draw_grid(pen, grid):
	pen.clear()
	top = 270
	left = -130

	colors = ["black", "lightblue", "blue", "orange", "yellow", "green", "purple","red", "gray", "brown", "pink"]

	for y in range(len(grid)):
		for x in range(len(grid[0])):
			screen_x = left + (x * 20)
			screen_y = top - (y * 20)
			color_number = grid[y][x]
			color = colors[color_number]
			pen.color(color)
			pen.goto(screen_x, screen_y)
			pen.stamp()


def check_grid(grid):
	#checar si cada renglon esta completo
	y = 23
	while y > 0:

		is_full = True
		for x in range(0, 12):
			if grid[y][x] == 0:
				is_full = False
				y -= 1
				break

		if is_full:
			global score
			score += 10
			draw_score(pen, score)
			for copy_y in range(y, 0, -1):
				for copy_x in range(0, 12):
					grid[copy_y][copy_x] = grid[copy_y-1][copy_x]

def draw_score(pen, score):
	pen.color("blue")
	pen.hideturtle()
	pen.goto(-75, 300)
	pen.write("Puntuación: {}".format(score), move=False, align="left", font=("Arial", 20, "normal"))
	

#crear la figura basica para iniciar el juego
shape = Shape()

#colocar la figura en el grid
grid[shape.y][shape.x] = shape.color

#dibujar el grid inicial
#draw_grid(pen, grid)

ventana.listen()
ventana.onkeypress(lambda: shape.move_left(grid), "Left")
ventana.onkeypress(lambda: shape.move_right(grid), "Right")
ventana.onkeypress(lambda: shape.rotate(grid), "space")

#colocar la puntuacion a 0
score = 0

draw_score(pen, score)

while True:
	ventana.update()

	#mover la figura

	#bottom row
	

	#abrir renglon

	#checar por el vacio

	if shape.y == 23 - shape.height + 1:
		shape = Shape()
		check_grid(grid)
		#checar por colision con el siguiente renglon
	elif shape.can_move(grid):
		#borrar la figura actual
		shape.erase_shape(grid)
		#mover la figura por 1		
		
		shape.y +=1

		#dibujar nuevamente la figura
		shape.draw_shape(grid)		
		

	else:
		shape = Shape()
		check_grid(grid)

	
#dibujar la pantalla
	
	draw_grid(pen, grid)
	draw_score(pen, score)

	time.sleep(delay)

ventana.mainloop()