def binary_search(sorted_list, target):
    # Inicializa los punteros
    left_pointer = 0
    right_pointer = len(sorted_list)

    # Ciclo mientras los punteros no se crucen
    while left_pointer < right_pointer:
        # Calcula el índice medio y el valor medio
        mid_idx = (left_pointer + right_pointer) // 2
        mid_val = sorted_list[mid_idx]

        # Verifica si el valor medio es igual al objetivo
        if mid_val == target:
            return mid_idx

        # Ajusta los punteros según el valor del objetivo
        elif target < mid_val:
            right_pointer = mid_idx
        else:
            left_pointer = mid_idx + 1

    # Si no se encuentra el objetivo, regresa un mensaje
    return "Valor no encontrado"
