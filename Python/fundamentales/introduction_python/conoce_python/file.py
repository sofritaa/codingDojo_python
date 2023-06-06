num1 = 42 # Declaración de una variable, valor inicial
num2 = 2.3 # Declaración de una variable, valor inicial
boolean = True #Declaración de una boolean, valor inicial
string = 'Hello World' #declaración de una string

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Declaración de variable, lista inicial 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  # Declaración de variable, diccionario 
fruit = ('blueberry', 'strawberry', 'banana') # Declaración de variable, tupla inicializada

print(type(fruit)) # Imprimir el tipo de dato de la variable "fruit"
print(pizza_toppings[1])# Imprimir el elemento en la posición 1 ('Sausage') de la lista "pizza_toppings"
pizza_toppings.append('Mushrooms')# Agregar el elemento 'Mushrooms' a la lista "pizza_toppings"
print(person['name'])# Imprimir el valor asociado a la clave 'name' en el diccionario "person"

person['name'] = 'George'# Asignar el valor 'George' a la clave 'name' en el diccionario "person"
person['eye_color'] = 'blue' # Asignar el valor 'blue' a la clave 'eye_color' en el diccionario "person"
print(fruit[2])# Imprimir el elemento en la posición 2 ('Banana')de la tupla "fruit"

# Conditional if - elif - else Verificar si el valor de la variable "num1" es mayor a 45 y mostrar el mensaje correspondiente
if num1 > 45: 
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!") # Imprimir mensaje si la longitud de la cadena es menor a 5
elif len(string) > 15:
    print("It's a long word!")# Imprimir mensaje si la longitud de la cadena es mayor a 15
else:
    print("Just right!")  # Imprimir mensaje si la longitud de la cadena está entre 5 y 15

for x in range(5):# Imprimir valores en el rango de 0 a 4
    print(x)
for x in range(2,5):# Imprimir valores en el rango de 2 a 4
    print(x)
for x in range(2,10,3): # Imprimir valores en el rango de 2 a 9 con un incremento de 3
    print(x)
x = 0
while(x < 5): # Imprimir valores mientras x sea menor a 5
    print(x)
    x += 1

pizza_toppings.pop()# Eliminar el último elemento de la lista "pizza_toppings" y retornarlo
pizza_toppings.pop(1)# Eliminar el elemento en la posición 1 de la lista "pizza_toppings"

print(person)# Imprimir el diccionario "person"
person.pop('eye_color')# Eliminar la clave 'eye_color' y su valor asociado del diccionario "person"
print(person)# Imprimir el diccionario "person" después de eliminar la clave 'eye_color'

for topping in pizza_toppings:# Iterar sobre los elementos de la lista "pizza_toppings"
    if topping == 'Pepperoni':# Condicional if para verificar si el topping es 'Pepperoni'
        continue # Continuar con la siguiente iteración del bucle si el topping es 'Pepperoni'
    print('After 1st if statement') # Imprimir mensaje en la consola después de la primera condición if
    if topping == 'Olives':# Condicional if para verificar si el topping es 'Olives
        break # Detener el bucle por completo si el topping es 'Olives'

def print_hello_ten_times():# Definición de la función "print_hello_ten_times
    for num in range(10):# Bucle for que itera sobre los números en el rango de 0 a 9
        print('Hello') # Imprime el mensaje 'Hello' en la salida

print_hello_ten_times()# Llamada a la función "print_hello_ten_times"


def print_hello_x_times(x): # Definición de la función "print_hello_x_times" con un parámetro "x"
    for num in range(x): # Bucle for que itera sobre los números en el rango de 0 a x-1
        print('Hello')# Imprime el mensaje 'Hello' en la salida

print_hello_x_times(4) # Llamada a la función "print_hello_x_times" con el argumento 4

def print_hello_x_or_ten_times(x = 10):# Definición de la función "print_hello_x_or_ten_times" con un parámetro opcional "x" con valor predeterminado 10
    for num in range(x):    # Bucle for que itera sobre los números en el rango de 0 a x-1 (o 0 a 9 si x no se proporciona)
        print('Hello') # Imprime el mensaje 'Hello' en la salida

print_hello_x_or_ten_times() # Llamada a la función "print_hello_x_or_ten_times" sin argumento
print_hello_x_or_ten_times(4)# Llamada a la función "print_hello_x_or_ten_times" con el argumento 4



"""
Bonus section
"""

print(num3)  # Intenta imprimir el valor de la variable 'num3'

num3 = 72  # Asigna el valor 72 a la variable 'num3'.

fruit[0] = 'cranberry'  # Intenta modificar el elemento en la posición 0 de la lista `fruit` asignándole el valor 'cranberry'. Esto dará lugar a un error ya que las tuplas en Python son inmutables y no se pueden modificar elementos individuales.

print(person['favorite_team'])  # Intenta imprimir el valor de la clave 'favorite_team' en el diccionario "person".

print(pizza_toppings[7])  # Intenta acceder al elemento en la posición 7 de la lista "pizza_toppings".

print(boolean)  # Intenta imprimir el valor de la variable 'boolean'.

fruit.append('raspberry')  # Agrega el elemento 'raspberry' al final de la lista 'fruit' utilizando el método "append()".

fruit.pop(1)  # Elimina el elemento en la posición 1 de la lista `fruit` utilizando el método "pop()".
