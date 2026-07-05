#new calculator
total = None
while True:
    if total is None:
        num_input = input("Введи первое число (или '=' для выхода): ").strip()
    else:
        num_input = input("Введи число (или '=' для выхода): ").strip()
    
    if num_input == "=":
        break
        
    try:
        if "." in num_input:
            number = float(num_input)
        else:
            number = int(num_input)
    except ValueError:
        print("Это не похоже на число. Попробуй еще раз.")
        continue

    if total is None:
        total = number
        print(f"Текущий результат: {total}")
        continue

    while True:
        op = input(f"Введи оператор (+, -, *, /): ").strip()
        if op in ["+", "-", "*", "/"]:
            break
        print("Неверный оператор! Используй только +, -, * или /")

    if op == "+":
        total += number
    elif op == "-":
        total -= number
    elif op == "*":
        total *= number
    elif op == "/":
        if number == 0:
            print("Деление на ноль!")
            continue
        total /= number

    print(f"Результат: {total}")

print(f"Финальный результат: {total}")
