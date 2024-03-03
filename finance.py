import re
from typing import Callable

def generator_numbers(text: str):
    # Регулярний вираз для пошуку дійсних чисел
    pattern = r'\b\d+\.\d+\b'
    # Пошук дійсних чисел у тексті
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    # Виклик функції generator_numbers і підсумовування чисел
    total_sum = sum(func(text))
    return total_sum

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1010.01 як основний дохід, доповнений додатковими надходженнями 66.00 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
