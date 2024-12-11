def sparse_search(data, search_val):
    print("Datos: " + str(data))
    print("Valor de búsqueda: " + str(search_val))

    if not data:
        print("La lista está vacía.")
        return None

    # Variables para los índices iniciales y finales
    first = 0
    last = len(data) - 1

    # Bucle principal de búsqueda
    while first <= last:
        # Calcular el índice del medio
        mid = (first + last) // 2

        # Comprobar si el medio está vacío
        if data[mid] == "":
            left = mid - 1
            right = mid + 1

            # Encontrar el valor más cercano no vacío
            while True:
                # Verificar si hemos agotado las posibilidades
                if left < first and right > last:
                    print(f"{search_val} no está en el conjunto de datos.")
                    return None

                # Comprobar el valor de la derecha
                elif right <= last and data[right] != "":
                    mid = right
                    break

                # Comprobar el valor de la izquierda
                elif left >= first and data[left] != "":
                    mid = left
                    break

                # Mover los punteros
                left -= 1
                right += 1

        # Verificar si el valor medio es igual al valor de búsqueda
        if data[mid] == search_val:
            print(f"{search_val} encontrado en la posicion {mid}")
            return mid

        # Comprobar si el valor de búsqueda es menor que el medio
        elif search_val < data[mid]:
            last = mid - 1

        # Comprobar si el valor de búsqueda es mayor que el medio
        elif search_val > data[mid]:
            first = mid + 1

    # Si no se encuentra el valor
    print(f"{search_val} no está en el conjunto de datos.")
    return None
