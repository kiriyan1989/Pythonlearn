from question import question

question_prompt = [
    "what is my name? \n (a) Kiriyan \n(b) Tha \n(c) Bala\n \n" ,
    "what is my age? \n (a) 20 \n(b) 30 \n(c) 40 \n\n" ,
    "what is my location ? \n (a) Glasgow \n(b) London \n(c) NYC\n\n"
]

questions = [
    question(question_prompt[0], "a"),
    question(question_prompt[1], "b"),
    question(question_prompt[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
             score = score + 1
    print("You got " + str(score) + "/" + str(len(questions) + " Correct"))

    run_test(questions)

    #Hello2 - cloned repo commit.