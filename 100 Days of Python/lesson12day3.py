# print("The Love Calculator is calculating your score...")
name1 = input().upper() # What is your name?
name2 = input().upper() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

score1 = 0
score2 = 0
true_letters = set("TRUE")
love_letters = set("LOVE")

for letter in name1:
    if letter in true_letters:
        score1 += 1
    if letter in love_letters:
        score2 += 1

for letter in name2:
    if letter in true_letters:
        score1 += 1
    if letter in love_letters:
        score2 += 1

score = int(str(score1) + str(score2))


if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

if score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f'Your score is {score}.')


