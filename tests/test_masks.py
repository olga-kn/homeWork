import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


# Функция get_mask_card_number
# Тестирование правильности маскирования номера карты.
assert get_mask_card_number("1478523697412365") == "1478 52** **** 2365"


# Проверка работы функции на различных входных форматах номеров карт, включая нестандартные длины номеров и отсутствие номера карты.
@pytest.mark.parametrize(
    "card_number, result",
    [
        ("123456789ASDFGHJ", "Некорректный ввод"),
        ("1265489", "Некорректный ввод"),
        ("14785623894571236548", "Некорректный ввод"),
        (" ", "Некорректный ввод"),
    ],
)
def test_get_mask_card_number(card_number, result):
    assert get_mask_card_number(card_number) == result


# Функция get_mask_account
# Тестирование правильности маскирования номера счета.
assert get_mask_account("23558766748914578546") == "**8546"


# Проверка работы функции с различными форматами и длинами номеров счетов.
@pytest.mark.parametrize(
    "check, mask",
    [
        ("12356478", "Некорректный ввод"),
        ("564879546ASD56874935", "Некорректный ввод"),
        ("256879431524796587463", "Некорректный ввод"),
        (" ", "Некорректный ввод"),
    ],
)
def test_get_mask_account(check, mask):
    assert get_mask_account(check) == mask
