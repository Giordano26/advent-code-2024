import pandas as pd

df = pd.read_csv('./input.csv', header=None)

reports_result = df[0]

safe_reports = 0

for results in reports_result:
	results_arr = results.split()

	last_diff = 0
	vars_ok = 0
	for index in range(len(results_arr) - 1):
		results_diff = int(results_arr[index]) - int(results_arr[index+1])

		if abs(results_diff) < 1 or abs(results_diff) > 3:
			break

		if results_diff > 0 and last_diff < 0 :
			break

		if results_diff < 0 and last_diff > 0 :
			break
			
		last_diff = results_diff
		vars_ok += 1

	if(vars_ok == len(results_arr) - 1):
		safe_reports += 1

print("number of safe reports", safe_reports)