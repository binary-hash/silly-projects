"""
. This calculator is a prototype compunding calculator 
. Author: samuel godwill babua
. Date/time: oct/9/21 ::: 4:14pm
"""
import time
#inputs from users
amount_investing = int(input("Amount Investing: "))
time_end = int(input("Duration(eg: 20): "))
percentage = float(input("Intrest earned each year(eg: 0.20, 0.36): "))
amount_inv = amount_investing

for count in range(time_end + 1):
    amount_percent = amount_inv * percentage
    amount_inv += int(amount_percent)
    print(f"{count} year: {amount_inv}$")
    time.sleep(0.75)