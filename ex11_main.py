__author__ = 'lauri'
__DATE__ = '18.05.2018'
'''
Ask the user for a number and determine whether the number
is prime or not. (For those who have forgotten, a prime
number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4
to help you. Take this opportunity to practice using
functions, described below.



'''



#
# n=30
# lista = [i for i in range(2,n+1)]
# if n<=1:
#     l = []
# elif n == 2:
#         l = [2]
# else:
#     for i in lista:
#         for j in range(2*i,n,i):
#             for k in range(1,len(lista)):
#                 if lista[k] == j:
#                     del lista[k]
#                     break;
# print(lista)
#
#
#
# lista = [i for i in range(0,n+1)]
#
# for i in range(2,n):
#     if lista[i] != 0:
#         for j in range(2*i,n,i):
#             lista[j] = 0
# del lista[1]
# print([i for i in lista if i !=0])




# n = int(input('Introduceti numarul: '))
# prime = ''
# if n > 2:
#     for i in range(2,(n//2)+1):
#         if n % i == 0:
#             prime = 'nu'
#             break
# elif n == 1:
#     prime = 'nu'
# else:
#     pass
#
#
#
# print('Numarul {} e prim'.format(prime))


num = int(input('Insert a number: '))

def is_prime(n):
    a = [x for x in range(2, (num // 2 )+1) if num % x == 0]
    m = 'NOT prime'
    if num > 1:
        if len(a) == 0:
             m = 'prime'
    print(m)

is_prime(num)



