def countdown(number):
    return [i for i in range(number, -1, -1)]
print(countdown(5))

def imprimir_y_devolver(numbers):
    print(numbers[0])
    return numbers[1]
print(imprimir_y_devolver([1, 2]))

def primero_mas_longitud(numbers):
    return numbers[0] + len(numbers)
print(primero_mas_longitud([1, 2, 3, 4, 5]))

def valores_mayores_que_el_segundo(numbers):
    if len(numbers) < 2:
        return False

    second_value = numbers[1]
    new_list = [num for num in numbers if num > second_value]
    print(len(new_list))
    return new_list
print(valores_mayores_que_el_segundo([5, 2, 3, 2, 1, 4]))
print(valores_mayores_que_el_segundo([3]))

def length_and_value(tamaño, valor):
    return [valor] * tamaño
print(length_and_value(4, 7))
print(length_and_value(6, 2))
