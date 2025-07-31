from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(info_card: str) -> str:
    """Возвращает замаскированный номер счета или карты."""
    if not info_card.strip():
        return "Некорректный ввод"

    parts = info_card.strip().split()
    card_number = parts[-1]

    if parts[0].lower() == "счет":
        return f"{parts[0]} {get_mask_account(card_number)}"
    else:
        name_part = " ".join(parts[:-1])
        return f"{name_part} {get_mask_card_number(card_number)}"


def get_date(date_str: str) -> str:
    """Преобразует дату в формат 'ДД.ММ.ГГГГ'."""
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return "Неверный формат даты"
