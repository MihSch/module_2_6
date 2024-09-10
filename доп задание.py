from random import randint

n = randint (3,20)
result = ''
print(n)
for i in range (1, n):
    for j in range (i+1, n):
        if n % (i + j) == 0:
            result += f'{i}{j}'

print(f'{n} - {result}')







# 
# def more_than_five(lst):
#     new_lst = []
#     for num in lst:
#         if abs(num) > 5:
#             new_lst.append(num)
#     return new_lst
# print(more_than_five([1, 66, -11]))