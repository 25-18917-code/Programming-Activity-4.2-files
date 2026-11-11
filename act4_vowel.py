#Olarte James Robin
#BAET 2101

sentence = input("Sentence: ")
count = 0

for ch in sentence:
    if ch.lower() in "aeiou":
        count += 1

print(f"Vowels: {count}")