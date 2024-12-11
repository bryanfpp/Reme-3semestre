from Node_sandbox import Node
import logging

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            logging.warning(f"¡Agregando {item_to_add.get_value()} a la cola!")
            
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            
            self.size += 1
        else:
            logging.warning("¡Lo sentimos, no hay más espacio!")

    def dequeue(self):
        """
        Elimina el nodo al inicio de la cola y devuelve su valor.
        """
        if not self.is_empty():
            item_to_remove = self.head
            logging.warning(f"¡Eliminando {item_to_remove.get_value()} de la cola!")
            
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            
            self.size -= 1
            return item_to_remove.get_value()
        else:
            logging.warning("¡Esta cola está totalmente vacía!")
            return None

    def peek(self):
        if self.is_empty():
            logging.warning("¡No hay nada que ver aquí!")
            return None
        return self.head.get_value()

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size is None:
            return True
        return self.get_size() < self.max_size

    def is_empty(self):
        return self.size == 0
