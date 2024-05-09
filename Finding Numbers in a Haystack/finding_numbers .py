import requests
import re


URL = requests.get('http://py4e-data.dr-chuck.net/regex_sum_2013945.txt').text

pattern = r'[0-9]+'
numbers_regex = re.findall(pattern, URL)
total = 0
for numbers in numbers_regex:    
    total += int(numbers)
print(total)

    

