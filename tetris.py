import turtle
import time
import random

ventana = turtle.Screen()
ventana.title("Creando Tetris con Turtle")
ventana.bgcolor("black")
ventana.setup(width=600, height=800)
ventana.tracer(0)

delay = 0.05

class Shape():
	def __init__(self):
		self.x = 5
		self.y = 0
		self.color = random.randint(1, 7)

	def move_left(self, grid):
		if self.x > 0:
			if grid[self.y][self.x -1] == 0:
				grid[self.y][self.x] = 0
				self.x -= 1

	def move_right(self, grid):
		if self.x < 11:
			if grid[self.y][self.x +1] == 0:
				grid[self.y][self.x] = 0
				self.x +=1

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
	[1, 2, 2, 2, 4, 5, 6, 7, 4, 3, 2, 0],
	[1, 2, 2, 2, 4, 5, 6, 7, 4, 3, 2, 0],
	[1, 2, 2, 2, 4, 5, 6, 7, 4, 3, 2, 0],
	[1, 2, 2, 2, 4, 5, 6, 7, 4, 3, 2, 0],
	[0, 1, 2, 3, 0, 0, 0, 7, 1, 2, 3, 4]
]

print(len(grid))

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)

def draw_grid(pen, grid):
	pen.clear()
	top = 230
	left = -110

	colors = ["black", "lightblue", "blue", "orange", "yellow", "green", "purple","red"]

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
	pen.hideturtle()
	pen.goto(-75, 300)
	pen.write("Puntuacion: {}".format(score), move=False, align="left", font=("Arial", 20, "normal"))
	pen.showturtle()

#crear la figura basica para iniciar el juego
shape = Shape()

#colocar la figura en el grid
grid[shape.y][shape.x] = shape.color

#dibujar el grid inicial
#draw_grid(pen, grid)

ventana.listen()
ventana.onkeypress(lambda: shape.move_left(grid), "Left")
ventana.onkeypress(lambda: shape.move_right(grid), "Right")

#colocar la puntuacion a 0
score = 0

draw_score(pen, score)

while True:
	ventana.update()

	#mover la figura

	#bottom row
	

	#abrir renglon
	if shape.y == 23:
		shape = Shape()
		check_grid(grid)
	elif grid[shape.y +1] [shape.x] == 0:
		grid[shape.y][shape.x] = 0
		
		shape.y +=1
		grid[shape.y][shape.x] = shape.color

	else:
		shape = Shape()
		check_grid(grid)

	
#dibujar la pantalla
	
	draw_score(pen, score)	
	draw_grid(pen, grid)

	time.sleep(delay)

ventana.mainloop()