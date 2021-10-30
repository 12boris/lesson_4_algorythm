import cProfile, math


n = 900

def loop(n):
    num = 2
    i = 0
    while i != n:
        num = num * math.sqrt(num)
        i += 1
    print(f'Результат после {n} итераций равен {num} (Цикл)')


def recursion(i, num, n):
    if i == n:
        print(f'Результат после {i} итераций равен {num} (Рекурсия)')
        return num
    elif i <= n:
        return recursion(i + 1, num * math.sqrt(num), n)
    

"""2. Написать два алгоритма нахождения i-го по счёту простого числа."""

nu = int(input('Введите номер простого числа: '))


"""Без использования «Решета Эратосфена"""

def algo(n):
    primes = []
    for i in range(2, 10000):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    print(f'Искомое простое число = {primes[n - 1]} (БЕЗ)\n')


cProfile.run('algo(nu)')

print('*' * 100, '\n')


def sieve(n):
    primes = []
    nums = [i for i in range(2, 10000)]

    for i in nums:
        if i != 0:
            primes.append(i)
            for j in nums[i:]:
                if j % i == 0:
                    nums[j - 2] = 0
    print(f'Искомое простое число = {primes[n - 1]} (РЕШЕТО) \n')

cProfile.run('sieve(nu)')
