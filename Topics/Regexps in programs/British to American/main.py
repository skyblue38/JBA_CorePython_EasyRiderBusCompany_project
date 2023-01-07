import re

string = input()
a_words = ou_to_o = re.sub(r'ou', 'o', string, flags=re.IGNORECASE)
print(a_words)
