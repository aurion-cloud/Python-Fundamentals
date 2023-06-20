
scores = []
while True:
    try:
        score = int(input('Enter a score or 0 to quit: '))
    except ValueError:
        print(f"Please enter a number")
        continue
    if score == 0:
        break
    scores.append(score)
avg = sum(scores)/len(scores)
print(f"Mean of scores is {avg}")


def calc_grades(avg):
    if avg>=90:
        grade = "A"
    elif avg>=80 and avg<=89:
        grade = "B"
    elif avg>=70 and avg<=79:
        grade = "C"
    elif avg>=60 and avg<=69:
        grade = "D"
    elif avg<60:
        grade = "F"
    print(f"Your grade is {grade}")

calc_grades(avg)

