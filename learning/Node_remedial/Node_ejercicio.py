# Ejercicio: Usando la clase Node

from Node_sandbox import Node

Juan = Node("Es jefe de jefes")
Yady = Node("Le gustan las flores")
Giovany = Node("Le gustan las princesas")

Juan.set_next_node(Giovany)
Giovany.set_next_node(Yady)

Giovany_data = Giovany.get_value()
Yady_data = Yady.get_value()

print(Giovany_data)
print(Yady_data)