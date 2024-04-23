immutable_var = 1, ['a', 'b', 'c'], True, 3.14 # Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
print(immutable_var) # Выполните операции вывода кортежа immutable_var на экран.
immutable_var[1][1] = 'f' # Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
#immutable_var[2] = False нельзя менять элемент кортежа, но можно элементы внутри элемента кортежа
print(immutable_var)
mutable_list = ['a','b','c'] # Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
mutable_list[0] = 14
mutable_list[1] = True # Измените элементы списка mutable_list.
print(mutable_list) # Выведите на экран измененный список mutable_list.
