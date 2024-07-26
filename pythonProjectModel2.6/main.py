# def draw_area():
#     for i in area:
#         print(*i)
#
# area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
# print("Добро пожаловать в крестики-нолики")
# print("----------------------------------")
# draw_area()
# for turn in range(1, 10):
#     print(f'Ход: {turn}')
#     if turn % 2 == 0:
#         turn_char = "0"
#         print("Ходят нолики")
#     else:
#         turn_char = "X"
#         print("Ходят крестики")
#     row = int(input("Введите номер строки (1, 2, 3) ")) - 1
#     column = int(input("Введите номер стобца (1, 2, 3) ")) - 1
#     if area[row][column] == "*":
#         area[row][column] = turn_char
#     else:
#         print("Ячейка уже занята, вы пропускаете ход")
#         draw_area()
#         continue
#
#     draw_area()
#     area[0][0] == "X" and area[0][1] == "X" and area[0][2] == "X"


def generate_password(n):
    result = ""
    used_numbers = set()
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if i != j:
                sum = i + j
                if n % sum == 0:
                    result += f'{i}{j}'
                    used_numbers.add(i)
                    used_numbers.add(j)


    return result
n = int(input("Введите число от 3 до 20: "))
if 3 < n < 20:
    result = generate_password(n)
    print("Число:", {n}, "Пароль:4", {result})
else:
    print("Введите число от 3 до 20")



