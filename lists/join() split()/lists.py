# ******************************************** Методы join() и split() *************************

# Построчный вывод ==================

# s = input()
# words = s.split()
# print(*words, sep='\n')

# Инициалы ==================

# s = input()
# word = s.split()
# sp = []
# sp.append(word[0][0])
# del word[0]
# sp.append(word[0][0])
# del word[0]
# sp.append(word[0][0] + '.')
# res = '.'.join(sp)
# print(res)

# Windows OS ==================

# s = input()

# word = s.split('\\')
# print(*word, sep='\n')

# Диаграмма ==================

# def draw_bar_chart(numbers):
#     for num in numbers:
#         print('+' * num)

# input_string = input()

# numbers = list(map(int, input_string.split()))

# draw_bar_chart(numbers)

# Корректный ip-адрес ==================

# def is_valid_ip_address(ip_str):
#     try:
#         octets = ip_str.split('.')
        
#         if len(octets) != 4:
#             return "НЕТ"
        
#         for octet in octets:
#             value = int(octet)
#             if not (0 <= value <= 255):
#                 return "НЕТ"
        
#         return "ДА"
    
#     except ValueError:
#         return "НЕТ"

# input_ip = input()

# result = is_valid_ip_address(input_ip)
# print(result)

# Добавь разделитель ==================

# s = input()
# w = input()

# print(w.join(s))

# Все сразу 2 🌶️

# numbers = [8, 9, 10, 11]
# numbers.insert(1, 17)
# numbers.extend([4,5,6])
# del numbers[0]
# numbers *= 2
# numbers.insert(3, 25)
# print(numbers)

# Переставить min и max

s = input().split()
sp = []

for i in range(1, len(s) + 1):
    sp.append(int(i))

sp_max = max(sp)
sp_min = min(sp)

sp1 = sp_max, sp_min = sp_max, sp_min
sp.append(sp1)

print(sp)