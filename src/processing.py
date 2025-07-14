from datetime import datetime
from typing import Dict
from typing import List


def filter_by_state(data_list: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция фильтрации по статусу операции"""
    result_list = []
    for dict in data_list:
        if dict.get("state") == state:
            result_list.append(dict)
        else:
            continue
    return result_list


def sort_by_date(list_of_dict: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """Функция фильтрации по дате опрерации"""
    sorted_list_of_dict = sorted(list_of_dict, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
    return sorted_list_of_dict
