import random

questions = [
    ["What is the capital of Japan?", "A. Seoul", "B. Beijing", "C. Tokyo", "D. Bangkok", "C","50,000"],
    ["Which gas do plants absorb from the atmosphere?", "A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen", "C", "10,000"],
    ["What's the square of 25?", "A. 550", "B. 225", "C. 2205", "D. 625", "D", "33000"],
    ["Who wrote 'A Good Girl's Guide to Murder'?", "A. Holly Jackson", "B. William Shakespeare", "C. Mark Twain", "D. Charles Dickens", "A","90,000"],
    ["What is the chemical symbol for water?", "A. O2", "B. CO2", "C. H2O", "D. NaCl", "C", "1,00,000"],
    ["How many continents are there on Earth?", "A. 5", "B. 6", "C. 7", "D. 8", "C", "70,000"],
    ["What is the smallest prime number?", "A. 0", "B. 1", "C. 2", "D. 3", "C", "4,00,000"],
    ["Which planet is closest to the Sun?", "A. Venus", "B. Earth", "C. Mars", "D. Mercury", "D", "10,000"],
    ["Who painted the 'Mona Lisa'?", "A. Picasso", "B. Van Gogh", "C. Leonardo da Vinci", "D. Michelangelo", "C", "7,00,000"],
    ["Which language is primarily spoken in Brazil?", "A. Spanish", "B. French", "C. Portuguese", "D. English", "C", "4,000"]
]

random.shuffle(questions)
prize = 0
right = 0
wrong = 0
total_answered = 0

for question in questions:
    print(question[0])
    print(question[1])
    print(question[2])
    print(question[3])
    print(question[4])
    print("Press 'Q' for quiting!")
    print(f"Prize amount for correct solution is {question[6]}")
    
    while True:
        ans = input("Option (A/B/C/D/Q) : ")
        if ans.upper() not in ['A','B','C','D']:
            print("Select Valid option")
            continue
        break

    if ans.upper() == question[5]:
        print("Correct Answer..")
        prize += int(question[6].replace(",",""))
        right += 1
    else:
        print("Hard Luck..")
        prize -= 10000
        wrong += 1
    if ans.upper() == 'Q':
        break
    
    total_answered += 1
    print()


print("Your Scoreboard");print()
print(f"Total questions faced : {total_answered}")
print(f"Correct Answer : {right}")
print(f"Wrong Answers : {wrong}")
print(f"Total Prize won : {prize}")
