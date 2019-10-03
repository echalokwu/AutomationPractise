nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List Comprehension
# for n in nums:
#     print(n)
#
# my_list = [n*3 for n in nums]
# print(my_list)
#
# my_list = [n*n for n in nums]
# print(my_list)

# I want 'n' for each 'n' in nums if 'n' is even

# my_list = [n for n in nums if n%2 == 0]
# print(my_list)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)


# # Dictionary Comprehensions
# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# # print zip(names, heros)


# # I want a dict {'name ': 'hero'} for each name, hero in zip(names, heros)
# my_dict = {name: hero for name, hero in zip (names, heros)}
# print(my_dict)

square = [x * x for x in range(10) if x % 2 == 0]
print(square)

# square = []
# for x in range(10):
#     if x % 2 == 10:
#         square.append(x * x)
#     else:
#         print(square)


square = [n * n for n in range(10 + 1)]
print(square)

square = []
for n in range(10 + 1):
    square.append(n*n)
    print(square)
