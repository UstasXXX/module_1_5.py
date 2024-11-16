immutable_var = (1, 2, 3, 'education', False)
print(immutable_var)
#immutable_var[-1]=True (у кортежей нет ни одного метода или команды на изменение)
mutable_list = [1, 2, 3, 'education', True]
mutable_list[-2]= 'Homework'
mutable_list[-1]= False
print(mutable_list)