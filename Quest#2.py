# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def list_of_prime_factors_of_a_number(N: int):
    factors = []
    for i in range(2, N+1):
        if N % i == 0:
            count = 1
            for j in range(2, i//2+1):
                if i % j == 0:
                    count = 0
                    break
                if count == 1:
                    factors.append(i)
    return factors

print(list_of_prime_factors_of_a_number(20))
print(list_of_prime_factors_of_a_number(30))
