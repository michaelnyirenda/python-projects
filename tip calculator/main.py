print("welcome to the tip calculator")
total = float(input("what was the total bill? $"))
percent = int(input("what percentage would you like to give? 10, 12, or 15? "))
peeps = int(input("how many people to split the bill? "))
tip = total * (percent * 0.01)
total += tip
final = round(total/peeps, 2)
message = f"each person should pay: ${final}"
print(message)