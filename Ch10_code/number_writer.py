"""write numbers into json file"""

import json

numbers = [2, 3, 5, 7, 11, 13]

f_name = 'numbers.json'
with open(f_name, 'w') as f_obj:
    json.dump(numbers, f_obj)