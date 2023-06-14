def ordenamiento_por_seleccion(lista):
    n = len(lista)
    for i in range(n-1):

        indice_minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    
    return lista
lista = [5, 2, 9, 1, 3]
lista_ordenada = ordenamiento_por_seleccion(lista)
print(lista_ordenada)
