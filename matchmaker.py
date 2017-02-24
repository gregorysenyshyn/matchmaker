import csv

FILENAME = "matchmaker.csv"

answers = {}
with open(FILENAME) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        answers[row[1]] = []
        for number in range(2,len(row)):
            answers[row[1]].append(row[number])


matches = {}
for item in answers:
    matches[item] = {}
    for match_item in answers:
        if item == match_item:
            pass
        else:
            score = 0
            for number in range(len(answers[item])):
                if answers[item][number] == answers[match_item][number]:
                    score += 1
            matches[item][match_item] = score / len(answers[item])
print(matches)
