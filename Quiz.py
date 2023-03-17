def wrong(correct_answer):
    print(f"Wrong, the answer was actually {correct_answer}.")

def wrong_input():
     x = input("""Press 1 if you would like to go to the next question
    Press 2 if you want to see all questions and answers
    Press 3 if you want to exit the program""")

     if x == '3':
         exit("Hope you liked the quiz")
     elif x == '2':
         input()
     elif x == '1':
         return ()

name = input("What's your name?: ")
welcome = print(f"Hey {name}, welcome to my General Knowledge quiz!! Let's Begin.")
question1 = input("What is the capital of New Jersey?: ")
question1 = question1.upper()
answer1 = "TRENTON"
answer2 = '6'
if question1 == answer1:
    print("Yaay, you got it!!")
    wrong_input()

else:
    wrong(answer1)
    wrong_input()








