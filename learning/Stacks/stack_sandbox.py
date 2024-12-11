from Node import Node
import logging

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit
        logging.warning(f"Pila inicializada: tamaño actual es {self.size}, límite es {self.limit}.")

    def has_space(self):
        return self.size < self.limit

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if not self.is_empty():
            value = self.top_item.get_value()
            logging.warning(f"El elemento superior de la pila es: {value}")
            return value
        else:
            print("La pila está vacía. No se puede realizar peek.")
            logging.warning("Intento de ver el elemento superior en una pila vacía.")
            return None

    def push(self, value):
        if self.has_space():
            item = Node(value)
            logging.warning(f"Agregando valor {value} a la pila.")

            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            logging.warning(f"Elemento {value} agregado. Ahora es el elemento superior de la pila. Tamaño actual: {self.size}.")
        else:
            print("La pila está llena. ¡No queda espacio!")
            logging.warning(f"Intento de agregar {value} a una pila llena.")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            logging.warning(f"Eliminando elemento {item_to_remove.get_value()} de la pila.")
            
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            logging.warning(f"Elemento eliminado. Tamaño actual de la pila: {self.size}.")
            return item_to_remove.get_value()
        else:
            print("La pila está vacía. No se puede realizar pop.")
            logging.warning("Intento de eliminar un elemento de una pila vacía.")
            return None
