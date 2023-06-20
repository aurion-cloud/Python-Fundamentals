
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
print(f"Mean of scores is {sum(scores)/len(scores)}")



# avg = sum(scores)/len(scores)
# print(avg)

if score>=90:
    print("Your Grade is A")
elif score>=80 and score<=89:
    print("Your Grade is B")
elif score>=70 and score<=79:
    print("Your Grade is a C")
elif score>=60 and score<=69:
    print("Your grade is a D")
elif score<60:
    print("Your grade is a F")


