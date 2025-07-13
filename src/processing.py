def filter_by_state(data_list: list, state: str = 'EXECUTED') -> list:
    """ Функция фильтрации по статусу операции """
    result_list = []
    for dict in data_list:
        if dict.get('state') == state:
            result_list.append(dict)
        else:
                continue
    return result_list

