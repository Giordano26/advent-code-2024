import re

corretct_token = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

found_tokens = []
with open('./input.txt', 'r') as file:
	for line in file:
		found = re.findall(corretct_token, line)

		found_tokens.extend(found)

final_sum = 0
for token in found_tokens:
	token = token.translate({ord(i): None for i in 'mul()'}) #translates m u l ( ) to Void
	x,y = token.split(',')
	final_sum += int(x) * int(y)

print(final_sum)

