token = ''
weather_api_key = "467e9329e78d70b728147eb922f99675"
group_id = ''

import re
def check_group_format(group_number):
    pattern = r'^[A-Za-zА-Яа-я]{4}-\d{2}-\d{2}$'
    match = re.match(pattern, group_number)
    if match:
        return not None
    else:
        return None


def check_proffesor_pattern(string):
    pattern = r'^[А-ЯЁ][а-яё]+\s[А-ЯЁ]\.[А-ЯЁ]\.$'
    match = re.match(pattern, string)
    if match:
        return True
    else:
        return False

