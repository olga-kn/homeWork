from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция маскировки номера банковской карты"""
    card_number = str(card_number)
    if len(card_number) == 16 and card_number.isdigit():
        mask_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return mask_number
    else:
        return "Некорректный ввод"


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция маскировки номера банковского счета"""
    account_number = str(account_number)
    if len(account_number) == 20 and account_number.isdigit():
        mask_account = f"**{account_number[-4:]}"
        return mask_account
    else:
        return "Некорректный ввод"