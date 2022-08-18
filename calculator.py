a = float(input("Введите первое число:  "))
b = float(input("Введите второе число:  "))
addition = input("Введите оперaтор: ")
result = 0
if (type())
if(addition == "+") :
    result = a + b
elif(addition == "-"):
    result = a - b
elif (addition == "*"):
    result = a * b
elif (addition == "/" and b != 0):
    result = a / b
else :
    print("Пример или оператор неправильные")

if(b == 0 and addition == "/") :
    print("На ноль делить нельзя!")
else:
    print(f"Результат :",result)




