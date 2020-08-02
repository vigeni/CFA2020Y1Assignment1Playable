import turtle
t = turtle.Turtle()
t.speed(20)


squares = {
  'a1' : {'x': 0, 'y': 0, 'player': None},
  'a2' : {'x': 0, 'y': -50, 'player': None},
  'a3' : {'x': 0, 'y': -100, 'player': None},
  'b1' : {'x': 50, 'y': 0, 'player': None},
  'b2' : {'x': 50, 'y': -50, 'player': None},
  'b3' : {'x': 50, 'y': -100, 'player': None},
  'c1' : {'x': 100, 'y': 0, 'player': None},
  'c2' : {'x': 100, 'y': -50, 'player': None},
  'c3' : {'x': 100, 'y': -100, 'player': None},
}

for x in range(4):
  t.forward(150)
  t.right(90)


for x in [50, 100]:
 t.penup()
 t.goto(x, -150)
 t.seth(90)
 t.pendown()
 t.fd(150)
 t.penup()
 
 t.goto(0, x - 150)
 t.seth(0)
 t.pendown()
 t.fd(150)
 t.penup()
 
#Letters
t.color('black')
style=('Arial', 20)
t.goto(25, 5)
t.write('A', font=style, align='center')

t.goto(75, 5)
t.write('B', font=style, align='center')

t.goto(125, 5)
t.write('C', font=style, align='center')


#Numbers
t.goto(-15, -40)
t.write('1', font=style, align='center')

t.goto(-15, -90)
t.write('2', font=style, align='center')

t.goto(-15, -140)
t.write('3', font=style, align='center')

t.penup
t.ht()

print('Welcome to Tic Tac Toe! Type q to quit the game!')

def makestar(square):
  t.penup()
  t.goto(squares[square]['x'] + 5, squares[square]['y'] -20)
  t.seth(0)
  t.pendown()
  for i in range(5):
   t.forward(40)
   t.right(144)
  t.penup()
  t.ht()


def makediamond(square):
  t.penup()
  t.goto(squares[square]['x'] + 25, squares[square]['y'] -45)
  t.pendown()
  t.seth(-45)
  for i in range(4):
   t.left(90)
   t.forward(30)
   t.ht()


def prompt(currentPlayer): 
  print("It is " + currentPlayer + " turn!")

  a=input("Choose your square:")
  if a == 'q':
    print('Game ended! Thanks for playing!')
    return

  if squares[a]['player'] != None:
    print('Square is not empty!')
    prompt(currentPlayer)

  if currentPlayer == 'star':
    makestar(a)
    squares[a]['player'] = currentPlayer
    currentPlayer = 'diamond'

  elif currentPlayer == 'diamond':
    makediamond(a)
    squares[a]['player'] = currentPlayer
    currentPlayer = 'star'

  prompt(currentPlayer)

prompt('star')
