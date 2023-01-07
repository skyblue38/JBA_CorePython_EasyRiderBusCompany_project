import re

re_pattern = '[A-Za-z]'
text = input()
result = re.match(re_pattern, text)
if result:
    print('Thank you!')
else:
    print('Oops! The username has to start with a letter.')
    
