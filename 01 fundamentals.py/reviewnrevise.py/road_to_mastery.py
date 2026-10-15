#count how many times a status value appaears in a list statuses = [200, 500, 200, 404, 500, 200]
statuses = [200, 500, 200, 404, 500, 200]
counts = {}
for status in statuses:
    if status in counts:
        counts[status] += 1
    else:
        counts[status] =1
print("counts of statuses:", counts)

#names = ["Asha", "Ravi", "Asha", "Meena", "Ravi", "Asha"]Count the names in the list
names = ["Asha", "Ravi", "Asha", "Meena", "Ravi", "Asha"]
name_counts = {}
for name in names:
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1
print("Counts of names:", name_counts)

#scores = [80, 90, 80, 70, 90, 80, 60]find the most repeated score in the list
scores = [80, 90, 80, 70, 90, 80, 60]
score_repeated = {}
for score in scores:
    if score in score_repeated:
        score_repeated[score] += 1
    else:
        score_repeated[score] = 1
#for finding the most repeated score and frequency
most_repeated_score = max(score_repeated, key = score_repeated.get)
Frequency = score_repeated[most_repeated_score]
print("Most repeated score:", most_repeated_score, "with frequency:", Frequency)

#Find the first repeated number.
numbers = [4, 7, 2, 7, 4, 9]
seen = set()
first_repeated = None
for num in numbers:
    if num in seen:
        first_repeated = num
        break
    seen.add(num)
print("First repeated number:", first_repeated)
#Find the first non repeated numbers = [4, 7, 2, 7, 4, 9, 2, 11]
numbers = [4, 7, 2, 7, 4, 9, 2, 11]
counts = {}
first_non_repeated = None
for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
for num in numbers:
    if counts[num] == 1:
        first_non_repeated = num
        break
print("First non-repeated number:", first_non_repeated)

