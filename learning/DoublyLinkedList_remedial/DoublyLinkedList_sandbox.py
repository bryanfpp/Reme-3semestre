from Node_sandbox import Node

class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head is not None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head_node = new_head

        if self.tail_node is None:
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail is not None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail

        if self.head_node is None:
            self.head_node = new_tail

    def remove_head(self):
        removed_head = self.head_node

        if removed_head is None:
            return None

        self.head_node = removed_head.get_next_node()

        if self.head_node is not None:
            self.head_node.set_prev_node(None)
        else:
            self.tail_node = None

        return removed_head

    def remove_tail(self):
        removed_tail = self.tail_node

        if removed_tail is None:
            return None

        self.tail_node = removed_tail.get_prev_node()

        if self.tail_node is not None:
            self.tail_node.set_next_node(None)
        else:
            self.head_node = None

        return removed_tail

    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        current_node = self.head_node

        # Buscar el nodo con el valor especificado
        while current_node is not None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break
            current_node = current_node.get_next_node()

        # Si no se encuentra el valor, devolver None
        if node_to_remove is None:
            return None

        # Caso 1: Nodo a eliminar es la cabeza
        if node_to_remove == self.head_node:
            return self.remove_head()

        # Caso 2: Nodo a eliminar es la cola
        if node_to_remove == self.tail_node:
            return self.remove_tail()

        # Caso 3: Nodo está en el medio
        next_node = node_to_remove.get_next_node()
        prev_node = node_to_remove.get_prev_node()

        if next_node is not None:
            next_node.set_prev_node(prev_node)
        if prev_node is not None:
            prev_node.set_next_node(next_node)

        return node_to_remove
