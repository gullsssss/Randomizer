import random
print("Это генератор рандомных чисел, чтобы использовать")
while True:
    Fn = int(input("Введите от скольки будет идти счет: "))
    Sn = int(input("Введите до скольки будет идти счет: "))
    if a > b:
        print("Число от скольки не может быть больше до скольки, введите все заново")
        continue
    result = random.randint(Fn,Sn)
    print("Результат: ",c)
    con = input("Продолжить? y/n :")
    if con != "y":
        break
