with open("input.txt", "r") as file:
    data = file.readlines()
increasing = 0
prev = data[0]
for each in data:
    if each >= prev:
        increasing += 1
    prev = each

print(increasing)
