#Olarte James Robin S.
#BAET 2101

count = int(input("Students: "))
total = 0
highest = None

for i in range(1, count + 1):
    score = int(input(f"Score {i}: "))
    total += score
    if highest is None or score > highest:
        highest = score

avg = total / count
print(f"Total: {total}  Avg: {avg:.2f}")
print(f"Highest: {highest}")