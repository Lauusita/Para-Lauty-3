from turtle import*

title('hola lauty')

width(0)
pencolor('white')
left(180)
forward(500) # El cursor se dirige a la izquierda 500 pixeles
pencolor('black')
width(4)# Cambia el color del cursor 
right(90) # 
forward(100)
backward(100) #el cursor se devuelve
right(90)
forward(50) 
width(0)
pencolor('white') # se cambia el color del cursor para pasar a la siguiente letra
forward(70)
width(4)
pencolor('black')
circle(50)
width(0)
pencolor('white') # se cambia el color del cursor para pasar a la siguiente letra (B)
right(0) 
forward(70)
width(4)
pencolor('black')
right(270) # 
forward(150)
backward(100)
right(180)
circle(50)
width(0)
pencolor('white') #cambio la letra (O)
right(270)
forward(130)
width(4)
pencolor('black')
right(90)
circle(50)
# fin frase
# inicio corazón 
width(0)
pencolor('white') #cambio
left (90)
forward(250) #alejarse de las letras para hacer el corazón u.u
right(90)
forward(50) # LAURA NO TOQUES MÁS HASTA AQUÍ XFAVOR
fillcolor('pink') # Dándole color u.u
begin_fill() 
pencolor('black')
left(130)
forward(100)
circle(50, 180) # primer semicírculo 
right(90)
circle(50, 180)
forward(100)
end_fill()
# fin del corazón 

right(90)
forward(1)
pencolor('white')#primera letra "u"
right(0)
forward (170)
pencolor('red')
forward(50)
circle(20,180)
forward(50) 
pencolor('white') # la w
right(90)
forward(24)
pencolor('red')
forward(50)
circle(20,180)
forward(50)
forward(50)
circle(20,180)
forward(50) 

bgpic("lobo.png")

mainloop()

