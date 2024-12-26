from django.test import TestCase

# Create your tests here.
import secrets

# def generate_confirmation_code(length=6):
#     return secrets.token_urlsafe(length)[:length] # обрезаем до нужной длины

# def generate_confirmation_code():
#     import random
#     return str(random.randint(100000, 800000))
#
# confirmation_code = generate_confirmation_code()
#
# print(confirmation_code)

import timeit

# Код, который нужно измерить
code_to_test = """
import secrets
def generate_confirmation_code(length=6):
    return secrets.token_urlsafe(length)[:length] # обрезаем до нужной длины

confirmation_code = generate_confirmation_code()

print(confirmation_code)
"""

# Количество запусков
number = 10000

# Время выполнения
elapsed_time = timeit.timeit(code_to_test, number=number)

print(f"Время выполнения: {elapsed_time:.6f} секунд ({number} запусков)")