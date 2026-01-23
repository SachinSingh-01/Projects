'''Quiz Game Application (Moderate)
What to build
Multiple questions with options
Score calculation
Final result display
Concepts used
List of dictionaries for questions
Loop for question flow
if-else for answer checking
Function to run quiz
Strings for questions and answers'''
quiz=[
    {
    "Question":"Who is the prime minister of india?",
    "Option":["A.Sachin singh", "B.Narendra Modi", "C.Elon musk","D.Punit superstar"],
    "Answer":"B"
},
{
    "Question":"Capital of India?",
    "Option":["A.Kolkata", "B.Bihar", "C.New Delhi","D.Punjab"],
    "Answer":"C"
},
{
    "Question":"Father of nation?",
    "Option":["A.Mahatma Gandhi", "B.Albert Einstin", "C.Mark Zuckerberg","D.Ratan Tata"],
    "Answer":"A"
}
]
def run_quiz(myquiz):
    score=0
    for each_question in myquiz:
        print(each_question["Question"])
        for option in each_question["Option"]:
            print(option)
        print()
        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == each_question["Answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong!\n")
    print("Your final score is:", score, "out of", len(myquiz))
run_quiz(quiz)

