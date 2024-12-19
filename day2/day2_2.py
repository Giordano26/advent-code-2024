import pandas as pd

df = pd.read_csv('./input.csv', header=None)

reports_result = df[0]

def is_safe(results_arr):
    last_diff = 0
    for index in range(len(results_arr) - 1):
        results_diff = int(results_arr[index]) - int(results_arr[index+1])
        if abs(results_diff) < 1 or abs(results_diff) > 3:
            return False
        if results_diff > 0 and last_diff < 0:
            return False
        if results_diff < 0 and last_diff > 0:
            return False
        last_diff = results_diff
    return True

def can_be_made_safe(results_arr):
    for i in range(len(results_arr)):
        modified_arr = results_arr[:i] + results_arr[i+1:]
        if is_safe(modified_arr):
            return True
    return False

safe_reports = 0
for results in reports_result:
    results_arr = results.split()
    if is_safe(results_arr) or can_be_made_safe(results_arr):
        safe_reports += 1

print("number of safe reports", safe_reports)