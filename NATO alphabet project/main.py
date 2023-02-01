numbers = [1, 2, 3, 4, 5, 6]
new_numbers = [1 + n for n in numbers]
print(new_numbers)

name = "michael"
letter_list = [letter for letter in name]
print(letter_list)

new_range = [n*2 for n in range(1, 5)] # [1, 2, 3, 4]
print(new_range)

names = ["Katara", "Toph", "Aang", "Zuko", "Sokka"]
short_names = [name for name in names if len(name)<5]
print(short_names)

names = ["Katara", "Toph", "Aang", "Zuko", "Sokka"]
upper_names = [name.upper() for name in names if len(name)>4]
print(upper_names)
