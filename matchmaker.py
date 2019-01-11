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
            #Sex match
            if answers[item][2] == "the opposite sex":
                if answers[item][0] != answers[match_item][0]:
                    score += 1
                else:
                    continue
            elif answers[item][2] == "the same sex":
                if answers[item][0] == answers[match_item][0]:
                    score += 1
                else:
                    continue
            elif answers[item][2] == "both sexes":
                score += 1
            # Age match 
            ages = ["9", "10", "11", "12", "12+"]
            if answers[item][3] == "Younger":
                if ages.index(answers[item][1]) > ages.index(answers[match_item][1]):
                    score += 1
            elif answers[item][3] == "Same age and younger":
                if ages.index(answers[item][1]) >= ages.index(answers[match_item][1]):
                    score += 1
            elif answers[item][3] == "Same age only":
                if ages.index(answers[item][1]) == ages.index(answers[match_item][1]):
                    score += 1
            elif answers[item][3] == "Same age and older":
                if ages.index(answers[item][1]) <= ages.index(answers[match_item][1]):
                    score += 1
            elif answers[item][3] == "Older":
                if ages.index(answers[item][1]) < ages.index(answers[match_item][1]):
                    score += 1
            elif answers[item][3] == "Any age":
                score += 1
            # Hair Match
            if answers[item][4] == answers[match_item][5]:
                score += 1
            # Height Match
            heights = ["no", "Under 4'9\"", "4'9\" to 5'1\"", "5'1\" to 5'4\"", "5'5\" to 5'8\"", "5'9\" to 6'0\"", "over 6'"]
            if answers[item][7] == "Shorter than you":
                if heights.index(answers[item][6]) > heights.index(answers[match_item][6]):
                    score += 1
            elif answers[item][7] == "Shorter or the same height as you":
                if heights.index(answers[item][6]) >= heights.index(answers[match_item][6]):
                    score += 1
            elif answers[item][7] == "The same height as you":
                if heights.index(answers[item][6]) == heights.index(answers[match_item][6]):
                    score += 1
            elif answers[item][7] == "The same height as you or taller":
                if heights.index(answers[item][6]) <= heights.index(answers[match_item][6]):
                    score += 1
            elif answers[item][7] == "Taller than you":
                if heights.index(answers[item][6]) < heights.index(answers[match_item][6]):
                    score += 1
            elif answers[item][7] == "Any height":
                score += 1
            # Personality Trait Match
            if answers[match_item][8] == "A brain" and answers[item][9] == "Intelligence":
                score += 1
            elif answers[match_item][8] == "A comedian" and answers[item][9] == "A sense of humour":
                score += 1
            elif answers[match_item][8] == "Honest and sincere" and answers[item][9] == "Honesty":
                score += 1
            elif answers[match_item][8] == "Very fashionable" and answers[item][9] == "Looks":
                score += 1
            elif answers[match_item][8] == "Compassionate and caring" and answers[item][9] == "Caring":
                score += 1
            elif answers[match_item][8] == "Exciting and enthusiastic" and answers[item][9] == "Enthusiasm":
                score += 1
            elif answers[item][9] == "Doesn't Matter":
                score += 1
            # Standard Match
            for number in range(10, len(answers[item])):
                if answers[item][number] == answers[match_item][number]:
                    score += 1
            matches[item][match_item] = score / len(answers[item])



with open('results.txt','w') as f:
    string = ""
    for item in matches:
        scores = sorted(matches[item].items(), key=lambda x: x[1])
        sorted_scores = scores[::-1]
        string += item + "|*"
        for score in sorted_scores[:10]:
            string += score[0] + "|^" + str((score[1] + 0.3) * 100)[:2] + "%|*"
    f.write(string)

