from Node_sandbox import Node

class LinkedList:

    def __init__(self, value = None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
    
    def set_head_node(self, new_head):
        self.head_node = new_head

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)

        self.head_node = new_node
        
    def stringify_list(self):
        string_list = ""
        current_node = self.head_node

        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"  
            current_node = current_node.get_next_node()

        return string_list
    
    def remove_node(self, value_to_remove):
        current_node = self.head_node
        
  
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node() 
        else:
            # Recorremos la lista para encontrar el nodo a eliminar
            while current_node and current_node.get_next_node():
                if current_node.get_next_node().get_value() == value_to_remove:
                    # Ajustar los enlaces para omitir el nodo a eliminar
                    current_node.set_next_node(current_node.get_next_node().get_next_node())
                    break  # Salimos del bucle después de eliminar
                current_node = current_node.get_next_node()  # Avanzamos al siguiente nodo

    def swap_nodes(self, val1, val2):
        # Paso 1: Verificar si los valores son iguales
        if val1 == val2:
            print("Los elementos son iguales por lo que no es necesario intercambiarlos")
            return

        # Inicialización de nodos
        node1 = self.get_head_node()  # El nodo que contiene val1
        node2 = self.get_head_node()  # El nodo que contiene val2
        node1_prev = None             # El nodo anterior a node1
        node2_prev = None             # El nodo anterior a node2


        while node1 is not None:
            if node1.get_value() == val1:
                break
            node1_prev = node1
            node1 = node1.get_next_node()

        while node2 is not None:
            if node2.get_value() == val2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()

        if node1 is None or node2 is None:
            print("No es posible realizar el intercambio: uno o más elementos no están en la lista")
            return

        if node1_prev is not None:
            node1_prev.set_next_node(node2)
        else:
            self.set_head_node(node2)

        if node2_prev is not None:
            node2_prev.set_next_node(node1)
        else:
            self.set_head_node(node1)

        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)


