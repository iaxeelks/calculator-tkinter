from tkinter import *

print("On")

# VARIABLES

pos = 0

# PANTALLA

window = Tk()
window.title("Calculadora")

# ENTRADA DE TEXTO

datos = Entry(window, font = ("Calibri 20"))
datos.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)

# CREAR LOS BOTONES

b1 = Button(window, text = "1", width = 5, height = 2, command = lambda: click_boton(1))
b2 = Button(window, text = "2", width = 5, height = 2, command = lambda: click_boton(2))
b3 = Button(window, text = "3", width = 5, height = 2, command = lambda: click_boton(3))
b4 = Button(window, text = "4", width = 5, height = 2, command = lambda: click_boton(4))
b5 = Button(window, text = "5", width = 5, height = 2, command = lambda: click_boton(5))
b6 = Button(window, text = "6", width = 5, height = 2, command = lambda: click_boton(6))
b7 = Button(window, text = "7", width = 5, height = 2, command = lambda: click_boton(7))
b8 = Button(window, text = "8", width = 5, height = 2, command = lambda: click_boton(8))
b9 = Button(window, text = "9", width = 5, height = 2, command = lambda: click_boton(9))
b0 = Button(window, text = "0", width = 15, height = 2, command = lambda: click_boton(0))

b_borrar = Button(window, text = "AC", width = 5, height = 2, command = lambda: borrar())
b_parentesisA = Button(window, text = "(", width = 5, height = 2, command = lambda: click_boton("("))
b_parentesisB = Button(window, text = ")", width = 5, height = 2, command = lambda: click_boton(")"))
b_punto = Button(window, text = ".", width = 5, height = 2, command = lambda: click_boton("."))

b_div = Button(window, text = "/", width = 5, height = 2, command = lambda: click_boton("/"))
b_mult = Button(window, text = "*", width = 5, height = 2, command = lambda: click_boton("*"))
b_suma = Button(window, text = "+", width = 5, height = 2, command = lambda: click_boton("+"))
b_resta = Button(window, text = "-", width = 5, height = 2, command = lambda: click_boton("-"))
b_igual = Button(window, text = "=", width = 5, height = 2, command = lambda: resultado())

# POSICIONAR LOS BOTONES

b_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
b_parentesisA.grid(row = 1, column = 1, padx = 5, pady = 5)
b_parentesisB.grid(row = 1, column = 2, padx = 5, pady = 5)

b_div.grid(row = 1, column = 3, padx = 5, pady = 5)
b_mult.grid(row = 2, column = 3, padx = 5, pady = 5)
b_suma.grid(row = 3, column = 3, padx = 5, pady = 5)
b_resta.grid(row = 4, column = 3, padx = 5, pady = 5)
b_punto.grid(row = 5, column = 2, padx = 5, pady = 5)
b_igual.grid(row = 5, column = 3, padx = 5, pady = 5)

b9.grid(row = 2, column = 0, padx = 5, pady = 5)
b8.grid(row = 2, column = 1, padx = 5, pady = 5)
b7.grid(row = 2, column = 2, padx = 5, pady = 5)
b6.grid(row = 3, column = 0, padx = 5, pady = 5)
b5.grid(row = 3, column = 1, padx = 5, pady = 5)
b4.grid(row = 3, column = 2, padx = 5, pady = 5)
b3.grid(row = 4, column = 0, padx = 5, pady = 5)
b2.grid(row = 4, column = 1, padx = 5, pady = 5)
b1.grid(row = 4, column = 2, padx = 5, pady = 5)
b0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)


# FUNCIONES

def click_boton(valor):
	global pos
	datos.insert(pos, valor)
	pos += 1

def borrar():
	datos.delete(0, END)
	pos = 0

def resultado():
	ecuacion = datos.get()
	resultado = eval(ecuacion)
	datos.delete(0, END)
	pos = 0
	datos.insert(pos, resultado)


# AVISAR QUE TODO FUNCIONA

print("All run.")


# ACTUALIZAR PANTALLA

window.mainloop()


# AVISAR QUE SE CERRO TODO

print("Off")
