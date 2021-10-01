todo_list = ['hacer la cama', 'Barrer el patio', 'Comer menos azúcar']

# Podemos eliminar elementos de listas con el método remove()

# todo_list.remove('Hacer la cama')

# print(todo_list)

# Podemos eliminar elementos por su índice con el método pop(indice)

# todo_list.pop(1) 

# print(todo_list)

# Si llalamos al método pop() sin argumento. Se eliminan el último elemento 

# todo_list.pop()

# print(todo_list)

# Tambiém tenemos el método especial "del". Este es un método especial y no es tan frecuente
# Podemos pasar el índice para eliminar un elemento específico  

del todo_list[1]
print(todo_list)

# O eliminar la colección completa, incluyendo la variable que lo referencia 

del todo_list
# print(todo_list)

todo_list = ['Hacer la cama', 'Barrer el patio', 'Comer menos azúcar']

# Existe además el método clear() para vaciar la lista 

todo_list.clear()
print(todo_list)