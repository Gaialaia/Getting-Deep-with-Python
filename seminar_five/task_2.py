

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]  #500 300 1050
bonus = ["10%", "5%", "15%"]
#
bonus_cor = []
for i in bonus:
    k = i.replace('%', '')
    k = int(k)
    bonus_cor.append(k)
print(bonus_cor)


h = {i * j//100 for i in salary for j in bonus_cor}

print(h)

j = {names[i]:(salary[i] * bonus_cor[i])//100 for i in range(len(names)) }

print(j)



g = {k:v for (k,v) in zip(names, salary)}


print(g)








