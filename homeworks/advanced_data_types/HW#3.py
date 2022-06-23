int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

# 1. Define the id of next variables:
print(f'int_a={id(int_a)}')
print(f'str_b={id(str_b)}')
print(f'set_c={id(set_c)}')
print(f'lst_d={id(lst_d)}')
print(f'dict_e={id(dict_e)}')
# int_a=4515989424
# str_b=4518135984
# set_c=4518339168
# lst_d=4518135680
# dict_e=4518135872

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d += [4, 5]
# [1, 2, 3, 4, 5]
print(f'new lst_d id = {id(lst_d)}')
# new lst_d id = 4442769280

# 3. Define the type of each object from step 1.
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

# <class 'int'>
# <class 'str'>
# <class 'set'>
# <class 'list'>
# <class 'dict'>

# 4*. Check the type of the objects by using isinstance.
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))
# True
# True
# True
# True
# True

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

# 5. With .format and curly braces {}
print('Anna has {} apples and {} peaches'.format(2, 4))
# Anna has 2 apples and 4 peaches

# 6. By passing index numbers into the curly braces.
print('Anna has {1} apples and {0} peaches'.format(2, 4))
# Anna has 4 apples and 2 peaches

# 7. By using keyword arguments into the curly braces.
print('Anna has {number_of_apples} apples and {number_of_peaches} peaches'.format(number_of_apples= 2, number_of_peaches = 4))
# Anna has 2 apples and 4 peaches

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print('Anna has {:5} apples and {:3} peaches'.format(2, 4))
# Anna has     2 apples and   4 peaches

# 9. With f-strings and variables
number_of_apples = 2
number_of_peaches = 4
print(f'Anna has {number_of_apples} apples and {number_of_peaches} peaches')
# Anna has 2 apples and 4 peaches

# 10. With % operator
print('Anna has %s apples and %s peaches' %(number_of_apples, number_of_peaches))
# Anna has 2 apples and 4 peaches

# 11*. With variable substitutions by name (hint: by using dict)
data = {'number_of_apples':9, 'number_of_peaches':8}
print(f'Anna has {data["number_of_apples"]} apples and {data["number_of_peaches"]} peaches')
# Anna has 9 apples and 8 peaches

# Comprehensions:
# (1)
#lst = []
# for num in range(10):
#    if num % 2 == 1:
#         lst.append(num ** 2)
 #   else:
 #        lst.append(num ** 4)
# print(lst)
#
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

# 12. Convert (1) to list comprehension
lst_comp = [num **2 if num % 2 == 1 else num **4 for num in range(10)]
print(lst_comp)
#[0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

# 13. Convert (2) to regular for with if-else

lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)
# [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

# 14. Convert (3) to dict comprehension.
#d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
d = {num: num ** 2 for num in range(1,11) if num % 2 == 1}
print(d)
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# 15*. Convert (4) to dict comprehension.

# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
d = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1,11)}
print(d)
# {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

# 16. Convert (5) to regular for with if.
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
d = {}
for num in range(10):
    if num % 4 == 0:
        d[num] = num **3
print(d)
# {0: 0, 4: 64, 8: 512}

# 17*. Convert (6) to regular for with if-else.
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
d = {}
for num in range(10):
    if num **3 % 4 == 0:
        d[num] = num **3
    else:
        d[num] = num
print(d)
# {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}

# 18. Convert (7) to lambda function
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
foo = lambda x, y: x if x < y else y
print(foo(7, 11))
# 7

# 19*. Convert (8) to regular function
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo(8, 9, 5))
# 9

lst = [5, 18, 1, 24, 33, 15, 13, 55]
# 20. Sort lst_to_sort from min to max
print(sorted(lst))
# [1, 5, 13, 15, 18, 24, 33, 55]

# 21. Sort lst_to_sort from max to min
lst.sort(reverse=True)
print(lst)
# [55, 33, 24, 18, 15, 13, 5, 1]

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print(list(map(lambda x: x * 2, lst)))
# [110, 66, 48, 36, 30, 26, 10, 2]

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
print(list(map(lambda x, y: x ** y, list_A, list_B)))
# [32, 729, 16384]
# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print(list(filter(lambda x: x % 2 == 1, lst)))
#[55, 33, 15, 13, 5, 1]

# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print(list(filter(lambda x: x < 0 ,range(-10, 10))))
# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 26*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
print(list(filter(lambda x: x == x in list_1, list_2)))
# [2, 3, 5, 7]