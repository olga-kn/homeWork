from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция маскировки номера банковской карты"""
    card_number = str(card_number)
    mask_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return mask_number


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция маскировки номера банковского счета"""
    account_number = str(account_number)
    mask_account = f"**{account_number[-4:]}"
    return mask_account



