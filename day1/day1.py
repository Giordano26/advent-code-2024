import pandas as pd
import numpy as np 

df = pd.read_csv('./input.csv', header=None)

df[['A', 'B']] = df[0].str.split(expand=True)


arr_a = df['A'].to_numpy()
arr_b = df['B'].to_numpy()

sorted_a = np.sort(arr_a).astype(int)
sorted_b = np.sort(arr_b).astype(int)

similarity_dict = {}

locations_diff = 0
for index in range(sorted_a.size):
	locations_diff += abs(sorted_b[index] - sorted_a[index])
	right_number = sorted_b[index]
	if right_number in similarity_dict:
		similarity_dict[right_number] += 1
	else:
		similarity_dict[right_number] = 1

similartity_sum = 0
for number in sorted_a:
	if number not in similarity_dict:
		continue
	similartity_sum += number * similarity_dict[number]

print('locations diff', locations_diff) #first solution
print('similarity sum', similartity_sum) #second solution


