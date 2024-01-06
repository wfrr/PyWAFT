import random
from string import ascii_letters, digits

import allure


@allure.title('Генерация случайной строки')
def random_string(length: int) -> str:
    letters = ascii_letters + digits
    return ''.join(random.choice(letters) for _ in range(length))
