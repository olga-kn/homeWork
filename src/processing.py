from datetime import datetime
from typing import Dict
from typing import List


def filter_by_state(list_of_dic: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция фильтрации по статусу операции"""
    return list(filter(lambda operation: operation.get("state") == state, list_of_dic))


def sort_by_date(list_of_dict: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """Функция фильтрации по дате опрерации"""
    try:
        sorted_list_of_dict = sorted(list_of_dict, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
        return sorted_list_of_dict
    except ValueError:
        return "Неверный формат даты"
