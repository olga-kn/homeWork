import pytest

from src.widget import mask_account_card
from src.widget import get_date

# Функция mask_account_card
# Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"

assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"


# Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
@pytest.mark.parametrize(
    "card_info, masks_num",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("счет 35383033474447895560", "счет **5560"),
        ("", "Некорректный ввод"),
    ],
)
def test_mask_account_card(card_info, masks_num):
    assert mask_account_card(card_info) == masks_num


# Функция get_date
# Тестирование правильности преобразования даты.
assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


# Проверка работы функции на различных входных форматах даты.
@pytest.mark.parametrize(
    "info, date",
    [
        ("", "Неверный формат даты"),
        ("2024-30-11", "Неверный формат даты"),
        ("2024-02-13", "13.02.2024"),
        ("15-03-2025", "Неверный формат даты"),
    ],
)
def test_get_date(info, date):
    assert get_date(info) == date
