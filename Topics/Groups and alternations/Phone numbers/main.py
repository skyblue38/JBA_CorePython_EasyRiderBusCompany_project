import re

string = input().strip()
regex_phone_pattern = r'\+(\d{1})[ |-]?(\d{1,3})[ |-]?([\d| |-]+)'
found = re.match(regex_phone_pattern, string)
if found:
    print(f'Full number: {string}')
    print(f'Country code: {found.group(1)}')
    print(f'Area code: {found.group(2)}')
    print(f'Number: {found.group(3)}')
else:
    print("No match")
