from question import question

question_prompt = [
    "what is my name? \n (a) Kiriyan \n(b) Tha \n(c) Bala\n \n" ,
    "what is my age? \n (a) 20 \n(b) 30 \n(c) 40 \n\n" ,
    "what is my location ? \n (a) Glasgow \n(b) London \n(c) NYC\n\n"
]

questions = [               
    question(question_prompt[0], "a"), # create 1st question object, 
                                       # call 'question' class init function in the question.py file.
                                       # call with values from above list.
    
    question(question_prompt[1], "b"), # create 2nd question object
    question(question_prompt[2], "a"), # create 3rd question object
]



def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
             score = score + 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")


run_test(questions)