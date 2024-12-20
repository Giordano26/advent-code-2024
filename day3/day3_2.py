import re

corretct_token = r"(?:mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\))"

found_tokens = []
with open('./input.txt', 'r') as file:
	for line in file:
		found = re.findall(corretct_token, line)

		found_tokens.extend(found)

final_sum = 0
enabled = True
for token in found_tokens:
	if token == "do()":
		enabled = True
		continue

	if token == "don't()":
		enabled = False
		continue
	
	if enabled:
		token = token.translate({ord(i): None for i in 'mul()'}) #translates m u l ( ) to Void
		x,y = token.split(',')
		final_sum += int(x) * int(y)

print(final_sum)

