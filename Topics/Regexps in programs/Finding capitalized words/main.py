import re

string = input().strip()
words = string.split()
capitals = re.compile(r'[A-Z]+')
capital_words = [w for w in words if capitals.match(w) is not None]
print('Capitalized words:', ', '.join(capital_words))
numbers = re.compile(r'\d+')
digit_words = [numbers.match(s).group() for s in words if numbers.match(s) is not None]
print('Digits:', ', '.join(digit_words))
