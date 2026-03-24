import random
while True:
    print("Это генератор ранжомных чисел, чтобы использовать")
    a = int(input("Введите от скольки будет идти счет: "))
    b = int(input("Введите до скольки будет идти счет: "))
    if a > b:
        print("Число от скольки не может быть больше до скольки, введите все заново")
        continue
    c = random.randint(a,b)
    print("Результат: ",c)
    con = input("Продолжить? y/n :")
    if con != "y":
        break
