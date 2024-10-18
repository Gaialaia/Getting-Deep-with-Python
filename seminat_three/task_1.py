


# text = 'Hello, World!'
#
# print(f'{text = :<25}')


my_list = [1, 65, 78, 6, 7, 65, 1, 33, 544, 25]
print(my_list.count(1))
replica = []
for i in my_list:
     if my_list.count(i) > 1 and i not in replica:
        replica.append(i)
        my_list.remove(i)

print(f'replica {replica}, list without duplicates {my_list}')



