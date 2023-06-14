def ordenamiento_por_insercion(lista):
    n = len(lista)
    for i in range(1, n):
        valor_actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valor_actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor_actual
    
    return lista
lista = [5, 2, 9, 1, 3]
lista_ordenada = ordenamiento_por_insercion(lista)
print(lista_ordenada)
