import unittest
from Node_sandbox import Node
from DoublyLinkedList_sandbox import DoublyLinkedList

class TestDoublyLinkedListRemoveTail(unittest.TestCase):

    def setUp(self):
        self.doubly_linked_list = DoublyLinkedList()

    def test_remove_tail_single_node(self):
        # Caso de prueba con solo un nodo
        self.doubly_linked_list.add_to_tail(10)
        removed_value = self.doubly_linked_list.remove_tail()
        self.assertEqual(removed_value, 10, "El valor eliminado debería ser 10.")
        self.assertIsNone(self.doubly_linked_list.head_node, "La cabeza debería ser None después de eliminar el único nodo.")
        self.assertIsNone(self.doubly_linked_list.tail_node, "La cola también debería ser None después de eliminar el único nodo.")

    def test_remove_tail_multiple_nodes(self):
        # Caso de prueba con múltiples nodos
        self.doubly_linked_list.add_to_tail(10)
        self.doubly_linked_list.add_to_tail(20)
        self.doubly_linked_list.add_to_tail(30)

        removed_value = self.doubly_linked_list.remove_tail()
        self.assertEqual(removed_value, 30, "El valor eliminado debería ser 30, que es el nodo cola.")
        self.assertEqual(self.doubly_linked_list.tail_node.get_value(), 20, "El nuevo nodo cola debería ser 20.")

        removed_value = self.doubly_linked_list.remove_tail()
        self.assertEqual(removed_value, 20, "El siguiente nodo eliminado debería ser 20.")
        self.assertEqual(self.doubly_linked_list.tail_node.get_value(), 10, "El nuevo nodo cola debería ser 10.")

    def test_remove_tail_empty_list(self):
        # Caso de prueba con una lista vacía
        removed_value = self.doubly_linked_list.remove_tail()
        self.assertIsNone(removed_value, "El valor eliminado debería ser None si la lista está vacía.")

if __name__ == '__main__':
    unittest.main()
