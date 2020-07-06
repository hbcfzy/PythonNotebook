"""read numbers form json file"""

import json

f_name = 'numbers.json'
with open(f_name, 'r') as f_obj:
    numbers = json.load(f_obj)

print(numbers)
