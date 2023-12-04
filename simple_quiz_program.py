quiz = {
    "question 1":{
        "question": "What is the capital of Nigeria?",
        "answer": "",
    },

    "question 2":{
        "question": "What is the capital of Australia?",
        "answer": "",
    },

    "question 3":{
        "question": "What is the capital of South Africa?",
        "answer": "",
    },

    "question 4":{
        "question": "What is the capital of Switzerland",
        "answer": "",
    },

    "question 5":{
        "question": "What is the capital of Portugal",
        "answer": "",
    },

    "question 6":{
        "question": "What is the capital of Senigal",
        "answer": "",
    },

    "question 7":{
        "question": "What is the capital of Austria",
        "answer": "",
    },

    "question 8":{
        "question": "What is the capital of Germany",
        "answer": "",
    },
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Please input your answer: ")

    if answer.lower() == value["answer"]:
        print("Correct")
        score += 1
        print("Your current score is : " + score)
    else:
        print("Incorrect")
        print("The answer is: " + value["answer"])
        print("Your score is: " + str(score))

print("You got score " + str(score) + " out of 8 questions")
print("your percentage is " + str(int(score / 8 * 100)) + "%")