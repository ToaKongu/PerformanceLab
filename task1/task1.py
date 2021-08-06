import json
import sys


def filling(val):
    for i in range(len(val)):
        if val[i].get('value') is not None:
            val[i]['value'] = values_dict[val[i]['id']]
        if val[i].get('values') is not None:
            filling(val[i]['values'])


with open(f'{sys.argv[1]}', 'r') as f:
    tests = json.loads(f.read())

with open(f'{sys.argv[2]}', 'r') as f:
    values = json.loads(f.read())

values_dict = {}
values = values['values']
for i in values:
    values_dict[i['id']] = i['value']

filling(tests['tests'])

with open("report.json", "w") as f:
    json.dump(tests, f, ensure_ascii=False, indent=1)
