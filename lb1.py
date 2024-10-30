import random

def print_fragments(text, N):
    for i in range(0, len(text), N):
        print(text[i:i+N])

def add_random_digits(text):
    for i in range(0, len(text), 2):
        fragment = text[i:i+2]
        random_digits = f"{random.randint(0, 9)}{random.randint(0, 9)}"
        print(fragment + random_digits)

input_text = input("Введіть текст: ")
N = int(input("Введіть кількість символів для першої функції: "))

print("Фрагменти по", N, "символів:")
print_fragments(input_text, N)

print("\nФрагменти по 2 символи з доданими випадковими цифрами:")
add_random_digits(input_text)
