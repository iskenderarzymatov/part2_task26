spisok = input("Введите цифры: ").split()
new_spisok = []
for i in spisok:
    new_spisok.append(int(i))
even_numbers = 0
odd_numbers = 0
for x in new_spisok:
    if x % 2 == 0:
        print(x)
        even_numbers += 1
    else:
        odd_numbers += 1
print("Четных чисел: ", even_numbers)
print("Нечетных чисел: ", odd_numbers