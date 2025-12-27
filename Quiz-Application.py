def quiz_app():
    print("----- PYTHON QUIZ APPLICATION -----\n")

    questions = [
        {
            "question": "What is the output of print(2 ** 3)?",
            "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
            "answer": "B"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. function", "B. define", "C. def", "D. fun"],
            "answer": "C"
        },
        {
            "question": "Which data type is immutable?",
            "options": ["A. List", "B. Set", "C. Dictionary", "D. Tuple"],
            "answer": "D"
        },
        {
            "question": "What does len() function return?",
            "options": ["A. Size", "B. Type", "C. Value", "D. Memory"],
            "answer": "A"
        }
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("✔ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}\n")

    print("----- QUIZ RESULT -----")
    print(f"Your Score: {score} / {len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")

quiz_app()
