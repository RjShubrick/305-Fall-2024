import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

total_sum = num1 + num2 + num3


print(f"The sum of {num1}, {num2}, and {num3} is: {total_sum}")

grade1 = float(input("Enter the first grade (0-100): "))
grade2 = float(input("Enter the second grade (0-100): "))
grade3 = float(input("Enter the third grade (0-100): "))


average = (grade1 + grade2 + grade3) / 3

if average > 80:
    print("Grade A")
elif average > 70:
    print("Grade B")
else:
    print("Grade F")


