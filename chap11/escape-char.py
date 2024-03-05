# using the escape character \ to indicate we want what is actually there, not what it symbolizes in re:

import re

text = 'we won $40000000.00 in the lottery tomorrow'

x = re.findall('(\$[0-9.]+)', text)  # we need the + for greediness
print(x)