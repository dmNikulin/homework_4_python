n = int(input('Введите количество эл-ов первого множества: '))
m = int(input('Введите количество эл-ов второго множества: '))

first_list = set()
second_list = set()

for i in range(n):
    first_list.add(int(input('Введите элемент n - множества: ')))

print('')

for j in range(m):
    second_list.add(int(input('Введите элемент m - множества: ')))

count = 0
empty_list = []

for item in first_list:
    for k in second_list:
        if item == k:
            count += 1
            empty_list.append(item)

empty_list.sort()
print(empty_list)
