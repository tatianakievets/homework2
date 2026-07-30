height = float(input("Введите рост (в метрах): "))
weight = float(input("Введите вес (кг): "))

bmi = weight / (height ** 2)

print(f"\nВаш ИМТ: {bmi:.2f}")

if bmi < 18.5:
    print("Недостаточный вес")
elif bmi < 25:
    print("Нормальный вес")
elif bmi < 30:
    print("Избыточный вес")
else:
    print("Ожирение")