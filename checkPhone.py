import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('My number is 888-312-1244 and actually it was 123-456-7890')
print(mo)