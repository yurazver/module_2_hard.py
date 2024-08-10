def generate_password(n):
    result = ""


    pairs = []
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i != j:
                pairs.append((i, j))


    for i, j in pairs:
        pair_sum = i + j
        if n % pair_sum == 0:
            result += str(i) + str(j)

    return result


n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"Нужный пароль для {n}: {password}")
else:
    print("Введите корректное число.")