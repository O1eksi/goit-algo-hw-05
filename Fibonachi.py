def caching_fibonacci():
    # Створити порожній словник для кешування
    cache = {}

    # Визначення внутрішньої функції fibonacci
    def fibonacci(n):
        # Перевірка наявності числа Фібоначчі у кеші
        if n in cache:
            return cache[n]
        # Базові випадки: fib(0) = 0, fib(1) = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        # Обчислення числа Фібоначчі рекурсивно
        result = fibonacci(n - 1) + fibonacci(n - 2)
        # Зберігання результату у кеші
        cache[n] = result
        return result

    # Повернення внутрішньої функції fibonacci
    return fibonacci

# Приклад використання:
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
