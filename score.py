


scores= [75, 82, 92, 68, 78]
print(scores)

avg = sum(scores)/len(scores)
print(avg)

if avg>=90:
    print("Your Grade is A")
elif avg>=80 and avg<=89:
    print("Your Grade is B")
elif avg>=70 and avg<=79:
    print("Your Grade is a C")
elif avg>=60 and avg<=69:
    print("Your grade is a D")
elif avg<60:
    print("Your grade is a F")


